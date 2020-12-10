# 암호 해독
--ing

def get_primes(n):
    res = []
    for i in range(2, n):
        if n % i == 0:
            res.append(i)
    return res

def decrypt(p, q):
    # To-do
    p_primes = get_primes(p)
    print(p_primes)
    q_primes = get_primes(q)
    print(q_primes)

    for i in p_primes:
        for j in q_primes:
            if i == j:
                return i



p = 6
q = 10
result = decrypt(p, q)
print(result)