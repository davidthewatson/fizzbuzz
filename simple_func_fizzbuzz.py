from __future__ import print_function


def fbn(n, d, s):
    for i, j in enumerate(d):
        if n % j == 0:
            return s[i]
    return n

# pep8 line length - the bane of my existence
print(*(fbn(i, (15, 5, 3), ('fizzbuzz', 'buzz', 'fizz')) for i in range(1, 101)))
