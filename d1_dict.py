A825662 = {
    "Name" : "Giri Prasad P",
    "Age"  : 41,
    "email" : "giri-prasad.p@atos.net",
    "city" : "Chennai, IN"
}
print(A825662.keys())
print(f" Name of A825662 is {A825662["Name"]} and his age is {A825662["Age"]} from {A825662["city"]}")


print(A825662.values())

A825662.pop("email")
print(A825662.keys())
print(A825662.values())

A825662.popitem()
print(A825662.keys())
print(A825662.values())


emp = {
    "a1" : {"name": "Giri Prasad", "age":41, "city":"Chennai"},
    "a2" : {"name": "Hari Prasad", "age":40, "city":"Chennai"},
    "a3" : {"name": "Sakthi", "age":41, "city":"Chennai"},   
    "a4" : {"name": "Ramya", "age":30, "city":"Delhi"},    
    "a4" : {"name": "Pricy", "age":30, "city":"Delhi"},    
    "a4" : {"name": "Ramya", "age":30, "city":"Delhi"},    
    "a4" : {"name": "Rohin", "age":20, "city":"Delhi"},    
    "a4" : {"name": "Joy", "age":33, "city":"New York","name":"Rajan"},   
}

print(emp["a3"]["name"])
print(emp["a4"]["name"])