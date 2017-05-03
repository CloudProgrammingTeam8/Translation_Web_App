import speech_recognition as sr

def microphone():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    return audio

def speech_rec(audio, language):
    # recognize speech using Google Speech Recognition
    r = sr.Recognizer()
    #record txt
    return_txt=""
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return_txt = r.recognize_google(audio, language = language)
    except sr.UnknownValueError:
        return_txt = "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return_txt = "Could not request results from GoogleSpeech Recognition service; {0}".format(e)

    #print(return_txt)
    return return_txt

def write_to_file(name, audio):
    #write audio to a WAV file
    with open(name, "wb") as f:
        f.write(audio.get_wav_data())
