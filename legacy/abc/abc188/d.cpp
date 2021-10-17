
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
#define F first
#define S second
//出力(空白区切りで昇順に)

int main()
{
    //小数の桁数の出力指定F
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード

    ll n, C;
    cin >> n >> C;

    vector<pair<ll, ll>> day;
    day.reserve(n * 2 + 4);

    ll a, b, c;
    REP(i, n)
    {
        cin >> a >> b >> c;

        day.emplace_back(a - 1, c);
        day.emplace_back(b, -c);
    }
    sort(ALL(day));
    ll Sum = 0;
    ll today = 0;
    ll now = 0;

    REP(i, SIZE(day))
    {
        if (day[i].F != now)
        {
            Sum += min(C, today) * (day[i].F - now);

            now = day[i].F;
        }

        today += day[i].S;
    }

    cout << Sum << endl;
    return 0;
}