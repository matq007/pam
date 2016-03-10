#!/usr/bin/python
from classes.Configure import Configure
from classes.Listener import Listener
from classes.SentenceParser import SentenceParser

if __name__ == "__main__":

    # SETTING VARIABLES FROM CONFIG
    print "Reading configuration file"
    config = Configure()
    listener = Listener(config.WIT_AUTH_KEY)

    print "Starting listening"
    # sentence = listener.run()
    sentence = "Lights 90"
    sentence_parser = SentenceParser(sentence)

