def itc_fmin(min, min2):
    if min < min2:
        return min
    elif min > min2:
        return min2
    else:
        return False

a = float(input())
b = float(input())

print(itc_fmin(a,b))