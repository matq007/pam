#!/usr/bin/python
from textblob import TextBlob
from classes.Executor import Executor


class Light:
    def __init__(self, sentence):
        print "MODULE: " + str(self.__class__)
        self.sentence = TextBlob(sentence)
        self.commands = ["on", "off", "set"]
        self.command = ""
        for word, pos in self.sentence.tags:
            if pos.encode('utf-8') == "IN":
                if word.encode('utf-8') in self.commands:
                    self.command = word.encode('utf-8')
            if pos.encode('utf-8') == "RP":
                if word.encode('utf-8') in self.commands:
                    self.command = word.encode('utf-8')
            if pos.encode('utf-8') == "CD":
                self.command = "set"
                self.percent = word.encode('utf-8')

        self.execute()
        # print self.sentence.tags

    def execute(self):
        if self.command == "on":
            self.turn_on()
        elif self.command == "off":
            self.turn_off()
        elif self.command == "set":
            self.set_intensity()
        else:
            print "Command not recognized"

    def turn_on(self):
        text = "Light is on"
        response = 'espeak "%s"' % text
        Executor(text, response)

    def turn_off(self):
        text = "Light is off"
        response = 'espeak "%s"' % text
        Executor(text, response)

    def set_intensity(self):
        text = "Light is on %s percent" % self.percent
        response = 'espeak "%s"' % text
        Executor(text, response)


