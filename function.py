def greet():
    print("Hello")

def greetPerson(name):
    print(f"hello {name},how are you?")

def make_coffee(water,coffee_bean,milk):
    print(f"make cofee with {water}ml of water,{coffee_bean}g of coffee bean ,{milk}ml of milk")

def happyBirthday(name="guest",age=0):
    print(f"Happy birthday {name}!, you are now {age}.")

happyBirthday("Hayath",22)
happyBirthday(age=40)
make_coffee(30,2,50)

def compare_age(name1,age1,name2,age2):
    if age1>age2:
        print(f"{name1} is older than {name2}")
    elif age1==age2:
        print(f"both {name1},{name2} have equal age")
    else:
        print(f"{name2} is older than {name1}")

compare_age("hayath",2,"safreen",22)

def nextValue(number):
    return number+1

print(nextValue(5))

def years_until_100(age):
    if age<100:
        return 100-age
    
    return 100-age

print(years_until_100(22))
print(years_until_100(104))

def factorial(n):
    if n<=1:
        return 1
    
    return n * factorial(n-1)

print(factorial(3))