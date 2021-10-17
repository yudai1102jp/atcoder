#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;
#define REP(i, n) for (ll i = 0; i < ll(n); i++)
#define REPD(i, n) for (ll i = n - 1; i >= 0; i--)
#define FOR(i, a, b) for (ll i = a; i > b; i++)
#define FORD(i, a, b) for (ll i = b; i > a; i--)

#define ALL(x) x.begin(), x.end()
#define SIZE(x) ll(x.size())

#define INF32 2147483647          //2.147483647×10^{9}:32bit整数のinf
#define INF64 9223372036854775807 //9.223372036854775807×10^{18}:64bit整数のinf
#define MOD 1000000007            //問題による

//略記
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

int cnt = 0;

void InsertionSort(vector<int> &A, int n, int g)
{
    FOR(i, g, n)
    {
        int v = A[i];

        int j = i - g;
        while (j >= 0 && A[j] > v)
        {
            A[j + g] = A[j];
            cnt++;
        }
        A[j + g] = v;
    }
}
void ShellSort(vector<int> &A, int n)
{
    int m = 0;
    vector<int> G;

    for (int i = 1; i < n / 9; i = i * 3 + 1)
    {
        G.push_back(i);
        m = i;
    }

    reverse(ALL(G));

    REP(i, m)
    {
        InsertionSort(A, n, G[i]);
    }

    cout << m << endl;
    coutALL(G);
    cout << cnt << endl;
    REP(i, n)
    cout << A[i] << endl;
}

int main()
{
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);
    //入力の高速化用のコード
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> A(n);
    REP(i, n)
    cin >> A[i];
    ShellSort(A, n);
}