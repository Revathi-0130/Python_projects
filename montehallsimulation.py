# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:30:27 2023

@author: pochi
"""
import random
choice = "y"
swap = 0
no_swap = 0
while(choice == "y"):
    doors = [0]*3
    empty_doors = [0]*2
    x = random.randint(0,2)
    doors[x] = "prize"

    for i in range(0,3):
        if(i == x):
            continue
        else:
            doors[i] = "empty"
            empty_doors.append(i)
    
    user_choice = int(input("Please choose a door(0 or 1 or 2): "))
    
    open_door = random.choice(empty_doors)
    
    while(open_door == user_choice):
        open_door = random.choice(empty_doors)
    
    option = input("Do you want to swap y/n? ")
    
    if(option == "y"):
        if(doors[user_choice] == "empty"):
            print("player wins")
            swap += 1
        else:
            print("player lost")
    else:
        if(doors[user_choice] == "empty"):
            print("player lost")
        else:
            print("player wins")
            no_swap += 1
    
    choice = input("Do you want to continue?(y/n) ")
    
print(swap)
print(no_swap)
    
   
            
        