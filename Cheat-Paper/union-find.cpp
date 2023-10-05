#include<iostream>
using namespace std;
int parent[];
int fnd(int node) {
	if (parent[node] == node) return node;
	return parent[node] = fnd(parent[node]);
}

int merge(int x, int y) {
	x = fnd(x);
	y = fnd(y);
	if (x == y) return;
	parent[y] = x;	//오름차순으로 parent와 child 결정한다면 이 부분 수정
}

int main() {
	for (int i = 1; i <= 1e9; i++)
		parent[i] = i;
	//여기서부터 입력
	return 0;
}