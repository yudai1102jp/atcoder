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

void solve(long long N, std::vector<long long> x, std::vector<long long> y)
{
    int ans = 0;
    REP(i, N - 1)
    {
        FOR(j, i + 1, N)
        {

            P a = make_pair(x[i], y[i]);
            P b = make_pair(x[j], y[j]);
            int x1 = abs(x[i] - x[j]);

            int y1 = abs(y[i] - y[j]);

            if (-1 * x1 <= y1 && y1 <= x1)
            {
                ans++;
            }
        }
    }
    cout << ans << endl;
}

// Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
int main()
{
    long long N;
    scanf("%lld", &N);
    std::vector<long long> x(N);
    std::vector<long long> y(N);
    for (int i = 0; i < N; i++)
    {
        scanf("%lld", &x[i]);
        scanf("%lld", &y[i]);
    }
    solve(N, std::move(x), std::move(y));
    return 0;
}