try:
    number=input("please enter 3 numbers to compare together\n:").split()
    number.sort()
    print(number[-1])
except : print("please enter valid number and between them set a space")