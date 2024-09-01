import numpy as np


checkboard = np.arange(1,10,dtype=object).reshape(3,3)


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
    checkboard = np.arange(1,10,dtype=object).reshape(3,3)
    checkboard = swap(10)
    random_space_row = np.random.randint(3)
    random_space_column = np.random.randint(3)
    random_space = checkboard[random_space_row,random_space_column]
    checkboard[random_space_row,random_space_column] = '?'
    print(checkboard)
    check_ans = True
    while check_ans:
        user_ans = int(input("Number:"))
        if user_ans == random_space:
            print("Correct!")
            check_ans = False
            check_continue()
        else:
            print("Try again")
            continue

        

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

game_start()