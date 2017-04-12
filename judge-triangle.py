import math

a = input("please input a: ")
b = input("please input b: ")
c = input("please input c: ")

if a > b:
    t = a
    a = b
    b = t
if a > c:
    t = a
    a = c
    c = t
if b > c:
    t = b
    b = c
    c = t
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print """triangle's area is """, area
    if a == b and a == c:
        print "triangle is Equilateral"
    elif a == b or a == c or b == c:
        print "triangle is isosceles"
    elif a * a + b * b == c * c:
        print "triangle is right-angled"
    else:
        print "triangle is normal"
else:
    print "No triangle"
