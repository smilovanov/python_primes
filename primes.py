import time

# user input for calculations limit is packed in try to avoid typos and errors. Default is 10'000
try:
    calc_limit = int(input("Please enter limit for calculations(default is 100'000): "))
except ValueError:
    calc_limit = 100000
finally:
    print(f"Limit set to {calc_limit}")

# variable to format output
format_len = len(str(calc_limit))

# variable to store start time of calculations to measure optimization of script
start_time = time.time()

# calculations block
primes = [2]
pairs = 0
i = 3
while i <= calc_limit:
    prime = True
    for divider in primes:
        if i % divider == 0:
            prime = False
            break
    if prime:
        if i == primes[-1] + 2:
            print(f"Pair found: {primes[-1]} and {i}")
            pairs += 1
        primes.append(i)
    i += 1

# summary block
print(f"\n\nLimit was set to {calc_limit}")
print(f"{len(primes)} prime numbers in total. {pairs} of pairs with difference 2 between of them.")
print(f"{time.time() - start_time:.3f} seconds spent on calculations.")
