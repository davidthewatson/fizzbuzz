print(*((lambda x=x: 'FizzBuzz\n' if x % 15 == 0 else 'Fizz\n' if x % 3 == 0 else 'Buzz\n' if x % 5 == 0 else str(x) + '\n')() for x in range(1, 101)))
