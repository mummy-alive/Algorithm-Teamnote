"""
페르마의 소정리를 활용해 nCk mod m, 단 m은 소수 일때 O(n)의 시간으로 구하기
"""

# 모듈러 지수승(Modular Exponentiation) : b^e % mod
# 파이썬의 내장 pow(b,e,mod)가 이 함수보다는 빠르다는것을 참조할것.
# 페르마의 소정리를 사용해 nCk mod p 를 구해보자
# 분자 분모를 p의 지수승으로 약분해서 계산
# 주의사항 : p가 반드시 소수여야 함
# 큰 수의 이항계수를 O(n)의 시간 복잡도 안에 구하는 코드
# 참고 : https://velog.io/@kasterra/%ED%81%B0-%EC%88%98%EC%9D%98-%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-mod-K-%EA%B5%AC%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95

def mod_exp(b,e,mod):
    r = 1
    while e > 0:
        if (e&1) == 1:
            r = (r*b)%mod
        b = (b*b)%mod
        e >>= 1

    return r



# n!에서 p의 차수를 구함(n! = p^a * ... 일때, 가능한 최대의 a를 구함)
def fact_exp(n,p):
    e = 0
    u = p
    t = n
    while u <= t:
        e += t//u
        u *= p

    return e


def fermat_binom_advanced(n,k,p):
    # 말이 되지 않는 입력을 거름
    num_degree = fact_exp(n,p) - fact_exp(n-k,p)
    den_degree = fact_exp(k,p)
    if num_degree > den_degree:
        return 0

    if k > n:
        return 0

    # 분자를 계산하고 p가 몇승만큼 들어있는지를 계산한다
    num = 1
    for i in range(n,n-k,-1):
        cur = i
        while cur%p == 0:
            cur //= p
        num = (num*cur)%p

    # 분모를 계산하고 p가 몇승만큼 들어있는지를 계산한다
    denom = 1
    for i in range(1,k+1):
        cur = i
        while cur%p == 0:
            cur //= p
        denom = (denom*cur)%p

    # 분자 * 분모^(p-2) (mod p)
    return (num * mod_exp(denom,p-2,p))%p

if __name__ == '__main__':
    mod = 1000000007 # prime

    # (950 choose 100) mod 1000000007
    print(fermat_binom_advanced(950,100,mod)) # should be 640644226
