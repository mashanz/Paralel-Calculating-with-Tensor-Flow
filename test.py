import waktuproses
d = 0.0
n = 0
c = 1.0
b = 2.0
a = (b + c) * (c + 2) * (b + c) * (c + 2)
while n < 999_999:
    d += a
    n += 1
print(d)
