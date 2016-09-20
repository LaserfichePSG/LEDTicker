from Led_Board import Led_Board

#initialization params
length = 9
height = 5

message = "hello world!"

strip_options = {"led_pin": 18, "led_frequency": 800000, "led_dma": 5, "led_invert": False, "led_brightness": 255}

#initialize board
test_board = Led_Board(length, height, message, strip_options)

#display message certain number of times
count = 0
buffer = 100
while (count < 5):
    test_board.display_message(buffer)
    count = count + 1

#turn off board
test_board.turn_off()
