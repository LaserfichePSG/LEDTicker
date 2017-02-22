from neopixel import *
import time

#handles commands in message (indicated by leading "&")
#talks to strip directly, using neopixel library
class Command(object)

	def __init__(self, strip, message)
		self.strip = strip
		self.message = message
		
	def run()
		raise CommandError("I'm afraid I can't do that. (no handling for that command yet)")


#error class
class CommandError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
