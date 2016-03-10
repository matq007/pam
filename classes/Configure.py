#!/usr/bin/python
import ConfigParser
import os.path


class Configure:
    def __init__(self):
        self.APP_VERSION = "0.1"
        self.CONFIG_FILENAME = "config.conf"
        self.FIRST_NAME = ""
        self.LAST_NAME = ""
        self.WIT_AUTH_KEY = ""
        self.profile = {}
        self.exists()

    def exists(self):
        if not os.path.exists(self.CONFIG_FILENAME):
            self.create_config()
        else:
            self.get_data()

    def create_config(self):
        print "Welcome to P.A.M system. You we need to setup some information for us"
        print "Please enter first name:"
        self.simple_request('FIRST_NAME', 'First Name')
        print "Please enter last name:"
        self.simple_request('LAST_NAME', 'Last Name')
        print "Required in order to work. Enter Wit.Ai api key"
        self.simple_request('API_KEY', 'Api key')
        config = ConfigParser.RawConfigParser()
        config.add_section('INFO')
        config.add_section('WITAI')
        config.set('INFO', 'FIRST_NAME', self.profile['FIRST_NAME'])
        config.set('INFO', 'LAST_NAME', self.profile['LAST_NAME'])
        config.set('WITAI', 'API_KEY', self.profile['API_KEY'])

        with open(self.CONFIG_FILENAME, 'wb') as configfile:
            config.write(configfile)

        self.welcome()

    def welcome(self):
        self.get_data()
        text = "Hello" + self.FIRST_NAME + " " + self.LAST_NAME + ", my name is PAM. " \
               "I am your personal appliance manager. You have successfully integrated me in your home."
        command = 'echo "%s" | festival --tts' % text
        os.system(command)

    def simple_request(self, var, cleanVar, cleanInput=None):
        input = raw_input(cleanVar + ": ")
        if input:
            if cleanInput:
                input = cleanInput(input)
            self.profile[var] = input

    def get_data(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read(self.CONFIG_FILENAME)
            self.FIRST_NAME = config.get("INFO", "FIRST_NAME")
            self.LAST_NAME = config.get("INFO", "LAST_NAME")
            self.WIT_AUTH_KEY = str(config.get("WITAI", "API_KEY"))
        except ConfigParser.NoSectionError as e:
            print "Section doesn't exist " + e.message
        except ConfigParser.NoOptionError as e:
            print "Option doesn't exist " + e.message
        except ConfigParser.ParsingError as e:
            print "File doesn't exist: " + e.message
