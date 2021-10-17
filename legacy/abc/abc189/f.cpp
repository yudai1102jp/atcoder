#include <iostream>
#include <algorithm>
#include <iomanip>
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
    cout << fixed << setprecision(5);
    //入力の高速化用のコード

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll m, n, k, len;
    cin >> n >> m >> k;

    if (k > 0)
    {
        V<ll> A(k);
        REP(i, k)
        {
            cin >> A[i];
        }
        len = 1;
        ll Max = 1;
        REP(i, k - 1)
        {

            if (A[i] + 1 == A[i + 1])
            {
                len++;
            }
            else
                len = 1;
            Max = max(Max, len);
        }
        if (Max >= m)
            cout << -1 << endl;
        else
        {

            vector<AB> p(n, AB(0, 0));

            int k_count = k - 1;

            if (A[k_count] == n - 1)
            {
                p[n - 1].b = 1;
                k_count--;
            }
            else
                p[n - 1].a = 1;

            AB temp(0, 0);

            REPD(i, n - 1)
            {

                temp = temp + p[i + 1];
                if (i + m + 1 < n)
                {
                    temp = temp - p[i + m + 1];
                }
                if (k_count >= 0 && i == A[k_count])
                {
                    p[i].b = 1;
                    k_count--;
                }
                else
                {
                    p[i] = temp / (double)m;
                    p[i].a++;
                }
                        }

            AB Ans = p[0];

            Ans.b = 1 - Ans.b;

            cout << Ans.a / Ans.b << endl;
        }
    }
    else
    {

        vector<double> p(n, 0);
        p[n - 1] = 1;
        double temp = 0;
        REPD(i, n - 1)
        {
            temp += p[i + 1];
            if (i + m + 1 < n)
                temp -= p[i + m + 1];

            p[i] = temp / m;

            p[i]++;
        }

        cout << p[0] << endl;
    }
}