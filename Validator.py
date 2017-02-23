'''
THIS CLASS IS USED TO VALIDATE INCOMING REQUESTS FOR THE LED BOARD  
'''

from Led_Character_Map import char_map

class Validator:
    
    #constructor
    def __init__(self, display_type, command):
        self._type = display_type
        self._command = command
        return self
    
    #main validator method
    def ValidateRequest (self):
        
        #call helper method depending on type
        if self._type == "message":
            return self.ValidateLedMessage()
        elif self._type == "command":
            return self.ValidateLedCommand()
        else:
            raise ("This type has not been implemented yet!")
        
    
    #validator method for message display
    def ValidateLedMessage (self):
        
        for char in self._command:
            if not char in char_map:
                raise ("Invalid character: "+str(char))
            
        return True
            
    #validator method for command display
    def ValidateLedCommand (self):
        raise ("Command has not been implemented yet")