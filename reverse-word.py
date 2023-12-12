word=str(input("enter the word :"))
rev=""
reverse=word[::-1]
print(reverse)

for i in range(len(word)-1,-1,-1):
    rev+=word[i]

print(rev)
  