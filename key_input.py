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
            pres_release(k)
    
    def pres_release(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)
    
    def tab(self):
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.tab) 
        
    def alt_tab(self):
        with self.keyboard.pressed(Key.alt_l):
            self.keyboard.press(Key.tab)
            self.keyboard.release(Key.tab)        
    
    def copy_paste(self, tip):
        if tip == "v":
            with self.keyboard.pressed(Key.ctrl_l):
                self.keyboard.press('v')
                self.keyboard.release('v')
                
        else:
            with self.keyboard.pressed(Key.ctrl_l):
                self.keyboard.press('c')
                self.keyboard.release('c')
    def enter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
    
    def escape(self):
        self.keyboard.press(Key.esc)
        self.keyboard.release(Key.esc)
    
    def shift_F_deset(self):
        with self.keyboard.pressed(Key.shift_l):
            self.keyboard.press(Key.f10)
            self.keyboard.release(Key.f10)        
