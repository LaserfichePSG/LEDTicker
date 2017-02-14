from flask import Flask, request
from Led_Board import Led_Board
from Led_Character_Map import char_map
from Led_Config import Led_Config
#import Led_Display_Test

app = Flask(__name__)

@app.route("/LedMessage", methods=['POST'])

def LedMessage ():

    #validate request param
    content = request.get_json(force=True)
    
    msg = str(content["message"]).lower()
    
    for char in msg:
        if not char in char_map:
            return ("Invalid message input. Unknown character: '" + str(char) + "'")

    #initialize board
    led_board = None
    config = Led_Config()
    try:
        led_board = Led_Board(config.board_length, config.board_height, msg, config.strip_options)
    except:
        return ("Could not initialize LED board! Please run in debug mode for more information.")
        
    #display message certain number of times
    #POSSIBLY MULTI-THREAD THIS SO THAT THE REQUESTER ISNT TIED UP FOR THE DURATION OF THE MESSAGE DISPLAY
    count = 0
    while (count < config.display_count):
        try:
            led_board.display_message(config.scroll_buffer)
        except:
            return ("Error displaying message! Please run in debug mode for more information.")
        count = count + 1

    #turn off board
    led_board.turn_off()

    '''
    #testing Flask app
    content = request.get_json(force=True)
    Led_Display_Test.execute(content["message"], 25, 5, 0.3)

    '''
    
    return "Message display finished."



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
