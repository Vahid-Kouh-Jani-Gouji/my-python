import datetime
import time
oster_ferien = datetime.datetime(2023, 4, 11)
while True:
    now = datetime.datetime.now()
    divid = oster_ferien - now
    second = divid.total_seconds()
    days = int(second // (3600 * 24))
    hours = int(second // 3600 % 24)
    minutes = int(second // 60 % 60)
    seconds = int(second % 60)

    print(f"only to (11.04.23): {days} Tage, {hours} Stunden, {minutes} Minuten, {seconds} Sekunden")
    time.sleep(1)
    if now > oster_ferien:
        print("Hooora now is time to party :)!")
        break
    

