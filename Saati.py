import math
n = int(input(print("сколько критериев в системе?")))
if n > 10:
    print("10 - предел.")
    exit()
elif n <= 0:
    print("10 - предел, 0 не подойдет.")
    exit()
else:
    pass
#проверка на целое число


#идентификация коэффициентов





#цикл с запросом ввода критериев критериев
a0 = 1
a1 = float(input(print("k1/k2")))
a2 = float(input(print("k1/k3")))
a3 = float(input(print("k1/k4")))


b0 = 1
b1 = 1/a1
b2 = float(input(print("k2/k3")))
b3 = float(input(print("k2/k4")))


c0 = 1
c1 = 1/b2
c2 = 1/a2
c3 = float(input(print("k3/k4")))


d0 = 1
d1 = 1/a3
d2 = 1/b3
d3 = 1/c3


Sa = (a1*a2*a3*a0)
Sb = (b1*b2*b3*b0)
Sc = (c1*c2*c3*c0)
Sd = (d1*d2*d3*d0)

Ma = Sa ** (1./4)
Mb = Sb ** (1./4)
Mc = Sc ** (1./4)
Md = Sd ** (1./4)

sx = (Ma+Mb+Mc+Md)

CFa = Ma/sx
CFb = Mb/sx
CFc = Mc/sx
CFd = Md/sx

print (f" {CFa:.2f}")
print (f" {CFb:.2f}")
print (f" {CFc:.2f}")
print (f" {CFd:.2f}")