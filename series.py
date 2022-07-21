
#define Fib
fib = [0,1]

# The Lucas series has the same recursive relationship as the Fibonacci sequence, where each term is the sum of the two previous terms, but with different starting values.

def lucas(n,value1=2,value2=1):
    lucas = [2, 1]
    sum = 0
#Loop ntil you find t
    while len(lucas) < n:
        a = lucas[0]
        b = lucas[1]
        # Fibonacci
        sum = lucas[-2] + lucas[-1]

        # Append to the fib list
        lucas.append(sum)

    print('lucas',lucas)
    return sum


def fibonacci(n):
    '''return the nth value in the fibonacci series. '''

    #In your series.py module, add a new function lucas that returns the nth value in the lucas numbers

#Loop ntil you find nth position
    while len(fib) < n:
        a = fib[0]
        b = fib[1]
        #Fibonacci
        sum = fib[-2] + fib[-1]

        #Append to the fib list
        fib.append(sum)

#If it is the first or second items in the lisprev)}')
    print('fib',fib)
    return sum
    lucas(n)


def sum_series(n, value2 = 0, value1 = 1):

        # Use the functions
        lucas(n)
        fibonacci(n)

sum_series(5)