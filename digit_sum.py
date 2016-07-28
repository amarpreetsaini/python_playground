def digit_sum(n):
    x = str(n)
    list = []
    sum = 0
    for digit in x:
        list += digit
    for digit in list:
        sum += int(digit)
    return sum
