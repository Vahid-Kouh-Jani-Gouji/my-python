
zahlen_list = []
while True:
    data = input ("\nGib die Datei ein oder drücke '.', um die Eingabe zu beenden: ")
    if data == ".":
         break
       
    zahlen_list+= [data]


zahlen_list.sort()
print("Sortierte Liste:", zahlen_list)

