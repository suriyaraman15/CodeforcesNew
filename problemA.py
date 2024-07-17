for _ in range(int(input())):
    a, b, c = [int(x) for x in input().split()]
    for i in range(5):
        if (a > b and a > c):
            if (b > c):
                c = c + 1
            else:
                b = b + 1
        elif (b > c):
            if (a > c):
                c = c + 1
            else:
                a = a + 1
        else:
            if (a > b):
                b = b + 1
            else:
                a = a + 1
    print(a * b * c)
