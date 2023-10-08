#include <iostream>
#include <vector>
#include <utility>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
 
//비재귀 적으로 (x^y)%p 를 O(log y)로 구하는 코드
ll power(ll x,ull y, ll p){  
    ll res = 1;     // 결과 변수 초기화  
 
    x = x % p; //x가 p 이상일 경우를 대비해서 하는 연산 
 
    if (x == 0) return 0; // x 가 p의 배수일경우
 
    while (y > 0){  
        //y가 홀수라면 결과에 x를 곱한다.
        if (y & 1)  
            res = (res % p) * (x % p) % p;  
 
        //이제 y는 반드시 짝수일 것
        y = y>>1; // y = y/2  
        x = (x%p)*(x%p) % p;  
    }  
    return res;  
} 

// n!에서 p의 차수를 구하는 함수
int fact_exp(ll n, ll p){
	int e = 0;
    ll u = p;
    ll t = n;
    while(u <= t){
    	e += t / u;
        u *= p ;
    }   
    return e;
}

//그때그떄마다 계산하는 O(n) 코드
//p는 소수, k < p 일때 정상작동
ll fermat_binom(ll n, ll k, ll p){
	if(k > n) return 0;
 
    //분자 계산
    ll num = 1;
    for(ll i = n; i > n - k;--i)
    	num = (num*i) % p;
 
    //분모 계산
    ll denom = 1;
    for(ll i = 1;i < k + 1;++i)
    	denom = (denom * i) % p;
 
    return (num * power(denom,p-2,p))%p;
}
 
//팩토리얼과 역원을 미리 계산하는 O(n * logn) 코드
// p는 소수 , k < p 일때 정상 작동
pair<vector<ll>,vector<ll> > fermat_compute(ll n, ll p){
	pair<vector<ll>, vector<ll> > ret 
    = make_pair(vector<ll>(n,0),vector<ll>(n,0));
    vector<ll>& facts = ret.first;
    vector<ll>& invfacts = ret.second;
 
    facts[0] = 1;
    invfacts[0] = 1;
    for(ll i = 1 ;i < n;++i){
    	facts[i] = (facts[i - 1] * i) % p;
        invfacts[i] = power(facts[i], p - 2, p);
    }
 
    return ret;
}
 
ll binom_pre_computed(vector<ll> facts,vector<ll> invfacts,ll n,ll k,ll p){
	return (facts[n] * ((invfacts[k] * invfacts[n-k] % p))) %p;
}
 
ll fermat_binom_advanced(ll n,ll k,ll p){
	int num_degree = fact_exp(n,p) - fact_exp(n-k,p);
    int den_degree = fact_exp(k,p);
    
    if(num_degree > den_degree)
    	return 0;
    if(k > n)
    	return 0;
    
    //분자 계산
    ll num = 1;
    for(ll i = n;i > n - k;--i){
    	ll cur = i;
        while(cur % p == 0) cur /=p;
        num = (num * cur) % p;
    }
    
    //분모 계산
    ll denom = 1;
    for(ll i = 1;i < k + 1;++i){
    	ll cur = i;
        while(cur % p == 0) cur /= p;
        denom = (denom * cur) % p;
    }
    
    return(num * power(denom,p - 2,p))%p;
}
int main(void){
	ll n = 1009; // 미리 계산할 팩토리얼들의 개수
    ll mod = 1000000007;//소수
 
    pair<vector<ll>, vector<ll> > temp = fermat_compute(n,mod);
    vector<ll> facts = temp.first;
    vector<ll> invfacts = temp.second;
 
    cout <<"binom_pre_computed : "<<binom_pre_computed(facts,invfacts,950,100,mod) << '\n';
    cout <<"fermat_binom : "<< fermat_binom(950,100,mod) << '\n';
    cout << "fermat_binom_advanced : "<<fermat_binom_advanced(950,100,mod);
	return 0;
}
