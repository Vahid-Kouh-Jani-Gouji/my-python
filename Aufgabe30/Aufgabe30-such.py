def such(list,thing):
    if thing in list : return True
    return False
    
list=[]    
list=input("please enter efew things as members of a list to finish type \"end\" \n:").split()
while True :
    data=input().split()
    if "end" in data : break
    list+=data 

thing=input("now can you enter your search item \n :")
if such(list,thing) : print("HOOOra")