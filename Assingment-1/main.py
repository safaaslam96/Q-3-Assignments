# create a simple Hello World program in Python
print ("Hello World")


# Pycache Example
def greet(name):
    return f"Hello, {name}!"

print(greet("Safa"))

  #Variables in Python 
 #first variable i store integer value
a1 = 10

#second variable i store float value
b1 = 12.3

#third variable i store string value
c1 = "Happy Summer"
 # I have create a new variable ans and store the sum of a1 and b1 in it
ans = a1+b1
#print means to show the output
print(ans)

# now im creating ans2 variable and store the sum of a1 and c1 in it
ans2 = a1*c1
print(ans2)
# after print the output of ans2 i got an error because we can't add integer and string together
#  now i will multiply a1 and c1, after multiply i will get the output of a1 10 times 


# boolean
is_student = True

# list
grades = [65, 50, 85, 87, 90]

# tuple
coordinates = (3, 5)

# dictionary
person = {"name": "Safa", "age": 21, "height": 5.7}

# set
unique_numbers = {1, 2, 3, 4, 5}


print( is_student, grades, coordinates, person, unique_numbers)