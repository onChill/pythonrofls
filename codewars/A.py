# 15 задач

def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i * i
    return sum
    
def greet(name):
    return "Hello, " + name + " how are you doing today?"

def remove_char(s):
    return s[1:-1]

def opposite(number):
    return number * -1

def smash(words):
    s = ''
    for i in words:
        s += i + ' '
    return s.strip()

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 == 1 or flower2 % 2 == 0 and flower1 % 2 == 1:
        return True
    else:
        return False

def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    return False

def string_to_array(s):
    return s.split(' ')

def reverse_seq(n):
    arr = []
    for i in range(n, 0, -1):
        arr.append(i)
    return arr

def are_you_playing_banjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
