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


def times_table():
    for i in range(1, 10):
        for j in range(1, i + 1, 1):
            print i, "*", j, "=", i * j,
        print


print 'times_table ', times_table()


def factorial(num):
    sum = 0
    for i in range(1, num + 1):
        s = 1
        for j in range(1, i + 1):
            s = j * s
        sum += s
    print sum


print 'factorial(3) is: ', factorial(3)


def star_column(n):
    for i in range(1, n + 1):
        for j in range(0, 2 * i - 1):
            print "*",
        print


star_column(6)


def star_column2(n):
    for i in range(1, n + 1):
        for j in range(0, n - i):
            print " ",
        for k in range(0, 2 * i - 1):
            print "*",
        print


star_column2(5)


def star3(n):
    for i in range(1, n + 1):
        for j in range(0, i - 1):
            print " ",
        for k in range(0, 2 * (n - i) + 1):
            print "*",
        print


print 'star3: '
print star3(5)


def star4(n):
    for i in range(1, 2 * n):
        if i <= n:
            for j in range(0, i):
                print "*",
            print
        else:
            for k in range(0, 2 * n - i):
                print "*",
            print


print 'star4'
print star4(4)


def star5(n):
    for i in range(1, n + 1):
        for j in range(0, 3 * n - i - 1):
            print " ",
        for k in range(0, 2 * i - 1):
            print "*",
        print

    for i in range(n, 2 * n):
        for j in range(0, 2 * n + 2 - i):
            print " ",
        for k in range(0, 2 * i - 1):
            print "*",
        print

    for i in range(1, 2 * n):
        for j in range(0, 2 * n):
            print " ",
        for k in range(0, n):
            print "*",
        print


star5(3)

print '''     *
            * * *
          * * * * *
          * * * * *
        * * * * * * *
      * * * * * * * * *
            * * *
            * * *
            * * *
            * * *
            * * *'''