import sys
input = sys.stdin.readline

prime = [1 for i in range(10**6+1)]
prime[0], prime[1] = 0, 0
now = 2
while now * now <= 10**6:
    if prime[now]:
        for i in range(2*now, 10**6+1, now):
            prime[i] = 0
    now += 1

def prime_factors(x): #소인수분해 함수
    target = x
    factors = []
    n = 2
    while n*n <= x:
        if prime[n]:
            while target % n == 0:
                factors.append(n)
                target //= n
        n += 1

    if target != 1:
        factors.append(target)
    return factors

def find_largest_2pow(n):
    if n <= 1:
        return 1
    if 1 << (n.bit_length() - 1) == n:
        return 1 << (n.bit_length() - 2)
    else:
        return 1 << (n.bit_length() - 1)

def func(k):
    k_c = k
    vt = prime_factors(k)
    if not vt:
        return k_c
    else:
        new_vt = list(map(str, vt))
        new_vt.sort(key=lambda x:x*13, reverse=True)

        res = ''
        for x in new_vt:
            res += x

        return int(res)

n = int(input())

if n == 2:
    print(3)
elif n == 4:
    print(25)
else:
    par = find_largest_2pow(n)
    check = prime_factors(par)
    new_par = (par//2)*3

    if new_par < n:
        check.remove(2)
        check.append(3)
        new_ck = list(map(str, check))
        new_ck.sort(key=lambda x:x*13, reverse=True)
        res = ''
        for x in new_ck:
            res += x
    else:
        new_ck = list(map(str, check))
        new_ck.sort(key=lambda x:x*13, reverse=True)
        res = ''
        for x in new_ck:
            res += x

    res = int(res)
    print(func(n) + res)
