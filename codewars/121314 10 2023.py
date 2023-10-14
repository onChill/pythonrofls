# 30 задач

def make_upper_case(strng):
    return strng.upper()

def check_for_factor(base, factor):
    return base % factor == 0

def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product

def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    if human_years < 2:
        catYears = human_years * 15
        dogYears = catYears
    elif human_years < 3:
        catYears = 15 + 9
        dogYears = catYears
    else:
        catYears = ((human_years -2) * 4) + 24
        dogYears = ((human_years -2) * 5) + 24
    return [human_years, catYears, dogYears]

def twice_as_old(dad, son):
    return abs(dad - 2 * son)

def count_sheeps(sheep):
    return sheep.count(True)

def goals(laLiga, copaDelRey, championsLeague):
    return sum(laLiga, copaDelRey, championsLeague)

def basic_op(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2

  
def maps(a):
    num = []
    for i in a:
        num.append(i * 2)
    return num


def switch_it_up(n):
    match n:
        case 0:return'Zero'
        case 1:return'One'
        case 2:return'Two'
        case 3:return'Three'
        case 4:return'Four'
        case 5:return'Five'
        case 6:return'Six'
        case 7:return'Seven'
        case 8:return'Eight'
        case 9:return'Nine'


def past(h, m, s):
    return 3600000 * h + 60000 * m + 1000 * s

def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

def str_count(strng, letter):
    counter = 0
    for chr in strng:
        if chr == letter:
            counter += 1
    return counter


def sum_str(a,b):
  a = int(a) if a else 0
  b = int(b) if b else 0
  return str(a+b)

def count_sheep(n):
    s = ""
    i = 1
    while i <= n:
        s += str(i)+" sheep..."
        i += 1
    return s

def solution(string):
  return string[::-1]

def square(n):
    return n*n

def hoopCount(n):
    if n >= 10:
        return 'Great, now move on to tricks'
    else:
        return 'Keep at it until you get it'

def cockroach_speed(s):
    return s // 0.036

def century(year):
    return (year + 99) // 100

def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum


def make_negative(number):
    return number if number <= 0 else number * -1


def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"


def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

def expression_matter(a, b, c):
    if 1 not in [a, b, c]:
        return a * b * c
    elif a == 1 and c == 1:
        return a + b + c
    elif a == 1 or (b == 1 and a < c):
        return (a + b) * c
    else:
        return a * (b + c)


def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))

def sale_hotdogs(n):
    if n < 5 and n>0:
        return n*100
    elif n>=5 and n<10:
        return n*95
    elif n>=10:
        return n*90
    else:
        return 0


def powers_of_two(n):
    a = []
    for i in range(0, n + 1):
        a.append(2 ** i)    
    return a

def find_average(array):
    if len(array) != 0:
        return sum(array) / len(array)
    else:
        return 0

def first_non_consecutive(arr):
    for n in arr:
        if n != arr.index(n)+arr[0]:
            return n


