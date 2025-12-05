# access modifier returntype function(argument){
# 
# 
# }

# def functionname(parameters):
#   --------
#   --------
#   --------
#   --------
#  return value

def areaC(rad):
    return 22*rad*rad/7

def welcome(username="Guest"):
    print(f"{username}, Welcome to Python Programming")

# welcome("Giri")
# welcome("Steve")
# welcome("Rose")
# welcome("Mohammed")
# welcome("Elizabeth")




def total(*numbers):
    print(sum(numbers))

# areaofTri =
# def areaofTri(b,h):
#     return 0.5*b*h
areaofTri = lambda b,h : 0.5*b*h