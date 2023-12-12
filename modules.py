# import math
# print(math.sqrt(16))

# import math as m

# print(m.sqrt(25))
# print(m.sqrt(48))

# from math import sqrt,pi
# n=56
# print(f"square root of {n} is:",sqrt(n),"\npi value is:",pi)

# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)

from lambdafun import is_adult

print("this is mudules file")
age=int(input("enter your age : "))
if is_adult(age):
    print("you are an adult")
else:
    print("you are not an adult")    