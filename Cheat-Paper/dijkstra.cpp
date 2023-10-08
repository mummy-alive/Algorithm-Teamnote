#include <iostream>
#include <vector>
#include <queue>
#define INF 1000000000
using namespace std;
typedef pair<int, int> ci;
vector<int> dijkstra(int k, int v, int e, vector<vector<ci>> &weights) {
    vector<int> cost(v + 1, INF);
    priority_queue<ci, vector<ci>, greater<>> pq;
    pq.push({0, k});
    cost[k] = 0;
    while(!pq.empty()) {
        int w = pq.top().first, v=pq.top().second; pq.pop();
        if (w > cost[v]) continue;
        for (int i = 0; i < weights[v].size(); i++) {
            int next = weights[v][i].first;
            int new_weight = w + weights[v][i].second;
            if(new_weight<cost[next]) {
                cost[next] = new_weight;
                pq.push({new_weight, next});
            }
        }
    }
    return cost;
}
int main() {
    int v, e, k; cin >> v >> e >> k;
    vector<vector<ci>> weights(v+1);
    for (int i = 0; i < e; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        weights[u].push_back({v, w});
    }
    vector<int> cost = dijkstra(k, v, e, weights);
    for (int i = 1; i <= v; i++) {
        if(cost[i]==INF) {
            cout << "INF\n";
        } else {
            cout << cost[i] << '\n';
        }
    }
    return 0;
}
