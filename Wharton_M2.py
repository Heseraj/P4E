# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 12:17:21 2020

@author: HeSer
"""

your_score = int(input("Enter you Score "))
if your_score > 100 or your_score < 0:
    print("sorry! This can't be your socre, try again")
    your_score = int(input("Enter your correct Score "))
    if your_score > 100 or your_score < 0:
        print("again, sorry, this can't be your number -:(")
        your_score = int(input("Please, Please enter your correct Score on last time! "))
        if your_score >= 90:
            print("Finally, A")
        elif your_score >= 80:
            print("B")
        elif your_score >= 70:
            print("C")
        elif your_score >= 60:
            print("D")
        elif your_score > 100 or your_score < 0:
            print("You need to go to the registrat Office to sort your issue out")
        else: 
            print("Unfortunately, You need to repeat the class !")
    elif your_score >= 90:
        print("Congratulation you got A for the class")
    elif your_score >= 80:
        print("your got B for the class")
    elif your_score >= 70: 
        print("You got C for the class")
    elif your_score >= 60: 
        print("you got D for the class")
    else:
        print("You need to repeat the class")
elif your_score >= 90:
    print("Congratulation you got A for the class")
elif your_score >= 80:
    print("your got B for the class")
elif your_score >= 70: 
    print("You got C for the class")
elif your_score >= 60: 
    print("you got D for the class")
else: 
    print("you need to repeat the class")
    
    
    