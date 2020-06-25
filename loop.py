A = [0, 1, 2, 3, 4, 5]  # List
B = (0, 1, 2, 3, 4, 5)  # tuple
C = {0, 1, 2, 3, 4, 5}  # set
D = 'Dilip'  # string
E = {
    "name": 'Dilip',
    "age": 38
} # Dictionary

print(2 in A)
print("D" in D)
print("b" in D)

for i in A:
    print(i)

for i in E:
    print(i)


for x,y in E.items():
    print(x, " ", y)


a = [0, 1, 2, 3, 4, 5]

for x in a:
    if x ==2:
        break
    print(x)

print("___________________")

x=0
while x<5:
    if x ==3:
        break
    print(x)
    x+=1


print("###################")

for x in a:
    if x ==2:
        continue
    print(x)
print("###################")
x=0
while x<5:
    x += 1
    if x ==3:
        continue
    print(x)


