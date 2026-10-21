data = True
with open("simple.txt","r") as f:
    while data:
        data =f.readline()
        if ("WORLD" in data):
            print("Word Found")
            print(data)

         