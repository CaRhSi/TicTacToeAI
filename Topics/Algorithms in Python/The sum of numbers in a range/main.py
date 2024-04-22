def range_sum(numbers, start, end):
    summation = 0
    for i in range(len(numbers)):
        if int(start) <= int(numbers[i]) <= int(end):
            summation += int(numbers[i])
    return summation


input_numbers = input().split()
a, b = input().split()
print(range_sum(input_numbers, a, b))
