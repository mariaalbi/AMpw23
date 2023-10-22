# file = open("example.txt", "r")
#
# #lines = file.readlines()
# # for line in lines:
# #     #print(line.replace("\n",""))
# #     print(line, end = "")
# # print("\n", lines)
#
# for line in file:
#     print(line, end = "")
# file.close()

def file_lines(filepath):
    with open(filepath) as file:
        for line in file:
            yield line

for line in file_lines("example.txt"):
    print(line)

