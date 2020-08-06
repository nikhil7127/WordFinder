from randomSelect import *
def Trails():
    while(1):
        try:
            trail = int(input("Enter Number Of trails[5-25]: "))
            if(trail<5 or trail>25):
                print("Trails must be in between 5 and 25")
        except:
            print("enter valid number")
            continue
        if(trail>4 and trail<26):
            break
    return trail
def checkingTime():
    a1 = Trails()
    global a2
    a2 = RandomSelect()
    for afk in a2:
        print("*",end="")
    lists=[]
    old=[]
    for a in range(0,len(a2)):
        old.append(a)
    new=[]
    print("")
    while(a1!=0):
        i=0
        lists=[]
        while(1):
            enter = input("enter character : ")
            if(len(enter) ==1):
                break
        for a in a2:
            lists.append(a==enter)
        final=[]
        for i2,k in enumerate(lists):
            if i2 in old:
                if(k):
                    new.append(i2)
                    old.remove(i2)
                    final.append(enter)
                    i=1
                    continue
                else:
                    final.append("*")
            if i2 in new:
                final.append(a2[i2])
        if(i!=1):
            a1-=1
        print("word: ")
        for k23 in final:
            print(k23,end=" ")
        print(" ")
        print(f"attemts remaining: {a1}")
        
        if "*" not in final:
            break
    print(f"ANSWER : {a2}")
checkingTime()
while(1):
    play = input("Do You Want To Play Again(Y/N): ")
    if(play == "Y" or play == "y"):
       checkingTime()
    if(play == "N" or play == "n"):
       break
    else:
        print("enter valid choice")
