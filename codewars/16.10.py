def reverse_list(l):
  return l[::-1]

def get_char(c):
    return chr(c)

def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."

def find_difference(a, b):
	return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])

def is_uppercase(inp):
    return inp.upper()==inp

def xor(a,b):
    return a != b

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

def no_space(x):
    return x.replace(' ' ,'')

def quarter_of(n):
    return (n + 2) // 3

def chromosome_check(sperm):
    gender = {"XY" : "son", "XX" : "daughter"}
    
    return "Congratulations! You're going to have a {}.".format(gender[sperm])
