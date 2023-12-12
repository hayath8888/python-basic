for i in range(10):
    if i==4:
        continue
    if i==8:
        break
    print("number",i)

def usingloop(n):
    result=1
    for i in range(1,n+1):
        result*=i

    return result

print(usingloop(5))


    