imadd_4 = lambda x : x + 4
print(add_4(4))

add = lambda x, y: x + y
print(add(4, 6))

def addf(x, y):
    return x + y

print(addf(6, 4))

print((lambda x, y: x + y) (10, 6))


Is_even = lambda x : x % 2 == 0

print(Is_even(2))
print(Is_even(3))


Blocks = lambda x, y: [x[i:i+y] for i in range(0, len(x), y)]

print(Blocks('string', 2))


To_ord  = lambda x : [ord(i) for i in x]

print(To_ord('ABCD'))


def ord_2(x):
    ret = []
    for I in x:
        ret.append(ord(I))
    return ret

ord_2('ABCD')
 
