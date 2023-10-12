# 5 задач

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

def invert(lst):
    j = 0
    for i in lst:
        lst[j] = i * -1
        j += 1
    return lst

def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    else:
        return 'No'

def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return n * m
