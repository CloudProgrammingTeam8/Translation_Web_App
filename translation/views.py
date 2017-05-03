from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render ,render_to_response
from .GTAPI import GTTS   # Google Translate Text To Speech
from .speechrecogition_example import SpeechRecogition  # SpeechRecogition
from .models import *

# Create your views here.
def translate(request):
    return render(request, 'trans/index.html')

def TextInput(request):

    if 'username' in request.GET:
        source_lan = request.GET['source_lan']
        target_lan = request.GET['target_lan']
        username = request.GET['username']
        print (source_lan, target_lan)
        SRtext,input_url = SpeechRecogition(source_lan)
        print (input_url)
        
        time = datetime.now().replace(microsecond=0)

        record = Record()
        record.words = SRtext
        record.user = username
        record.time = time
        record.input_lan = source_lan
        record.save()

        print (time)
    
    # if 'TranslateInput' in request.GET:
        # Totaltime , Filename , TranslateResult , url = GTTS(request.GET['TranslateInput'])
        Totaltime , Filename , TranslateInput, TranslateResult , output_url = GTTS(SRtext,target_lan,source_lan)
        # your responese
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
        print (response)
        return render_to_response('trans/index.html',response)
    else:
        return render_to_response('trans/index.html',locals())

