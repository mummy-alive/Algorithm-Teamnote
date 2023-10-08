#include <iostream>
#include <vector>
#include <algorithm> //sort()
using namespace std;
vector<int> parent;
struct edge {
    int u, v, w;
    edge(int u, int v, int w) {
        this->u = u;
        this->v = v;
        this->w = w;
    }
};
bool cmp(const edge &e1, const edge &e2) {
    return e1.w < e2.w;
}
int find(int x) {
    if (parent[x] == x) {
        return x;
    }
    return parent[x] = find(parent[x]);
}
void uni(int x, int y) {
    x = find(x);
    y = find(y);
    parent[min(x, y)] = max(x, y);
}
bool sameParent(int x, int y) {
    if (find(x) == find(y)) {
        return true;
    }
    return false;
}
int kruskal(int v, vector<edge> &graph) {
    int result = 0;

    parent.assign(v + 1, 0);
    for (int i = 1; i <= v; i++) {
        parent[i] = i;
    }
    for (int i = 0; i < graph.size(); i++) {
        int u = graph[i].u;
        int v = graph[i].v;
        if (sameParent(u, v)) {
            continue;
        }
        uni(u, v);
        result += graph[i].w;
    }
    
    return result;
}
int main() {
    int v, e, a, b, c;
    cin >> v >> e;
    vector<edge> graph;
    while (e--) {
        cin >> a >> b >> c;
        graph.push_back(edge(a, b, c));
    }
    
    sort(graph.begin(), graph.end(), cmp);
    cout << kruskal(v, graph);

    return 0;
}
