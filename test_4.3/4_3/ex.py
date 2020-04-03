print("所有三位数的素数如下：",end=" ")

for i in range(100,1000):
    j = 2
    flag = 1
    while j < i:
        if i % j == 0:
            flag = 0
            break
    j += 1
    if flag == 1:
        print(i,end=" ")