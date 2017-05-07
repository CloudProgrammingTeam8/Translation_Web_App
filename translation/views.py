from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render ,render_to_response
from .GTAPI import GTTS   # Google Translate Text To Speech
from .speechrecogition_example import SpeechRecogition  # SpeechRecogition
from .models import *
import boto3
import time
import pymysql

def db():
    conn = pymysql.connect(host='djangords.cldbugjrni6b.us-east-1.rds.amazonaws.com',\
        port=3306, user='bossi', passwd='bossiwai830601', db='Django')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM Django3")
    data = cur.fetchall()
    # print(data)
    return data

# Create your views here.
def TextInput(request):

    if 'username' in request.GET:
        source_lan = request.GET['source_lan']
        target_lan = request.GET['target_lan']
        username = request.GET['username']

        SRtext,input_url = SpeechRecogition(source_lan)
        
        time = str(datetime.now().replace(microsecond=0))

        Totaltime , Filename , TranslateInput, TranslateResult , output_url = GTTS(SRtext,target_lan,source_lan)

        #send a message in SQS
        
        message = {
                    'Username':{'DataType': 'String','StringValue':username},
                    'Time':{'DataType': 'String','StringValue':time},
                    'SourceLan':{'DataType': 'String','StringValue':source_lan},                    
                    'InputWord':{'DataType': 'String','StringValue':SRtext}, 
                    'TargetLan':{'DataType': 'String','StringValue':target_lan}, 
                    'TranslateResult':{'DataType': 'String','StringValue':TranslateResult}, 

        }  

        queue = boto3.client('sqs')
        queue_url = 'https://queue.amazonaws.com/977546219141/ForDjangoRecord'
        # Put Message
        queue.send_message(QueueUrl=queue_url,DelaySeconds=10,MessageAttributes = message , MessageBody=(SRtext))
        records = db()
        # your response
        response = {
                    'TranslateText':SRtext,
                    'Totaltime':Totaltime,
                    'Filename':Filename ,
                    'Speech':TranslateInput,
                    'TranslateResult':TranslateResult,
                    'flag' : 2,
                    'Mp3url':output_url,
                    'Srcurl':input_url,
                    'records':records,
                   }        
        print(response)
        # print (message)
        return render_to_response('trans/index.html',response)
    else:
        records = db()
        return render_to_response('trans/index.html',{'records':records})

def Delete(request):

    time = request.GET['time']
    conn = pymysql.connect(host='djangords.cldbugjrni6b.us-east-1.rds.amazonaws.com',\
      port=3306, user='bossi', passwd='bossiwai830601', db='Django')
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("DELETE FROM Django3 WHERE T = %s", (time,))
    conn.commit()

    records = db()
    return HttpResponseRedirect('/')
