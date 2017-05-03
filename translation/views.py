from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render ,render_to_response
from .GTAPI import GTTS   # Google Translate Text To Speech
from .speechrecogition_example import SpeechRecogition  # SpeechRecogition
from .models import *
import boto3
import time

# Create your views here.
def translate(request):
    return render(request, 'trans/index.html')

def TextInput(request):

    if 'username' in request.GET:
        source_lan = request.GET['source_lan']
        target_lan = request.GET['target_lan']
        username = request.GET['username']

        SRtext,input_url = SpeechRecogition(source_lan)
        
        time = str(datetime.now().replace(microsecond=0))

        Totaltime , Filename , TranslateInput, TranslateResult , output_url = GTTS(SRtext,target_lan,source_lan)
        # your response
        response = {
                    'TranslateText':SRtext,
                    'Totaltime':Totaltime,
                    'Filename':Filename ,
                    'Speech':TranslateInput,
                    'TranslateResult':TranslateResult,
                    'flag' : 2,
                    'Mp3url':output_url,
                    'Srcurl':input_url
                   }
        #send a message in SQS
        message = {
                    'Username':username,
                    'Time':time,
                    'SourceLan':source_lan,                    
                    'InputWord':SRtext,
                    'TargteLan':target_lan,
                    'TranslateResult':TranslateResult

        }  
            # Get the service resource
    # sqs = boto3.resource('sqs')

    # Get the queue
    # while True:
    #     queue = sqs.get_queue_by_name(QueueName='test')
    #     for message in queue.receive_messages(MessageAttributeNames=['Author']):
    #         #insert to rds
    #         print('Hello, {0}!'.format(message.body))

    #         #Let the queue know that the message is processed
    #         message.delete()
    #     time.sleep(5)

        print(response)
        print (message)
        return render_to_response('trans/index.html',response)
    else:
        return render_to_response('trans/index.html',locals())

