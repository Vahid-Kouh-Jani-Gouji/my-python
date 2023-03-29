ja="ja"
nein="nein"
antwort=input("\n Bitte folge die Frage und antworte nur mit ja/nain \n Funktioniert das System \n: ")
if antwort == ja : print("\n Fummel nicht daran herum \n Alles ist gut")
elif antwort==nein: 
    antwort=input("\n Bist du Schuld ? ")
    if antwort==nein : print("\n Du triffst es nicht")
    elif antwort==ja : 
        antwort=input(" Du Idiot ,\n hat es jemand gemerkt ?")
        if antwort==nein : print("\n Man wird dich nie finden")
        elif antwort==ja :
            antwort=input("\n Du bist am Arsch \n Kannst du einem Anderen die Schuld zuschieben ?")
            if antwort==nein : print("\n Du bist wirklich im Arsch")
            elif antwort==ja : print("Keine Sorge , jemand anderes ist im Arsch")