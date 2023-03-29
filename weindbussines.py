
weinprise = {"rotwein_preis" : 12.99, "rosewein_preis" : 9.98 , "weisswein_preis" : 11.99}


anzahl_rotwein = int(input("\nAnzahl Rotwein: "))
anzahl_rosewein = int(input("\nAnzahl Rosewein: "))
anzahl_weisswein = int(input("\nAnzahl Weißwein: "))


gesamtkosten = (anzahl_rotwein * weinprise['rotwein_preis']) + (anzahl_rosewein * weinprise['rosewein_preis']) + (anzahl_weisswein * weinprise['weisswein_preis'])


print("\nDie Gesamtkosten betragen:", gesamtkosten, "Euro")
