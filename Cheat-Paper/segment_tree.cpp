#include<iostream>
using namespace std;
int arr[];		//트리값 저장
int n;			//n은 원소의 개수
int query(int lt, int rt) {	//left와 right. left=(왼쪽)+base-1 // right=(오른쪽)+base-1
	int sum = 0;			//부분합 구하는 query함수
	while (lt <= rt) {
		if (lt % 2) {
			sum += arr[lt];
			lt++;
		}
		if (!(rt % 2)) {
			sum += arr[rt];
			rt--;
		}
		lt /= 2;
		rt /= 2;
	}
	return sum;
}

void update(int idx, int value) {	//특정 번호의 원소 update
	arr[idx] = value;
	for (int i = idx / 2; i >= 1; i /= 2)
		arr[i] = arr[i * 2] + arr[i * 2 + 1];
}

int main() {
	int base;
	for (base = 1; base < n; base *= n);
	for (int i = 0; i < n; i++)
		cin >> arr[base + 1];
	for (int i = base - 1; i >= 1; i--)
		arr[i] = arr[i * 2] + arr[i * 2] + 1;	//합쳐서 segment tree 구축
	

	return 0;
}