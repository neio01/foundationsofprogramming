name = "Neio"
age = 18
Location = "kathamandu"
print(f"Name: {name}, Age: {age}, Location: {Location}") 
print("Name:" + name + ", Age:" + str(age) + ", Location:" + Location)
print("Name: {}, Age: {}, Location: {}".format(name, age, Location))
print("Name: %s, Age: %d, Location: %s" % (name, age, Location))

name1 = input("Enter your name: ") 
age1 = int(input("Enter your age: "))
print(f"Name: {name1}, Age: {age1}")

print(type(name1))
print(type(age1)) 
print (6 or 5)