def itc_max(num, num2):
    if num > num2:
        return num
    elif num < num2:
        return num2
    else:
        return False

a = int(input())
b = int(input())

print(itc_max(a,b))