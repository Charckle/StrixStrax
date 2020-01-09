import pynput
from pynput.keyboard import Key, Controller
from time import sleep
import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN


#USE ONLY VIRTUAL!!!!!!!

UP = 0x26
DOWN = 0x28
LEFT = 0x25
RIGHT = 0x27

ESC = 0x1B
SPACE = 0x20
RETURN = 0x0D  #enter
INSERT = 0x2D

DELETE = 0x2E
HOME = 0x24 
LCONTROL = 0xA2
VK_CONTROL = 0x11
LSHIFT = 0xA0

TAB = 0x09
LALT = 0x12

F2 = 0x71
F10 = 0x79

A = 0x41
C = 0x43
V = 0x56

PERIOD = 0xBE

# C struct definitions
wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize


class KeyBoardHandler():
    def __init__(self, def_sleep=1):
        self.keyboard = Controller()
        
        self.default_sleep = def_sleep
        
        self.SendInput = ctypes.windll.user32.SendInput
        
    def PressKey(self, hexKeyCode):
        x = INPUT(type=INPUT_KEYBOARD,
                  ki=KEYBDINPUT(wVk=hexKeyCode))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

    def ReleaseKey(self, hexKeyCode):
        x = INPUT(type=INPUT_KEYBOARD,
                  ki=KEYBDINPUT(wVk=hexKeyCode,
                                dwFlags=KEYEVENTF_KEYUP))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
    
    def wai_t(self, seconds: int):
        print(f"[ ] - Sleeping for {seconds} seconds")
        sleep(seconds)
        
    def parse_word(self, word):
        keys = []   
        for k in word:
            keys.append(k)
        return keys
    
    def push_keys(self, to_type):
        
        for k in self.parse_word(to_type):
            self.pres_release(k)
            sleep(0.05*self.default_sleep)
    
    def pres_release(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)
        sleep(0.05*self.default_sleep)
    
    def right_arrow(self):
        self.PressKey(RIGHT)
        self.ReleaseKey(RIGHT)
        
    def left_arrow(self):
        self.PressKey(LEFT)
        self.ReleaseKey(LEFT)
        
    def down_arrow(self):
        self.PressKey(DOWN)
        self.ReleaseKey(DOWN)    
        
    def up_arrow(self):
        self.PressKey(UP)
        self.ReleaseKey(UP)
    
    def l_shift(self):
        self.PressKey(LSHIFT)
        self.ReleaseKey(LSHIFT)
        
    def l_control(self):
        self.PressKey(LCONTROL)
        self.ReleaseKey(LCONTROL)
        sleep(0.2*self.default_sleep)    
        
    def enter(self):
        self.PressKey(RETURN)
        self.ReleaseKey(RETURN)
        sleep(0.3*self.default_sleep)
        
    def insert(self):
        self.PressKey(INSERT)
        self.ReleaseKey(INSERT)
        sleep(0.5*self.default_sleep)
    
    def delete(self):
        self.PressKey(DELETE)
        self.ReleaseKey(DELETE)
        sleep(0.5*self.default_sleep)
    
    def home(self):
        self.PressKey(HOME)
        self.ReleaseKey(HOME)
        sleep(0.5*self.default_sleep)
        
    def period(self):
        self.PressKey(PERIOD)
        self.ReleaseKey(PERIOD)
        sleep(0.5*self.default_sleep)
        
    
    def tab(self):
        self.PressKey(TAB)
        self.ReleaseKey(TAB)
        sleep(1*self.default_sleep)

    def escape(self):
        self.PressKey(ESC)
        self.ReleaseKey(ESC)
        sleep(0.5*self.default_sleep)
        
    def spacebar(self):
        self.PressKey(SPACE)
        self.ReleaseKey(SPACE)  
        sleep(0.2*self.default_sleep)

    def f_dva(self):
        self.PressKey(F2)
        self.ReleaseKey(F2)  
        sleep(0.2*self.default_sleep)          
    
    def alt_tab(self):
        self.PressKey(LALT)
        self.PressKey(TAB)
        self.ReleaseKey(TAB)    
        self.ReleaseKey(LALT)
        sleep(1*self.default_sleep)
    
    def copy_paste(self, tip):
        if tip == "v":
            self.PressKey(LCONTROL)
            self.PressKey(V)
            self.ReleaseKey(V)
            self.ReleaseKey(LCONTROL)    
                
        else:
            self.PressKey(LCONTROL)
            self.PressKey(C)
            self.ReleaseKey(C)
            self.ReleaseKey(LCONTROL)    
        
        sleep(0.5*self.default_sleep)    
    
    def shift_F_deset(self):
        self.PressKey(LSHIFT)
        self.PressKey(F10)
        self.ReleaseKey(F10)
        self.ReleaseKey(LSHIFT)         

        sleep(0.3*self.default_sleep)    
      
    def ctrl_a(self):
        self.PressKey(VK_CONTROL)
        self.PressKey(A)
        self.ReleaseKey(A)        
        self.ReleaseKey(VK_CONTROL)
        
        sleep(0.5*self.default_sleep)    
    
    def shift_tab(self):
        self.PressKey(LSHIFT)
        self.PressKey(TAB)
        self.ReleaseKey(TAB)        
        self.ReleaseKey(LSHIFT)
        
        sleep(0.5*self.default_sleep)    
   
   
    
    #NON citrix buttons
    
    '''
    def shift_tab(self):
        with self.keyboard.pressed(Key.shift_l):
            self.keyboard.press(Key.tab)
            self.keyboard.release(Key.tab)
        sleep(0.5*self.default_sleep)
    
    def ctrl_a(self):
        with self.keyboard.pressed(Key.ctrl_l):
            self.keyboard.press('a')
            self.keyboard.release('a')
        sleep(0.2*self.default_sleep)

    def ctrl_a(self):
        with self.keyboard.pressed(Key.ctrl_l):
            self.keyboard.press('a')
            self.keyboard.release('a')
        sleep(0.2*self.default_sleep)

    def noncitrix_f_dva(self):
        self.keyboard.press(Key.f2)
        self.keyboard.release(Key.f2)
        sleep(0.2*self.default_sleep)

    def nonCitrix_spacebar(self):
            self.keyboard.press(Key.space)
            self.keyboard.release(Key.space)
            sleep(0.2*self.default_sleep)

    def nonCitrix_shift_F_deset(self):
        with self.keyboard.pressed(Key.shift_l):
            self.keyboard.press(Key.f10)
            self.keyboard.release(Key.f10)
        
        sleep(0.3*self.default_sleep)

    def nonCitrix_escape(self):
        self.keyboard.press(Key.esc)
        self.keyboard.release(Key.esc)
        sleep(0.5*self.default_sleep)

    def nonCitrix_copy_paste(self, tip):
        if tip == "v":
            with self.keyboard.pressed(Key.ctrl_l):
                self.keyboard.press('v')
                self.keyboard.release('v')
                
        else:
            with self.keyboard.pressed(Key.ctrl_l):
                self.keyboard.press('c')
                self.keyboard.release('c')
        
        sleep(0.5*self.default_sleep)

    def nonCitrix_enter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        sleep(0.3*self.default_sleep)

    def nonCitrix_alt_tab(self):
        with self.keyboard.pressed(Key.alt_l):
            self.keyboard.press(Key.tab)
            self.keyboard.release(Key.tab)
        
        sleep(1*self.default_sleep)

        
    def nonCitrix_tab(self):
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.tab)
        sleep(1*self.default_sleep)
    '''

if __name__ == '__main__':
    sleep(3)
    banana = KeyBoardHandler()
    banana.alt_tab()
    banana.ctrl_a()
    banana.copy_paste("c")
    banana.home()
    banana.copy_paste("v")    
    
    banana.period()
    
    
    
    '''
    banana.copy_paste("c")
    #banana.copy_paste("v")
    banana.push_keys("Tomi")
    banana.copy_paste("v")
    banana.tab()
    banana.enter()
    '''
    
    