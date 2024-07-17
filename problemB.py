for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]

    count = 0
    listCasserole = [int(x) for x in input().split()]
    listCasserole.remove(max(listCasserole))

    for i in listCasserole:
        if(i > 1):
            count += (i -1)
        count += i
    print(count)





