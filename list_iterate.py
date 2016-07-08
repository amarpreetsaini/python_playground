#Create a function called total that adds up all the elements of an arbitrary list and returns that count, using the existing code as a hint. Use a for loop so it can be used for any size list.

n = [3, 5, 7]

def total(numbers):
    result = 0;
    for i in range(len(numbers)):
        result +=numbers[i]
    return result
