n = int(input("n = "))
numbers = list(range(0, n + 1))
numbers[1] = 0
simple_numbers = []
for i in range(2, n+1):
    if numbers[i] != 0:
        j = i * 2
        while j < n + 1:
            numbers[j] = 0
            j += i
        simple_numbers.append(numbers[i])
    i+=1
print(simple_numbers)