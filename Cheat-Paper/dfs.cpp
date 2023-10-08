#include<iostream>
#include<vector>
using namespace std;
int arr[];
bool visit[];
vector<int> vt[];
void dfs(int node) {	//부가적인 문제조건에 따라 return 조건 및 for문 속 작업 수정 필요
	if (visit[node]) return;
	visit[node] = 1;
	for (auto x : vt[node]) {
		dfs(x);
	}
}
