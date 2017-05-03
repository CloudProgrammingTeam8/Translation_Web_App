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
        language = request.GET['language']
        print (language)
        SRtext, input_url = SpeechRecogition(language)
        print (input_url)
        Totaltime , Filename , TranslateInput, TranslateResult , output_url = GTTS(SRtext,'zh-TW',language)
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

