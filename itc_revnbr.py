def itc_revnbr(num):
    a = num % 10
    b = (num % 100) // 10
    c = num // 100
    print(a,b,c)


num = int(input())
itc_revnbr(num)
