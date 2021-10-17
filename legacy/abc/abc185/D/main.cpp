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

struct AB
{
    double a;
    double b;
    AB(const double &_a, const double &_b) : a(_a), b(_b){};
    AB operator+(const AB &other)
    {
        AB ret(a + other.a, b + other.b);
        return ret;
    }
    AB operator-(const AB &other)
    {
        AB ret(a - other.a, b - other.b);
        return ret;
    }
    AB operator/(const double &other)
    {
        AB ret(a / other, b / other);

        return ret;
    }
};

int main()
{
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll m, n, ans = 0;

    cin >> n >> m;
    V<ll> a(m);
    REP(i, m)
    cin >> a[i];

    sort(a.begin(), a.end());

    ll temp = 0;
    ll width = 10e10;
    if (m)
    {
        if (a[0] > 1)
            width = a[0] - 1;
    }
    else
    {
        cout << 1 << endl;
        return 0;
    }

    REP(i, m - 1)
    {
        if (a[i + 1] - a[i] > 1)
            width = min(width, a[i + 1] - a[i] - 1);
    }

    if (a[m - 1] != n)
    {
        width = min(width, n - a[m - 1]);
    }

    if (a[0] > 1)
    {

        temp = a[0] - 1;
        if (temp % width)
            ans++;
        ans += temp / width;
    }

    REP(i, m - 1)
    {
        if (a[i + 1] - a[i] > 1)
        {
            temp = a[i + 1] - a[i] - 1;
            if (temp % width)
                ans++;
            ans += temp / width;
        }
    }
    if (a[m - 1] != n)
    {
        temp = n - a[m - 1];

        if (temp % width)
            ans++;
        ans += temp / width;
    }
    cout << ans << endl;
}