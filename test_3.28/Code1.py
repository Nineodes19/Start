
s = eval('2+4/5')
print(s)
s = 'a\nb\tc'
print(len(s))
print(2!=5 or 0)
print(1234%1000//100)
x = 2
x
print(x)
x = 10
y = 20
z = 30
if x < y:
    z = x
    x = y
    y = z
print(x,y,z)

a = 1
b =3
c = 5
d = 4
if a < b:
    if c < d:
        x = 1
    elif a < c:
        if b < d:
            x = 2
        else:
            x = 3
    else:
        x = 6
else:
    x = 7
print(x)

a,x,y,ok1,ok2= 100,10,20,5,0
if x < y:
    if y != 10:
        if not ok1:
            a = 1
        elif ok2:
            a = 10
a = -1
print(a)