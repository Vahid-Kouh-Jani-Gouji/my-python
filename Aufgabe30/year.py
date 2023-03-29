import csv
def leap_year (file_year="leaputf.csv"):
    data=open(file_year,"r")
    year=csv.reader(data,delimiter=";")
    allyears=[]
    for leap in year : allyears+=leap
    data.close()
    return(allyears)

allyears=leap_year()

year_user=input("please enter a year \n  :")
if year_user in allyears : print("this year => %s is a leap year" %(year_user))
else : print("NO that is not a leap year")





# Überprüfe, ob ein vom Benutzer eingegebenes Jahr ein Schaltjahr ist. Folgende Regeln gelten für ein Schaltjahr:
# nicht durch 4 teilbar - kein Schaltjahr
# durch 4 teilbar - Schaltjahr
# durch 100 teilbar - kein Schaltjahr
# durch 400 teilbar - Schaltjahr

# Teste dein Programm mit den Jahren 1900 (Nein), 2000 (Ja), 2004 (Ja) und 2006 (Nein)


