from MatrixRGB import Matrix
from neopixel import *
import Led_Character_Map


#class to represent LED board
class Led_Board(object):

    #constructor
    def __init__(self, length, height, message, strip_options):

        #validate inputs
        if (not type(length) is int or length < 1 or not type(height) is int or height < 1 or not type(message) is str or len(message) < 1 or not type(strip_options) is list or not len(strip_options) == 5):
            print ("BAD INPUTS")
            
        self.length = length
        self.height = height
        self.message_string = message
        self.strip = Adafruit_NeoPixel((length*height), strip_options["led_pin"], strip_options["led_frequency"], strip_options["led_dma"], strip_options["led_invert"], strip_options["led_brightness"])
        self.message_matrix = self.generate_message_matrix()
        #self.frame = self.message_matrix.get_submatrix(self.height, self.length)


    #create a message matrix from internal message string
    def generate_message_matrix():
        count = 0
        result = None
        for char in self.message_string:
            temp = char_map[char]
            if (count == 0):
                result = temp
                result = result.concatenate(Matrix(self.height, 1))
            else:
                result = result.concatenate(temp)
                result = result.concatenate(Matrix(self.height, 1))
            count = count + 1

        #pad with empty pixels to fill out board
        if (result.n < self.length):
            result = result.concatenate(Matrix(self.height, self.length - result.n))

        return result


    #translate current message matrix into frame for strip
    def set_frame():
        range_start = 0
        range_end = self.length - 1
        for m in range(self.height):
            for n in range(self.length):
                #no inversion
                temp = Color(self.message_matrix[m][n][0], self.message_matrix[m][n][1], self.message_matrix[m][n][2])
                if (m % 2 == 0):
                     self.strip.setPixelColor(range_start + n, temp)
                #inversion required
                else:
                    self.strip.setPixelColor(range_end - n, temp)
            range_start = range_start + length
            range_end = range_end + length
    
    #shift message matrix to reflect new frame
    def shift_frame():
        self.message_matrix = self.message_matrix.shift_horizontal(True, Matrix(self.height, 1))
        #self.frame = self.message_matrix.get_submatrix(self.height, self.length)

    #turn off all pixels
    def turn_off():
        color = Color(0, 0, 0)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
