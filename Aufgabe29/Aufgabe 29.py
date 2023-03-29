import random
x=random.randint(1,10)
i=1
print(x)
try :

    while True :
        x_input=int(input("please enter a number between 1 to 10 :\n"))
        if x==x_input : 
            print (" HOOOORA , At the %d time you won :-)"%(i)) 
            break
        elif x<x_input :
            print ("that is %d once : your number is higher than the right number , come lower :-)"%(i)) 
            i=i+1
        elif x>x_input : 
            print ("that is %d once : your number is lower than the right number , come higher :-)"%(i))
            i=i+1
except:
    print("you gave any number out of range or invalid number , please try a gain ")    