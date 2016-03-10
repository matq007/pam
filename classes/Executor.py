#!/usr/bin/python
import os


class Executor:
    def __init__(self, command, response):
        self.command = command
        self.response = response
        self.run()

    def run(self):
        print "Command: " + self.command
        print "Response: " + self.response
        os.system(self.response)
