#!/usr/bin/python
import ConfigParser


class Configure:
    def __init__(self):

        self.APP_VERSION = "0.1"
        self.CONFIG_FILENAME = "config.conf"

        try:
            config = ConfigParser.ConfigParser()
            config.read(self.CONFIG_FILENAME)
            self.WIT_AUTH_KEY = config.get("WIT", "AUTH_KEY")
        except ConfigParser.NoSectionError as e:
            print "Section doesn't exist " + e
        except ConfigParser.NoOptionError as e:
            print "Option doesn't exist " + e
        except ConfigParser.ParsingError as e:
            print "File doesn't exist: " + e
