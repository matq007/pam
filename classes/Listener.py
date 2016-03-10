#!/usr/bin/python
import speech_recognition as sr


class Listener:
    def __init__(self, auth_key):
        self.auth_key = auth_key
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.microphone.SAMPLE_RATE = 48000
        self.microphone.CHUNK = 1024

    def run(self):
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.recognizer.listen(source)

        try:
            sentence = self.recognizer.recognize_wit(audio, key=self.auth_key)
            return sentence
        except sr.UnknownValueError:
            print "Wit.ai could not understand audio"
        except sr.RequestError as e:
            print "Could not request results from Wit.ai service; {0}".format(e)