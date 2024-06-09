print(10==10)
print((10==10)== False)

print((10 != 9) == True)
print((10 == 9) == False)

print(10 == 10 and 10 > 11)
print(10 > 5 or 10 < 5)


print(10 + 10)
print(10 - 10)
print(10/5)
print(10//5)

print("------")

x = 10
x = x + 10
x += 10
print(x)

print("-----")

x = 20
x -= 10

print(x)

y = 100
y //= 10

Z = 30
Z *= 2

print(y)
print(Z)


x = 13

print(bin(x >> 1)[2:].rjust(4,("0")))
