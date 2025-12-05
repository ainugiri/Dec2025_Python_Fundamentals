file = open("input.txt","r")
cont = file.read()
print(cont)

file = open("input1.txt","a")
file.write("Welcome to Python\n")
file.close()
