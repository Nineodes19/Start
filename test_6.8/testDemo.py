# f = open(r'd:\\test.txt')
# line =f.readline()
# while line:
#     print(line,end=' ')
#     line = f.readline()
# f.close()

# f = open('d:\\test.txt')
# for line in iter(f):
#     print(line,end= ' ')
# f.close()

# f = open('d:\\test.txt')
# for line in f:
#     print(line,end=' ')
# f.close()

f = open('d:\\test.txt')
li = list(f)
print(li)