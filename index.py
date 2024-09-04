import numpy as np
import time 
import threading

mode = 0
checkboard = np.arange(1,10,dtype=object).reshape(3,3)

def choose_difficulty():
    global mode
    user_difficulty = str(input("Choose your difficulty (Easy,Medium,Hard)"))
    if user_difficulty.capitalize() == "Easy":
        mode = 20
    elif user_difficulty.capitalize() == "Medium":
        mode = 15
    elif user_difficulty.capitalize() == "Hard":
        mode = 7
    else:
        print("Please select an approriate difficulty")
        choose_difficulty()


def countdown():
    global mode

    for i in range(mode):
        mode -= 1
        time.sleep(1)
        

    print("Out of time!")


def swap(shuffles):
    checkboard = np.arange(1,10,dtype=object).reshape(3,3)
    for i in range(shuffles):
        old_row = np.random.randint(3)
        old_column = np.random.randint(3)
        new_row = np.random.randint(3)
        new_column = np.random.randint(3)
        checkboard[old_row,old_column], checkboard[new_row,new_column] = checkboard[new_row,new_column], checkboard[old_row,old_column]
    return checkboard

def game_start():
    global mode
    checkboard = np.arange(1,10,dtype=object).reshape(3,3)
    checkboard = swap(10)
    random_space_row = np.random.randint(3)
    random_space_column = np.random.randint(3)
    random_space = checkboard[random_space_row,random_space_column]
    checkboard[random_space_row,random_space_column] = '?'
    print(checkboard)
    while mode >0:
        print(str(mode) + "s")
        user_ans = int(input("Number:"))
        if user_ans == random_space:
            print("Correct!")
            check_continue()
        else:
            print("Try again")
            continue


        if mode == 0:
            break
        
        

def check_continue():
    user_ans = input("Do you want to continue?")
    if user_ans.capitalize() == "Yes":
        swap(10)
        game_start()
    elif user_ans.capitalize() == "No":
        pass
    else:
        print("Please key in yes or no")
        check_continue()




choose_difficulty()

countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()
game_start()