# Author: CCG 3/7/2022

def r_max(nestedlst):
    max = 0
    for num in nestedlst:
        if type(num) == list:
            num = r_max(num)
            if num > max:
                max = num
        else:
            if num > max:
                max = num
    return max

print(r_max([0,2,2,[23,60],24]))