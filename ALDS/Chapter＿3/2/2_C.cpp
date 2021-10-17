#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;
#define REP(i, n) for (ll i = 0; i < ll(n); i++)
#define REPD(i, n) for (ll i = n - 1; i >= 0; i--)
#define FOR(i, a, b) for (ll i = a; i < ll(b); i++)
#define FORD(i, a, b) for (ll i = a; i > ll(b); i--)

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

struct S
{
    int value;
    char cha;
};

void BubbleSort(vector<S> &C, int N)
{
    REP(i, N)
    {
        FORD(j, N - 1, i)
        {
            if (C[j].value < C[j - 1].value)
            {
                S temp = C[j];
                C[j] = C[j - 1];
                C[j - 1] = temp;
            }
        }
    }
}

void SelectionSort(vector<S> &C, int N)
{
    REP(i, N)
    {
        int minj = i;
        FOR(j, i, N)
        {
            if (C[j].value < C[minj].value)
            {
                minj = j;
            }
        }
        S temp = C[i];
        C[i] = C[minj];
        C[minj] = temp;
    }
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
    vector<S> A(n), B(n), C(n), D(n);
    REP(i, n)
    {
        char cc;
        int nn;
        cin >> cc >> nn;
        A[i] = {nn, cc};
        B[i] = {nn, cc};
        C[i] = {nn, cc};
        D[i] = {nn, cc};
    }

    BubbleSort(B, n);

    BubbleSort(C, n);
    BubbleSort(C, n);

    bool flag = true;
    REP(i, n)
    {
        if (i == n - 1)
            cout << B[i].cha << B[i].value << endl;
        else
            cout << B[i].cha << B[i].value << ' ';
        if (B[i].cha != C[i].cha)
            flag = false;
        if (B[i].value != C[i].value)
            flag = false;
    }

    if (flag)
        cout << "Stable" << endl;
    else
        cout << "Not stable" << endl;

    SelectionSort(A, n);

    SelectionSort(D, n);
    SelectionSort(D, n);

    flag = true;
    REP(i, n)
    {
        if (i == n - 1)
            cout << A[i].cha << A[i].value << endl;
        else
            cout << A[i].cha << A[i].value << ' ';
        if (A[i].cha != B[i].cha)
            flag = false;
        if (A[i].value != B[i].value)
            flag = false;
    }
    if (flag)
        cout << "Stable" << endl;
    else
        cout << "Not stable" << endl;

}