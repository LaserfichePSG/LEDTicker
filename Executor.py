'''
THIS CLASS IS USED TO EXECUTE BOARD DISPLAYS PULLED OFF OF THE LED JOB QUEUE
'''

from Led_Config import Led_Config
from Led_Board import Led_Board
import time

class Executor:
    
    #constructor
    def __init__(self, display_type, command):
        self._type = display_type
        self._command = command
        
    
    #main executor method
    def ExecuteCommand(self):
        
        #call helper method depending on type
        if self._type == "message":
            self.ExecuteLedMessage()
        elif self._type == "command":
            self.ExecuteLedCommand()
        else:
            raise ("This type has not been implemented yet!")
            
    #method to display messages to the LED board
    def ExecuteLedMessage(self):
        #initialize board
        led_board = None
        config = Led_Config()
        try:
            led_board = Led_Board(config.board_length, config.board_height, msg, config.strip_options)
        except Exception as e:
            raise e
        
        #execute display
        try:
            led_board.display_message(config.scroll_buffer)
        except Exception as e:
            raise e

        #turn off board
        led_board.turn_off()
        
    
    #method to execute command display logic
    def ExecuteLedCommand(self):
        raise ("Command not implemented yet!")
        
        