import time
import asyncio
import threading
import sys
from LogWriter import LogWriter
from api_exceptions import *
from flask import Flask, request, jsonify
from Validator import Validator
from Executor import Executor

#global vars
q = asyncio.Queue()
EndQueue = False
t = None
log = LogWriter('logs', 'led_log', 2)
validator = None
executor = None

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

    #validate request params
    content = request.get_json(force=True)
    
    display_type = None
    command = None
    try:
        display_type = str(content["type"]).lower()
    except Exception as e:
        inner = GetInnerException()
        log.WriteLog("Bad request body: " + inner, 0)
        raise BadRequest("Could not extract board request type!", inner)
        
    try:
        command = str(content["command"]).lower()
    except Exception as e:
        inner = GetInnerException()
        log.WriteLog("Bad request body: " + inner, 0)
        raise BadRequest("Could not extract board request command!", inner)
        
    validator = Validator(display_type, command)
    result = False
    try:
        result = validator.ValidateRequest()
    except Exception as e:
        inner = GetInnerException()
        log.WriteLog("Bad request body: " + inner, 0)
        raise BadRequest("Request failed validation!", inner)
    
    if result:
        #push valid requests to a job queue for async processing
        q.put_nowait((display_type, command))
        log.WriteLog("Queued command "+(display_type, command), 2)
        if q.empty():
            return "Your command will be executed momentarily."
        else:
            return "Your command has been queued and will be executed when the board is next available."
        
    
    
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

#method to facilitate the execution of a given command
def ExecuteCommand (command):
    
    executor = Executor(command[0], command[1])
    try:
        executor.ExecuteCommand()
    except Exception as e:
        inner = GetInnerException()
        log.WriteLog("Command execution error for " + command + ": " + inner, 0)
    
    

#method to execute pending jobs in the job queue
#this runs in an independent thread
def ProcessQueue ():
    
    #while web server is running, grab jobs from the global job queue to execute
    while (not EndQueue):
        if not q.empty():
            command = q.get_nowait()
            log.WriteLog("Executing command " + msg, 2)
            ExecuteCommand(command)
            time.sleep(1)
            
    #once web server has been terminated, process remaining jobs in the queue
    while (not q.empty()):
        command = q.get_nowait()
        log.WriteLog("Executing command " + msg, 2)
        ExecuteCommand(command)
        
    #finally, terminate the program
    log.WriteLog("Program terminated", 1)
    sys.exit()
    

#main application entry point
if __name__ == "__main__":
    t = threading.Thread(target=ProcessQueue)
    t.start()
    log.WriteLog("Program started", 1)
    app.run(host='0.0.0.0', port=4000)
