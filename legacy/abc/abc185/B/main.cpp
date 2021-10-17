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
    int m, n, Max, t;

    ll a;
    ll b;
    ll temp;

    cin >> n >> m >> t;
    Max = n;
    temp = 0;
    REP(i, m)
    {
        cin >> a >> b;
        n -= (a - temp);
        if (n <= 0)
        {
            cout << "No" << endl;
            return 0;
        }
        n += b - a;
        n = min(n, Max);
        temp = b;
    }
    if (n <= t - b)
    {
        cout << "No" << endl;
        return 0;
    }
    cout << "Yes" << endl;
}