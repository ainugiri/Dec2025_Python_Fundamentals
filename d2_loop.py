# for loop
# for(int i=0; i<=n;i++){
#   ------
#   ======
# }

names = ["Giri ", "Prasad ","Samyuksha"]
for v in names:
    print(v)

for i in range(10):      #  0,1,2,3,4,5,6,7,8,9
    # print(i)
    print(f"{i+1} welcome")
for i in range(10,20):      #0,1,2,3,4
    # print(i)
    print(f"{i+1} welcome")


for i in range(10,21,2):      #0,1,2,3,4
    # print(i)
    print(f"{i} welcome")


# while 
count = 10
while count >= 0:
    count -=1
    if count == 5:
        continue
    print(f"{count} Break Time")
    if count == 2:
        break

for i in range(5):
    pass
print("Hello")