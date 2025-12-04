t1 = (10,20,30,10,20,30)
print(t1)

print(t1[2])
# t1[2] = 300
print(t1)

l1 = list(t1)
print(f"l1 is {l1} and the type of l1 is {type(l1)}")
l1[2] = 300
t1 = tuple(l1)
print(f"t1 is {t1} and the type of t1 is {type(t1)}")

t1 = tuple()
print(t1)

t2 = 1,2,3,4,5,6,7,8,9,10
print(f"t2 is {t2}, and the type is {type(t2)}")

t3 = (10)
print(f"t3 is {t3}, and the type is {type(t3)}")

t3 = (10, )
print(f"t3 is {t3}, and the type is {type(t3)}")

print(t2[-2])

print(t2[0:9:3])

l2 = list(t2)
print(l2[0:9:4])

t4 = (8,9,10,11,12,13,14,15)
t5 = t2 + t4
print(t5)

print(t5.count(8))

print(f"The index value of 15 in t5 is {t5.index(15)}")
print(f"The index value of 8 in t5 is {t5.index(8)}")

t6 = (101,102,103,(1,2,3,4,5),104,105)
print(f"t6 is {t6}, and at index 3  {t6[3]}")
print(f"t6 is {t6}, and at index 3 we have another tuple {t6[3]}")

# []
#               ()
# Change        Not
# append,       +, count, index
#

t7 =121,132,141,151,160,162,177
for value in t7:
    if value > 150:
        print(value)