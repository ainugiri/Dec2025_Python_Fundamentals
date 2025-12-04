# include all library
# printf    -   stdio

print("Welcome to python")
x = 10
y = x/2
z = 'Giri Prasad P'
b1 = x < y
print(b1)

# list -> []
# tuple -> ()
# set -> {}
# dict
purchase_items = ['apple', 'banana', 'pen', 'apple','pen','banana','repeat']
# list
#  maintain order / access - index / modify 
print(purchase_items)
print(type(purchase_items))

print(purchase_items[2])
purchase_items[2] = 'Pencil'
print(purchase_items)

# create
l1 = list()
print(f"l1 is {l1}, the type of l1 is {type(l1)}")

l1.append(1)
print(f"l1 is {l1}, the type of l1 is {type(l1)}")

l1.append(2)
print(f"l1 is {l1}, the type of l1 is {type(l1)}")

l1.append(4)
print(f"l1 is {l1}, the type of l1 is {type(l1)}")

l1.insert(2,3)
print(f"l1 is {l1}, the type of l1 is {type(l1)}")

l1.extend([5,6])
print(f"l1 is {l1}, the type of l1 is {type(l1)}")

l2 = [11,12,13]
l1.extend(l2)
print(f"l1 is {l1}, the type of l1 is {type(l1)}")

l1.remove(11)
print(f"l1 is {l1}, the type of l1 is {type(l1)}")

l1.pop()
print(f"l1 is {l1}, the type of l1 is {type(l1)}")

l1.pop()
print(f"l1 is {l1}, the type of l1 is {type(l1)}")


print(f"l1 is {l1}, the type of l1 is {type(l1)}")

l1.clear()
print(f"l1 is {l1}, the type of l1 is {type(l1)}")
l1 = [12,11,123,141,21,12,11,1412,123,21,141,1201]
print(l1)
l1.remove(11)
print(l1)
print(l1[6])
l1.sort(reverse=True)
print(l1)
print(l1[6])

print(f"In the list 21 is occured {l1.count(21)} times")

v = 123
while v in l1:
    l1.remove(v)

print(l1)

# list
#  duplicates allowed
#  ordered
#  index
#  add / modify / remove
#  sort
#  insert / append / extend
l1.pop(2)
print(l1)