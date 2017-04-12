# m = input("a number: ")
# n = input("a number: ")
#
# nm = n * m
# r = m % n
#
# if m < n:
#     t = m
#     m = n
#     n = t
#     r = m % n
# while r != 0:
#     m = n
#     n = r
#     r = m % n
# print "The greatest common divisor= ", n
# print "The least common multiple= ", nm / n


def divisor_multiple(m, n):
    nm = n * m
    r = m % n

    if m < n:
        t = m
        m = n
        n = t
        r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    print "The greatest common divisor= ", n
    print "The least common multiple= ", nm / n


divisor_multiple(5, 24)
