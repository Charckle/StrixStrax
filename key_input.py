from pynput.keyboard import Key, Controller
from time import sleep



class KeyBoardHandler():
    def __init__(self):
        self.keyboard = Controller()
        
    def parse_word(self, word):
        keys = []
        for k in word:
            keys.append(k)
        return keys
    
    def push_keys(self, to_type):
        
        for k in self.parse_word(to_type):
            self.keyboard.press(k)
            self.keyboard.release(k)      

