from MatrixRGB import Matrix
from Led_Character_Map import char_map
import time



#create a message matrix from internal message string
def generate_message_matrix(message, height, length):
    count = 0
    result = None
    for char in message:
          temp = char_map[char]
          if (count == 0):
               result = temp
               result = result.concatenate(Matrix(height, 1))
          else:
               result = result.concatenate(temp)
               result = result.concatenate(Matrix(height, 1))
          count = count + 1

    #pad with empty pixels to fill out board
    if (result.n < length):
          result = result.concatenate(Matrix(height, length - result.n))

    return result


#display matrix
def display(matrix, length):
    for m in range(matrix.m):
        hold = ""
        for n in range(length):
            if (matrix.rows[m][n] == (255,255,255)):
                hold += "."
            else:
                hold += " "
        print (hold)


#main function
def execute(message, length, height, buffer):

    test = generate_message_matrix(message, height, length)
    while (not test.is_empty()):
        display(test, length)
        test.shift_horizontal(True, Matrix(height, 1))
        print ("")
        time.sleep(buffer)

execute("hello world!", 9, 5, 0.1)

                
