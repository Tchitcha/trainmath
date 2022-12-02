# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:49:48 2021

@author: tchitcha / Fabien Lescot
"""

import random
import time
import datetime

def difficulty_is_valid(d):
    ret = False
    dn = -1
    if d.isnumeric():
        dn = int(d)
        if dn >=1 and dn <=4 :
            ret = True
    return ret

if __name__ == "__main__":
    replay = input("READY TO PLAY : (a)ddition, (s)ubstraction, (m)ultiplication, (l)eave ? ")
    difficulty = input("Which level of difficulty: 1,2,3,4 ? ")
    difficultyn = 0
    prefix = ""
    sign = ""
    f = lambda a,b : a+b


    while replay.lower() !="leave" and difficulty_is_valid(difficulty):
        replay = replay.lower()
        difficultyn = int(difficulty)

        if replay=="a":
            prefix = "Addition"
            sign = " + "
            f = lambda a,b : a+b
        elif replay=="s":
            prefix = "Substraction"
            sign = " - "
            f = lambda a,b : a-b
        elif replay=="m":
            prefix = "Multiplication"
            sign = " * "
            f = lambda a,b : a*b
        
        score = 0

        datetime_start = datetime.datetime.now()

        for i in range(20):
            if replay =="a":
                a = random.randrange(2,11 * difficultyn)
                b= random.randrange(2,11 * difficultyn)
            elif replay =="s":
                a = random.randrange(7, 20 * difficultyn)
                b = random.randrange(2, (a-1) * difficultyn)
            elif replay =="m":
                a = random.randrange(2,10 * difficultyn)
                b= random.randrange(2,10 * difficultyn)
            
            print(prefix, a, sign , b)
            
            entry = ""
            while not (entry.isdigit()):
                entry = input("= ? ")

            i = int(entry)
            
            if i == f(a,b):
                print("Good job")
                score+=1
            else:
                print("Wrong. ", a, sign, b, "= ", f(a,b))
                print()
            time.sleep(0.05)
        
        
        datetime_end = datetime.datetime.now()
        datetime_diff = (datetime_end - datetime_start).seconds
        print()
        print("Score = ", score, " out of 20.")
        print("Done in ", datetime_diff, " seconds")
        
        print()

        if score < 17 :
            print("You lose")
        elif score<20:
            print("You passed the test with ", score, )
        elif score ==20:
            print("Excellent, everything is perfect.")

        print("Show to your parents")
        replay = input("READY TO PLAY? (a)ddition, (s)ubstraction, (m)ultiplication, (l)eave ? ")
        difficulty = input("Which level of difficulty: 1,2,3,4 ? ")

    print("Good bye !")
