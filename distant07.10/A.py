def even_or_odd(numbers):
    evenNumbers = []
    oddNumbers = []
    for i in numbers:
        if i % 2 == 0:
            evenNumbers.append(i)
        else:
            oddNumbers.append(i)
    print('even numbers: ' + String(evenNumbers))
    print('even numbers: ' + String(oddNumbers))
even_or_odd([1, 2, 4])
