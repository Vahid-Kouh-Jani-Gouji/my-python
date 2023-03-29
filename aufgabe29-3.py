try :
    input_txt_write=input("please enter a name for your text file : \n")
    data_txt=open(input_txt_write+".txt","w+")
    input_txt_list=input("now you can type in your file to finish please type \"end\":\n").split()
    line=1
    while True :
        data_me= input().split()
        if "end" in data_me : break
        input_txt_list+=data_me
        line +=1
    
    data_txt.write(str(input_txt_list))
    wort=len(input_txt_list)
    print("your file has %d worts and %d lines\n _____________________________________________________________________________\n"%(wort,line))
    data_txt.close()
    data=open(input_txt_write+".txt")
    print(data.readlines())
    data.close()
except : 
    print ("Some things go wrong")