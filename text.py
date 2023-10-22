file = open("example.txt", "r")

#lines = file.readlines()
# for line in lines:
#     #print(line.replace("\n",""))
#     print(line, end = "")
# print("\n", lines)

for line in file:
    print(line, end = "")
file.close()