primes=[]
not_primes=[]

for num in numbers:
    is_prime = True
    if num == 1:
        continue
    if is_prime:
        primes.append(num)

    else:
        not_primes.append(num)

    for j in range(2,num//2+1):
        if num%j == 0:
            is_prime=False
            break

print('Primes: ', primes)
print('Not_primes: ', not_primes)
