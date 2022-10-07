"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if number_of_primes <= 0:
        raise ValueError(f'number_of_primes = {number_of_primes} must be a postive number greater than 0.')
    
    list = []

    if number_of_primes >= 1:
        list.append(2)
    if number_of_primes >= 2:
        list.append(3)

    i = 0
    j = 0
    n = 1
    while i < number_of_primes - 2:
        appended = True
        prime = 0
        if j % 2 == 0:
            x = 6*n-1
        else:
            x = 6*n+1
            n += 1
        
        k = 0
        prime = x
        while k < len(list):
            if prime % list[k] == 0:
                appended = False
            k += 1

        if appended:
            i += 1
            list.append(x)
        j += 1

    return list
