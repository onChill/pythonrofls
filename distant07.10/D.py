def make_negative(number):
    if number > 0:
        number -= number * 2
    return number
print(make_negative(333))
