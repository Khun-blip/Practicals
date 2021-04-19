for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0,110,10):
    print(i, end=' ')
print()

for i in range(20,0,-1):
    print(i, end=' ')
print()

star=int(input("number of star :"))
for n in range(star):
    print(end='*')


num = int(input("number of row: "))
row=0
while row<num:
    star=row+1
    while star>0:
        print("*",end="")
        star = star-1
    row = row+1
    print()