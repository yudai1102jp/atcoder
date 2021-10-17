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

bool check(ll &n, int &N, int &K, V<ll> &a)
{
    ll now = 0;
    int co = 0;
    REP(i, N + 1)
    {
        now += a[i];
        if (now >= n)
        {
            co++;
            now = 0;
        }
    }
    if (co > K)
        return true;
    else
        return false;
}

void init(int &N, ll &L, int &K, V<ll> &a)
{
    cin>> L;
    cin >> K;
    ll x;
    ll pre = 0;
    ll now;
    REP(i, N)
    {
        cin >> x;
        now = x - pre;
        a[i] = now;
        pre = x;
    }
    a[N] = L - pre;
}

ll solve(int &N, ll &L, int &K, V<ll> &a)
{
    ll ok = 0;
    ll ng = L;
    ll now;
    while (ng - ok != 1)
    {
        now = (ok + ng) / 2;
        if (check(now, N, K, a))
        {
            ok = now;
        }
        else
        {
            ng = now;
        }
    }

    return ok;
}

int main()
{
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K;
    cin>>N;
    ll L;

    V<ll> a(N + 4);
    init(N, L, K, a);
    ll ans = solve(N, L, K, a);

    cout << ans << endl;
}