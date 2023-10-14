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

















