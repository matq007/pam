#!/usr/bin/python
from textblob import TextBlob
from models import *


class SentenceParser:
    def __init__(self, sentence):
        self.sentence = TextBlob(sentence)
        self.analyze()
        print self.sentence.words

    def analyze(self):
        keyword_exists = False

        # TODO: Check if keywords exists in our database

        for word, pos in self.sentence.tags:
            if pos.encode('utf-8') == "NN":
                keyword_exists = True
                self.create_model(word)

        if not keyword_exists:
            for word, pos in self.sentence.tags:
                if pos.encode('utf-8') == "NNS":
                    self.create_model(word.singularize())

    def create_model(self, name):
        class_name = name.encode('utf-8').title()
        _class = globals()[class_name]
        _class(str(self.sentence))                      # dynamic initialization
