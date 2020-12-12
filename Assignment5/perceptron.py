d = [1, -1, 1]
o = [0, 0, 0]
print("DESIRED OUTPUT :")
print(d)
c = 1
print("c :"+str(c))
w = [1, -1, 0, 0.5]
x1 = [1, -2, 1.5, 0]
x2 = [1, -0.5, -2, -1.5]
x3 = [0, 1, -1, 1.5]

print("Weights :")
print(w)
print("x1 :")
print(x1)
print("x2 :")
print(x2)
print("x3 :")
print(x3)
print("------------------------")


def comp(d, o):
    for k in range(3):
        if(d[k] != o[k]):
            return 0
    return 1


def net(x, w):
    n = 0
    for i in range(4):
        n += x[i]*w[i]
    print("net :"+str(n))
    return n


def sgn(n):
    o1 = 0
    if(n > 0):
        o1 = 1
    if(n < 0):
        o1 = -1
    print("sgn(net) :"+str(o1))
    return o1


def wcal(w, c, d, o1, x):
    wnext = [0.0]*4
    # print("wnext test")
    # print(wnext)
    if(d == o1):
        for i in range(4):
            wnext[i] = w[i]
    else:
        mul = d-o1
        for i in range(4):
            wnext[i] = w[i]+(mul*x[i])
    print("w :")
    print(wnext)
    return wnext


flag = 0
count = 0
wnext = w
while(flag != 1):
    for i in range(3):
        if(i == 0):
            n = net(x1, wnext)
            o[0] = sgn(n)
            wnext = wcal(wnext, c, d[0], o[0], x1)
        if(i == 1):
            n = net(x2, wnext)
            o[1] = sgn(n)
            wnext = wcal(wnext, c, d[1], o[1], x2)
        if(i == 2):
            n = net(x3, wnext)
            o[2] = sgn(n)
            wnext = wcal(wnext, c, d[2], o[2], x3)
    count += 1
    print("Actual output :")
    print(o)
    flag = comp(d, o)
    print("Flag :" + str(comp(d, o)))
    print("epoch: "+str(count))
    print("-----------------------")
