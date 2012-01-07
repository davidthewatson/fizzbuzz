all = list(xrange(1,101))
divisible_by_3 = dict((x, 'Fizz') for x in filter(lambda x: x % 3 == 0, all))
divisible_by_5 = dict((x, 'Buzz') for x in filter(lambda x: x % 5 == 0, all))
divisible_by_3_and_5 = dict((x, 'FizzBuzz') for x in filter(lambda x: x % 3 == 0 and x % 5 == 0, all))
remainder = dict((x, x) for x in [x for x in all if not x in divisible_by_3 and not x in divisible_by_5 and not x in divisible_by_3_and_5])
all_dict = dict(divisible_by_3.items() + divisible_by_5.items() + divisible_by_3_and_5.items() + remainder.items())
for x in all:
    print all_dict[x]
