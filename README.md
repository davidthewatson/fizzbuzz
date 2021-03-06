My lighting talk on these fizzbuzz riffs is here: http://slides.com/davidthewatson/obfuscated-fizzbuzz#/

My mildly dysfunctional versions of FizzBuzz in python 3.

The shortest of these is the single line lambda version that is not pep8-compliant due to the line length. I've yet to see a shorter version in python 3. This clocks in at 151 characters.

         205 function calls in 0.001 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.000    0.000    0.000    0.000 non-pep8_lambda_fizzbuzz.py:1(<genexpr>)
      100    0.000    0.000    0.000    0.000 non-pep8_lambda_fizzbuzz.py:1(<lambda>)
        1    0.000    0.000    0.001    0.001 non-pep8_lambda_fizzbuzz.py:1(<module>)
        1    0.000    0.000    0.001    0.001 {built-in method exec}
        1    0.001    0.001    0.001    0.001 {built-in method print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

The pep8-compliant lambda version is longer, but perhaps more readable. Performance is, of course, identical to the one-line version.

         205 function calls in 0.001 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.000    0.000    0.000    0.000 pep8_lambda_fizzbuzz.py:1(<genexpr>)
      100    0.000    0.000    0.000    0.000 pep8_lambda_fizzbuzz.py:1(<lambda>)
        1    0.000    0.000    0.001    0.001 pep8_lambda_fizzbuzz.py:1(<module>)
        1    0.000    0.000    0.001    0.001 {built-in method exec}
        1    0.001    0.001    0.001    0.001 {built-in method print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

The loopy set version is surprisingly fast given how much more iteration there is - 2 to 5 times as much depending on which versions you are comparing.

         524 function calls in 0.001 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 pep8_loopy_sets_fizzbuzz.py:1(<module>)
       34    0.000    0.000    0.000    0.000 pep8_loopy_sets_fizzbuzz.py:3(<genexpr>)
      100    0.000    0.000    0.000    0.000 pep8_loopy_sets_fizzbuzz.py:3(<lambda>)
       21    0.000    0.000    0.000    0.000 pep8_loopy_sets_fizzbuzz.py:4(<genexpr>)
      100    0.000    0.000    0.000    0.000 pep8_loopy_sets_fizzbuzz.py:4(<lambda>)
        7    0.000    0.000    0.000    0.000 pep8_loopy_sets_fizzbuzz.py:5(<genexpr>)
      100    0.000    0.000    0.000    0.000 pep8_loopy_sets_fizzbuzz.py:6(<lambda>)
       54    0.000    0.000    0.000    0.000 pep8_loopy_sets_fizzbuzz.py:7(<genexpr>)
        1    0.000    0.000    0.000    0.000 pep8_loopy_sets_fizzbuzz.py:7(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method exec}
      100    0.001    0.000    0.001    0.000 {built-in method print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

The canonical version is unremarkable, except that it _seems_ like it should be faster.

         103 function calls in 0.001 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 canonical_fizzbuzz.py:1(<module>)
        1    0.000    0.000    0.001    0.001 {built-in method exec}
      100    0.001    0.000    0.001    0.000 {built-in method print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

<a href="http://davidwatson.org/">david watson</a>
