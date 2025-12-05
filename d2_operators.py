# operators

# arithmetic ( addition, sub, mul, div, mod, floor)
a = 1121
b = 17
print(f"Addition {a+b}")
print(f"Sub {a-b}")
print(f"mul {a*b}")
print(f"div {a/b}")
print(f"remainder {a%b}")
print(f"floor dev {a//b}")
print(f"2 to the power of 6 {2**6}")


# comparison operator = val1 with val2 => True | False
print(a < 1500)
print(a > 1500)
print(a <= 1500)
print(a >= 1500)
print(a == 1121)
print(a != b)

# logical operator (con1  con2 )
# and | or | not
# truth table

# cond1     cond2       and     or      not(cond1)
# true      true        true    true    false
# true      false       false   true    false
# false     true        false   true    true
# false     false       false   false   true

print(f" {a < 1500} and {b > 10} is {a < 1500 and b > 10}")
print(f" {a < 1500} and {b < 10} is {a < 1500 and b < 10}")
print(f" {a > 1500} and {b > 10} is {a > 1500 and b > 10}")
print(f" {a > 1500} and {b < 10} is {a > 1500 and b < 10}")



print(f" {a < 1500} or {b > 10} is {a < 1500 or b > 10}")
print(f" {a < 1500} or {b < 10} is {a < 1500 or b < 10}")
print(f" {a > 1500} or {b > 10} is {a > 1500 or b > 10}")
print(f" {a > 1500} or {b < 10} is {a > 1500 or b < 10}")



# assignment
x = 10
x += 5 # x = x + 5
print(x)
x += 5 # x = x + 5
print(x)
x -= 5 # x = x + 5
print(x)
x *= 5 # x = x + 5
print(x)
x /= 5 # x = x + 5
print(x)

l1 = [121,12131,131,141,1212]
print(f"121 in {l1} : {121 in l1}")
print(f"1210 in {l1} : {1210 in l1}")
print(f"1205 not in {l1} : {1205 not in l1}")
print(f"121 not in {l1} : {121 not in l1}")

print(a)

x = 1120
x +=1

print(f"{a} == {x} is {a==x}")
print(f"{a} is same {x} is {a is x}")