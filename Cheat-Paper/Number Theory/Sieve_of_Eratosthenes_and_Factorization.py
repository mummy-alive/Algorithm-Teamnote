prime = [1 for i in range(10**6+1)]
prime[0], prime[1] = 0, 0

now = 2
while now * now <= 10**6:
    if prime[now]:
        for i in range(2*now, 10**6+1, now):
            prime[i] = 0
    now += 1

now = 2
while now * now <= N_cp:
    if prime[now]:
        while N_cp%now == 0:
            N_factors.append(str(now))
            N_cp //= now
    now += 1
if N_cp != 1:
    N_factors.append(str(N_cp))
