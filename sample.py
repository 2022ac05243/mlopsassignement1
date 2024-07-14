import statistics

def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    average = total / count
    return average

numbers = [1, 2, 3, 4, 5]
result = statistics.mean(numbers)
print("The average is: ", result)



