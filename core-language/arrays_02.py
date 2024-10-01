#prime numbers

# number -> [a,c,v]
def factors(number):
    factors = []
    for index in range( 1, number + 1 ):
        if number % index == 0:
            factors.append(index)
    return factors


def is_prime(number):
    return factors(number) == [1,number]


def list_of_primes(number):
    prime_numbers = []
    for index in range(1,number):
        if is_prime(index):
            prime_numbers.append(index)
    return prime_numbers

first_100_primes = list_of_primes(101)
print(first_100_primes)

# nums -> print string symbol
def graph_number(nums):
    counter = 0
    for num in nums:
        symbol = '🔋'
        #symbol = '*'
        if counter % 2 == 0:
            symbol = 's'
            symbol = '🔧'
           # symbol = '🔋'
        print(symbol*num)
        counter += 1

graph_number(first_100_primes)
