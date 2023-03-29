file = input("Textdatei angeben: ")
with open(file, "r") as f:
	while True:
            line = f.readline()
            if line == "":break
            print(line.swapcase(), end="")