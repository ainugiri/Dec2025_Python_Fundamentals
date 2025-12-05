# if
# if else
# if elif else
# nested if


# inp1 = input("Enter a value : ")
# print(f"inp1 is {inp1} and the datatype of inp1 is {type(inp1)}")

# inp1 = int(inp1)
# print(f"inp1 is {inp1} and the datatype of inp1 is {type(inp1)}")

inp1 = int(input("Enter a value : "))
print(f"inp1 is {inp1} and the datatype of inp1 is {type(inp1)}")

if(inp1 < 500):
    print("Worst")
elif (inp1 < 1000):
    print("Failed")
else:
    print("Pass")
if inp1 > 0:
    if inp1 % 2 == 0:
        print("postive even number")
    else:
        print("positive odd number")
else: 
    if inp1 % 2 == 0:
        print("negative even number")
    else:
        print("negative odd number")


