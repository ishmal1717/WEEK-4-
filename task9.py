def average(*numbers):
    avg = sum(numbers) / len(numbers)
    return avg

result = average(10, 20, 30, 40, 50)

print("Average =", result)