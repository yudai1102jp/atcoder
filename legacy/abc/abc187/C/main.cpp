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

// Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
int main()
{
    long long N;
    cin >> N;

    V<V<string>> S1('z' - 'a' + 1);
    V<string> S2;
    string temp;
    REP(i, N)
    {
        cin >> temp;
        if (temp[0] == '!')
        {
            S2.push_back(temp);
        }
        else
        {
            S1[temp[0] - 'a'].push_back(temp);
        }
    }
    REP(i, S2.size())
    {

        string te = S2[i].substr(1, S2[i].length());
        
        if (find(S1[te[0] - 'a'].begin(), S1[te[0] - 'a'].end(), te) != S1[te[0] - 'a'].end())
        {
            cout << te << endl;
            exit(1);
        }
    }

    cout << "satisfiable" << endl;
    return 0;
}
