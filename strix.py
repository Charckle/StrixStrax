from pynput.keyboard import Key, KeyCode, Listener
from key_input import KeyBoardHandler
from time import sleep
import datetime


print('Strix - An annoying password printer.')

key_stroker = KeyBoardHandler()

# Your functions
def function_1():
    print('Pasting password')
    sleep(1)

    key_stroker.keyboard.release(Key.ctrl_l)
    key_stroker.keyboard.release(Key.cmd)
    #key_stroker.keyboard.press(Key.backspace)
    year = datetime.datetime.now().year
    key_stroker.push_keys(f"Password{year}")
    
    

def function_2():
    print('Executed function_2')

# Create a mapping of keys to function (use frozenset as sets are not hashable - so they can't be used as keys)
combination_to_function = {
    frozenset([Key.right, KeyCode(char='.')]): function_1, # No `()` after function_1 because we want to pass the function, not the value of the function
    frozenset([Key.ctrl_l, Key.cmd]): function_1,
    frozenset([Key.shift, KeyCode(char='B')]): function_2,
}

# Currently pressed keys
current_keys = set()

def on_press(key):
    # When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
        combination_to_function[frozenset(current_keys)]()

def on_release(key):
    # When a key is released, remove it from the set of keys we are keeping track of
    current_keys.remove(key)

while True:
    
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    
    except Exception as e:
        print('something gone wrong???!')
        print(e)