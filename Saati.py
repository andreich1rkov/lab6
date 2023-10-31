import math
n = input(print("сколько критериев в системе?"))
#проверка на целое число


#идентификация коэффициентов
k1, k2, k3, k4 = 0




#цикл с запросом ввода критериев критериев
a0 = 1
a1 = input(print("k1/k2"))
a2 = input(print("k1/k3"))
a3 = input(print("k1/k4"))


b0 = 1
b1 = input(print("k2/k1")) # 1/a1
b2 = input(print("k2/k3"))
b3 = input(print("k2/k4"))


c0 = 1
c1 = input(print("k3/k1")) # 1/b2
c2 = input(print("k3/k2")) # 1/a2
c3 = input(print("k3/k4"))


d0 = 1
d1 = input(print("k4/k1")) # 1/a3
d2 = input(print("k4/k2")) # 1/b3
d3 = input(print("k4/k3")) # 1/c3


Sa = math.prod(a1,a2,a3,a0)
Sb = math.prod(b1,b2,b3,b0)
Sc = math.prod(c1,c2,c3,c0)
Sd = math.prod(d1,d2,d3,d0)

Ma = Sa ** (1./4)
Mb = Sb ** (1./4)
Mc = Sc ** (1./4)
Md = Sd ** (1./4)

sx = sum(Ma,Mb,Mc,Md)

CFa = Ma/sx
CFb = Mb/sx
CFc = Mc/sx
CFd = Md/sx

print (f"dfff {CFa:.2f}")
print (f"dfff {CFb:.2f}")
print (f"dfff {CFc:.2f}")
print (f"dfff {CFd:.2f}")