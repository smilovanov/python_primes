import time

#user input for calculations limit is packed in try to avoid typos and errors. Default is 10'000
try:
	calc_limit = int (input("Please enter limit for calculations: "))
except:
	calc_limit = 10000
finally: 
	print (f"Limit set to {calc_limit}")

#variable to format output
format_len = len(str(calc_limit))

#used only to measure optimization of script
start_time = time.time ()

#calculations block
primes = {2}
i = 3
while i <= calc_limit:
	prime = True
	for divider in primes:
		if i % divider == 0:
			prime = False
	if prime == True: 
		print (f"{i:<{format_len}d}", end="",flush=True)
		primes.add (i)
	i += 1

#summary block
print (f"\n\nLimit was set to {calc_limit}")
print (f"{len(primes)} prime numbers in total.")
print (f"{time.time()-start_time:.3f} seconds spent on calculations.")