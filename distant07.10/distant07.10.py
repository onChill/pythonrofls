def even_or_odd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(even_or_odd(2))


def multiply(a, b):
    return a * b
    
print(multiply(4, 3))


def positive_sum(arr):
    
    positiveSum = 0
    
    for i in arr:
        if i >= 0:
            positiveSum += i
    return positiveSum
    
print(positive_sum([1, 2, -3, 7]))

def make_negative(number):
    if number > 0:
        number -= number * 2
    return number
print(make_negative(333))


def solution(string):
    return ''.join(reversed(string))
print(solution('abc'))
