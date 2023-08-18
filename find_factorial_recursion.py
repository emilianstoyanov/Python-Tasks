def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


inp_number = int(input())
t = factorial(inp_number)

print(f'The factorial of the number {inp_number} is {t}')
