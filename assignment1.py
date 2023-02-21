lower = 1
upper = 60
prime_numbers = []

print('Prime numbers between', lower, 'and', upper, 'are:')

prime_numbers = []
for num in range (lower, upper + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)
print(prime_numbers)
y= prime_numbers[ : :2]
print(y)