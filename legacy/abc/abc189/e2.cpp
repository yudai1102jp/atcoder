#include <iostream>
#include <algorithm>
#include <vector>

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

struct A
{
    V<V<int>> a;
    V<ll> b;
    A(V<V<int>> _a, const V<ll> &_b) : a{_a}, b(_b) {}
};

int main()
{
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;
    cin >> n;
    vector<vector<ll>> xy(n + 1, vector<ll>(2));

    REP(i, n)
    cin >> xy[i + 1][0] >> xy[i + 1][1];

    ll m;
    cin >> m;
    int op;
    ll p;
    V<A> Op;
    A res({{1, 0}, {0, 1}}, {0, 0});
    Op.emplace_back(res);
    REP(i, m)
    {
        cin >> op;

        if (op == 1)
        {
            res.a = {{0, 1}, {-1, 0}};
            res.b = {0, 0};
        }
        else if (op == 2)
        {

            res.a = {{0, -1}, {1, 0}};
            res.b = {0, 0};
        }
        else
        {
            cin >> p;
            if (op == 3)
            {
                res.a = {{-1, 0}, {0, 1}};
                res.b = {2 * p, 0};
            }
            else
            {
                res.a = {{1, 0}, {0, -1}};
                res.b = {0, 2 * p};
            }
        }

        A last = Op.back();

        A New({{0, 0}, {0, 0}}, {0, 0});
        REP(i, 2)
        {
            New.b[i] += res.b[i];
            REP(j, 2)
            {
                New.b[i] += res.a[i][j] * last.b[j];

                REP(k, 2)
                New.a[i][j] += res.a[i][k] * last.a[k][j];
            }
        }

        Op.emplace_back(New);
    }

    ll q;
    cin >> q;
    ll a;
    ll b;

    ll x;
    ll y;

    REP(i, q)
    {
        cin >> a >> b;
        x = y = 0;
        REP(j, 2)
        {
            x += Op[a].a[0][j] * xy[b][j];
            y += Op[a].a[1][j] * xy[b][j];
        }
        cout << x + Op[a].b[0] << ' ' << y + Op[a].b[1] << endl;
    }
}