filename = 'programing.txt'

with open(filename,'r+') as file_object:
    file_object.write("I love comic books.\n")
    file_object.write("I love games.\n")
    lines = file_object.readlines()
    #print(lines)


for line in lines:
    print(line.rstrip())

