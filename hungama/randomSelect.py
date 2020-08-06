from tkinter import *
import random as r
from tkinter import font
def RandomSelect():
    while(1):
        try:
            a = int(input('Enter Length Word [4-10]: '))
        except:
            print("must be integer")
        if(a>3 and a<11):
            break
    WantWords =[]
    with open("random_word.txt","r") as rs:
        words = rs.read()
        ListOfWords = words.split("\n")
        for k in ListOfWords:
            if(len(k)==a):
                WantWords.append(k)
        guess = r.randint(0,len(WantWords)-1)
    return WantWords[guess]
 
   
if __name__ == "__main__":
    print(RandomSelect())
    

