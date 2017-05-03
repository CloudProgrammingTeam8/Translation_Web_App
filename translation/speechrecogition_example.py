from .test_lex.microphone_rec import *
from .test_s3.s3_test import *
from subprocess import call
import time , os

def SpeechRecogition(language):
    #save voice path
    localtime = time.localtime(time.time())
    data_path = language+'_'+str(localtime.tm_year) + '_' + str(localtime.tm_mon) + '_' + \
    str(localtime.tm_mday) + '_' + str(localtime.tm_hour) + '_' + \
    str(localtime.tm_min) + '_' + str(localtime.tm_sec) + '.mp3'
    #s3 bucket path
    s3_path = 'django-speech-storage' #bucket name
    #recognation language
    #Traditional Taiwan language: zh-TW
    #English(US): en-US
    #Japanese: ja
    #Thailand: th-TH
    #language = 'en-US'

    #launch microphone and get audio
    audio = microphone()
    #transfer vocie into txt
    return_txt = speech_rec(audio, language)
    # return return_txt
    # #write txt to file
    write_to_file(data_path, audio)
    # #create s3 bucket
    # create_s3_bucket(s3_path)
    # #upload data to s3 bucket
    upload(data_path, s3_path)
    # #remove record.wav from local
    # call(["rm", data_path])

    url = 'https://s3.amazonaws.com/'+s3_path+"/"+data_path
    os.remove(data_path)
    return return_txt, url
    #download all data for bucket
    # print("DOWNLOADING...")
    # bucket_name = 'mike5'
    # save_path = './tmp/'
    # download_all_data(bucket_name, save_path)
