#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>

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

//aをbで割る時の繰上げ,繰り下げ
ll myceil(ll a, ll b) { return (a + (b - 1)) / b; }
ll myfloor(ll a, ll b) { return a / b; }

int main()
{
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, k;
    cin >> n >> m;
    V<P> A(m);
    REP(i, m)
    cin >> A[i].F >> A[i].S;
    cin >> k;
    V<P> C(k);
    REP(i, k)
    cin >> C[i].F >> C[i].S;

    int ans = 0;
    V<int> N(n + 1, 0);

    REP(i, k)
    N[C[i].F]++;
    REP(i, m)
    {
        if (N[A[i].F] > 0 && N[A[i].S] > 0)
            ans++;
    }

    int po = pow(2, k);
    int count, now;
    for (int i = 1; i < po; i++)
    {
        now = (i - 1) ^ i;
        REP(j, k)
        {
            if ((now >> j) & 1)
            {
                if ((i >> j) & 1)
                {
                    N[C[j].S]++;
                    N[C[j].F]--;
                }

                else
                {
                    N[C[j].S]--;
                    N[C[j].F]++;
                }
            }
        }
        count = 0;
        REP(j, m)
        {

            if (N[A[j].F] && N[A[j].S])
                count++;w
        }
        ans = max(ans, count);
    }

    cout << ans << endl;
    return 0;
}