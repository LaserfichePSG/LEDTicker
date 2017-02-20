import os.path
from datetime import datetime

class LogWriter:
    
    #constructor
    #format path to log and create log if it doesn't exist
    def __init__(self, file_path, file_name, mode):
        self._file_path = (file_path + "\\" + file_name + ".txt")
        self._mode = mode
        
        if not os.path.isfile(self._file_path):
            temp = open(self._file_path, 'w')
            temp.close()
            
    #format and write log message to file
    def WriteLog(self, msg, mode):
        
        if mode <= self._mode:
            mode_string = ""
            if mode == 0:
                mode_string = "[ERROR]"
            elif mode == 1:
                mode_string = "[INFO]"
            elif mode == 2:
                mode_string = "[DEBUG]"
            else:
                mode_string = ""
            
            f = open(self._file_path, 'a')
            today = datetime.today()
            message = (mode_string + " " + str(today) + ": " + msg + '\n')
            f.write(message)
            f.close()
        
        return self
    
if __name__ == "__main__":
    global log
    log = LogWriter(r'c:\users\josh.kimmel\desktop', 'test_log', 0)
    
        