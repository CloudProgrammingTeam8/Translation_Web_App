import os, boto3
import requests
import time
from gtts import gTTS
from .goslate import gtrans

def GTTS(TranslateInput,TextLanguage,src):
    # Documents : https://pypi.python.org/pypi/gTTS 
   
    # Translate (input from TextInput)
    start_time = time.time()   # time start
    TranslateResult = gtrans(TranslateInput, TextLanguage, src)
    
    # Texy to Speech
    tts = gTTS(text=TranslateResult, lang=TextLanguage, slow=False)
    # Save mp3 to local client
    localtime = time.localtime(time.time())
    # File Name
    filename = TextLanguage + '_' + str(localtime.tm_year) + '_' + str(localtime.tm_mon) + '_' + \
    str(localtime.tm_mday) + '_' + str(localtime.tm_hour) + '_' + \
    str(localtime.tm_min) + '_' + str(localtime.tm_sec) + '.mp3'
    tts.save(filename)
    
    # Excute Time
    total_time = time.time() - start_time
    print("--- %s seconds for GTTS---" % (total_time))  # time end
    
    # Save to S3
    #upload data to exist buckets
    s3 = boto3.client('s3')
    TargetBucket = 'django-speech-storage'
    data = open(filename, 'rb')
    s3.put_object(Key=filename, 
                  Body=data,
                  Bucket = TargetBucket,
                  ACL = 'public-read-write')

    # get s3 url
    url = 'https://s3.amazonaws.com/'+TargetBucket+"/"+filename
    
    # Play on Mac localhost
    # os.system('afplay filename')
    os.remove(filename)

    return  total_time  , filename , TranslateInput, TranslateResult , url
