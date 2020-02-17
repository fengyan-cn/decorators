def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

Sum = 0
for i in range(1,21):
    Sum += factorial(i)

print(Sum)
