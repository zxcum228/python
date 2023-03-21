def itc_min(min, min2):
    if min < min2:
        return min
    elif min > min2:
        return min2
    else:
        return False

a = int(input())
b = int(input())

print(itc_min(a,b))