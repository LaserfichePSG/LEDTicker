from flask import Flask, request
#from Led_Board import Led_Board
import Led_Display_Test

app = Flask(__name__)

@app.route("/LedMessage", methods=['POST'])

def LedMessage ():

    #validate request param

    #grab initialization params from a config
    '''
    length = 300
    height = 5

    strip_options = strip_options = {"led_pin": 18, "led_frequency": 800000, "led_dma": 5, "led_invert": False, "led_brightness": 150}

    #initialize board
    led_board = Led_Board(length, height, request.form[message], strip_options)

    #display message certain number of times
    count = 0
    buffer = 0.1
    while (count < 5):
        test_board.display_message(buffer)
        count = count + 1

    #turn off board
    test_board.turn_off()
    '''

    content = request.get_json(force=True)
    Led_Display_Test.execute(content["message"], 25, 5, 0.3)

    return "Message display finished."



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
