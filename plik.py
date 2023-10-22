with open("hello.txt", "r+") as file:
    #print(file.tell())
    file.seek(2)
    #print(file.tell())
    file.write("!!!")