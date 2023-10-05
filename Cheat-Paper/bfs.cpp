#include<iostream>
#include<queue>
#include<vector>
using namespace std;
bool visit[];
vector<pair<int, int>> vt[];	// first는 지금까지 간 거리, second는 node 번호
queue<pair<int,int>> qu;
int main() {
	qu.push({ 0,0 });	// first는 지금까지 간 거리, second는 node 번호
	while (!qu.empty()) {
		int sum = qu.front().first;
		int node = qu.front().second;
		qu.pop();
		visit[node] = 1;
		for (auto x : vt[node]) {
			if (!visit[x.second])
				qu.push({ sum + x.first, x.second });
		}
	}

}