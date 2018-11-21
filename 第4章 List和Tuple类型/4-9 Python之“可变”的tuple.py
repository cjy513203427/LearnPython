t1 = ('a', 'b', ('A', 'B'))
print t1
t2 = ('a', 'b', ['A', 'B'])
L = t2[2]
L[0] = 'X'
L[1] = 'Y'
print t2