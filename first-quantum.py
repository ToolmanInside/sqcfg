from z3 import *

k1 = Int('k1')
a = ((1,k1),(3,4))
b = ((1,1),(1,1))
c = ((3,3),(7,7))

s = Solver()
eq1 = a[0][1]>0
eq2 = [[sum(a[i][k]*b[k][j] for k in range(2)) == c[i][j] for i in range(2)] for j in range(2)]
s.add(eq1)
s.add(eq2[0][0])
s.add(eq2[0][1])
s.add(eq2[1][0])
s.add(eq2[1][1])

i = 3
if i > 2:
    print(1)

print(s)
print(s.check())
m = s.model()
print(m)