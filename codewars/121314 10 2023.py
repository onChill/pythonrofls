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
    # Your code here
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
