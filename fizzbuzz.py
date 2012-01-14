[(lambda x=x: print('FizzBuzz') if x % 3 == 0 and x % 5 == 0 else print('Fizz') if x % 3 == 0 else print('Buzz') if x % 5 == 0 else print(str(x)))() for x in range(1,101)]
