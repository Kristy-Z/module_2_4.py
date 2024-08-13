numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes=[]
not_primes=[]

for num in numbers:
 for j in range(2,15):
   is_prime=True
  if num//j>=1:
    primes.append(num)
 break

else:
 not_primes.append(num)

print('Primes: ', primes)
print('Not_primes: ', not_primes)
