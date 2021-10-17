// #include <iostream>
// #include <algorithm>
// #include <vector>
// #include <iomanip>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define REP(i, n) for (ll i = 0; i < ll(n); i++)
#define REPD(i, n) for (ll i = n - 1; i >= 0; i--)
#define FOR(i, a, b) for (ll i = a; i < ll(b); i++)
#define FORD(i, a, b) for (ll i = a; i > b; i--)

#define ALL(x) x.begin(), x.end()
#define SIZE(x) ll(x.size())

#define INF32 2147483647          //2.147483647×10^{9}:32bit整数のinf
#define INF64 9223372036854775807 //9.223372036854775807×10^{18}:64bit整数のinf
#define MOD 1000000007            //問題による

//略記
#define V vector
#define P pair<int, int>
#define F first
#define S second
//出力(空白区切りで昇順に)
#define coutALL(x)                                \
    for (auto i = x.begin(); i != --x.end(); i++) \
        cout << *i << " ";                        \
    cout << *--x.end() << endl;

//aをbで割る時の繰上げ,繰り下げ
ll myceil(ll a, ll b) { return (a + (b - 1)) / b; }
ll myfloor(ll a, ll b) { return a / b; }

struct NQ
{
    string name;
    int time;
    NQ(const string &_a, const int &_b) : name(_a), time(_b){};
};

int main()
{
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);

    ios::sync_with_stdio(false);

    queue<NQ> que;
    ll i;
    ll n;
    ll quontam;
    cin >> n >> quontam;

    string name;
    ll time;

    REP(i, n)
    {
        cin >> name >> time;

        que.emplace(name, time);
    }
    NQ temp("", 0);
    time = 0;
    temp = que.front();

    while (!que.empty())
    {
        temp = que.front();
        que.pop();
        if (temp.time > quontam)
        {
            time += quontam;
            temp.time -= quontam;
            que.push(temp);
        }
        else
        {
            time += temp.time;
            cout << temp.name << ' ' << time << endl;
        }
    }
}