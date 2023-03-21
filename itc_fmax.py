def itc_fmax(num, num2):
    if num > num2:
        return num
    elif num < num2:
        return num2
    else:
        return False

a = float(input())
b = float(input())

print(itc_fmax(a,b))