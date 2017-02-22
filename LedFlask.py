import time
import asyncio
import threading
import sys
from LogWriter import LogWriter
from api_exceptions import *
from flask import Flask, request, jsonify
from Led_Board import Led_Board
from Led_Character_Map import char_map
from Led_Config import Led_Config

#global vars
q = asyncio.Queue()
EndQueue = False
t = None
log = LogWriter('logs', 'led_log', 2)

app = Flask(__name__)

#format given exception as a string
def GetInnerException():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    return ''.join('!! ' + line for line in lines)

#error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

#this route queues a message up for display on the board
@app.route("/LedMessage", methods=['POST'])
def LedMessage ():

    #validate request param
    content = request.get_json(force=True)
    
    msg = None
    try:
        msg = str(content["message"]).lower()
    except Exception as e:
        inner = GetInnerException()
        log.WriteLog("Bad request body: " + inner, 0)
        raise BadRequest("Could not extract message!", inner)
    
	# check for debug case
	if msg[:1] == '&':
		log.WriteLog("Debug character detected.", 0)
    else:
		for char in msg:
			if not char in char_map: 
				log.WriteLog("Invalid character encountered for message " + msg, 0)
				raise BadRequest("Invalid character encountered", "Bad character: " + str(char))
        
    #push valid message to a job queue for async processing
    q.put_nowait(msg)
    log.WriteLog("Queued message " + msg, 2)
    if q.empty():
        return "Your message will be displayed momentarily."
    else:
        return "Your message has been queued and will be displayed when the board is next available."
    
#this route effectively ends the program
#but first allows the job queue to empty
@app.route("/BoardOff", methods=['DELETE'])
def BoardOff ():
    
    #terminate web server
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
    #flag clearing out of job queue
    global EndQueue
    EndQueue = True
    log.WriteLog("Terminate route called", 1)
    return "The program will end momentarily"

#method to facilitate the display of a single message
def DisplayMessage (msg):
    
    #initialize board
    led_board = None
    config = Led_Config()
    try:
        led_board = Led_Board(config.board_length, config.board_height, msg, config.strip_options)
    except Exception as e:
        log.WriteLog("LED board initialization error: " + GetInnerException(), 0)

    #display message certain number of times
    count = 0
    while (count < config.display_count):
        try:
            led_board.display_message(config.scroll_buffer)
        except Exception as e:
            log.WriteLog("LED board display error: " + GetInnerException(), 0)
        count = count + 1

    #turn off board
    led_board.turn_off()

#method to execute pending jobs in the job queue
#this runs in an independent thread
def ProcessQueue ():
    
    #while web server is running, grab jobs from the global job queue to execute
    while (not EndQueue):
        if not q.empty():
            msg = q.get_nowait()
            log.WriteLog("Displaying message " + msg, 2)
            DisplayMessage(msg)
            time.sleep(1)
            
    #once web server has been terminated, process remaining jobs in the queue
    while (not q.empty()):
        msg = q.get_nowait()
        log.WriteLog("Displaying message " + msg, 2)
        DisplayMessage(msg)
        
    #finally, terminate the program
    log.WriteLog("Program terminated", 1)
    sys.exit()
    

#main application entry point
if __name__ == "__main__":
    t = threading.Thread(target=ProcessQueue)
    t.start()
    log.WriteLog("Program started", 1)
    app.run(host='0.0.0.0', port=4000)
