from pynput import keyboard
import key_input
import sys

username = key_input.KeyBoardHandler()

def do_stuff(break_program):

    #YOUR CODE GOES HERE  ---->
    username.copy_paste("")
    username.alt_tab()
    username.copy_paste("v") #paste
    username.enter()
    username.spacebar()
    username.wai_t(0.5)
    username.shift_F_deset()
    username.wai_t(0.5)
    username.push_keys('m')
    username.wai_t(0.5)
    username.tab()
    username.tab()
    username.tab()
    username.tab()
    username.tab()
    username.tab()
    username.copy_paste("")
    username.alt_tab()
    username.tab()
    username.copy_paste("v")
    username.alt_tab()
    username.tab()
    username.copy_paste("")
    username.escape()
    username.tab()
    username.alt_tab()
    username.f_dva()
    username.copy_paste("v")
    username.enter()
    username.escape()
    print(f"Finished number {break_program}")
    #<---- YOUR CODE GOES HERE


while True:
    do_times = input("How many times do we execute? (Press the END button to stop the loop) ").strip()
    
    #check if given number is correctly formed
    number_ok = True
    for cha in do_times:
        if not cha.isdigit():
            print("Type a number.")
            number_ok = False
            break
    if number_ok == True:
        break

print(f"Ok, it will run for {do_times} times.")

#timer befor the program starts
t_minus = 0
while t_minus <= 5:
    username.wai_t(1)
    t_minus += 1
print("Start ---- >")


#start of main program loop
break_program = 1
def on_press(key):
    global break_program
    #print (key)
    if key == keyboard.Key.end:     #when END button is pressed it will stop
        print ('end pressed')
        break_program = 9999
        return False

with keyboard.Listener(on_press=on_press) as listener:
    while break_program <= do_times:
        do_stuff(break_program)
        break_program +=1
    sys.exit("Finished")
    
    listener.join()
