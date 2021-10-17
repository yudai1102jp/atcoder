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

int main()
{
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;
    V<queue<int>> word(32);
    // reverse(S.begin(), S.end());
    int i = 0;
    for (auto &w : S)
    {
        // cout << w << w - 'a' << " and s" << i;
        word[w - 'a'].push(i);
        i++;
    }

    int now = 0;
    while (K > 0)
    {
        int i = 0;
        for (auto &w : word)
        {
            if (w.empty())
            {
                i++;
                continue;
            }
            // cout << w.front();
            while (!w.empty() && now > w.front())

                w.pop();

            if (w.empty())
            {
                i++;
                continue;
            }
            if (now <= w.front() && w.front() <= N - K)
            {

                now = w.front();
                cout << (char)('a' + i);
                K--;
                w.pop();
                break;
            }
            i++;
        }
    }
    cout << endl;
}