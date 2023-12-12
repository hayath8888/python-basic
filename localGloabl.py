globalVariable ="i am global"

def functionOne():
    localVariable = "i am local"
    print(localVariable)
    print(globalVariable)

functionOne()

def functionTwo():
    globalVariable="global inside function"
    print(globalVariable)


print(globalVariable)
functionTwo()
print(globalVariable)

def functionThree():
    global globalVariable
    globalVariable ="I am new global"
    print(globalVariable)

print(globalVariable)
functionThree()
print(globalVariable)



