def s_len (S):
    N = len(S)
    if S == S[::-1]:
        print(N)
    else:
        for l in reversed(range(1, N)):
            for j in range(1+N-l):
                t = S[j:l+j]
                if t == t[::-1]:
                    print(l)
                    return

S = input()
s_len(S)
