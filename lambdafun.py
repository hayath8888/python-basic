def greet_person(name):
    return "hello ,"+name

greet = lambda name: "Hello ,"+name

print(greet_person("john"))
print(greet("jackie"))

is_adult =  lambda age : age>=18
print (is_adult(22))
print (is_adult(12))