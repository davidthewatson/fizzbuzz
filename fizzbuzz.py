from sys import stdout
[(lambda x=x: stdout.write('FizzBuzz\n') if x % 3 == 0 and x % 5 == 0 else stdout.write('Fizz\n') if x % 3 == 0 else stdout.write('Buzz\n') if x % 5 == 0 else stdout.write(str(x) + '\n'))() for x in xrange(1,101)]
