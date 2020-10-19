# 백준 1644번 소수의 연속합
# https://www.acmicpc.net/problem/1644
'''
에레토스의 체로 소수 리스트 구하기 
-> 다르게 소수를 구하면 시간초과가 발생함

prefix sum 사용

two pointers 사용
'''

# 소수 리스트 구하기   
def Eratosthenes(n): 
    Primes=[] 
    isPrime=[1 for i in range(n+1)] 
    isPrime[0]=0 
    isPrime[1]=0 
    for i in range(2, n+1): 
        if isPrime[i]==1: 
            Primes.append(i) 
            for j in range(i*i, n+1, i): 
                isPrime[j]=0 
    return Primes

 
n = int(input())
res = 0

prime_numbers = Eratosthenes(n)

prefix_sum = [0]*(len(prime_numbers)+1)
for i in range(len(prime_numbers)):
    val = prime_numbers[i] + prefix_sum[i]
    prefix_sum[i+1] = val

length = len(prefix_sum)
left, right = 0, 0
while left < length:
    number = prefix_sum[right] - prefix_sum[left]
    if number == n:
        res += 1
        if right < length-1:
            right += 1
        else:
            left += 1
    elif number > n:
        left += 1
    else:
        if right < length-1:
            right += 1
        else:
            left += 1

print(res)
