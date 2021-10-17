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
#define coutALL(x)                                \
    for (auto i = x.begin(); i != --x.end(); i++) \
        cout << *i << " ";                        \
    cout << *--x.end() << endl;

//aをbで割る時の繰上げ,繰り下げ
ll myceil(ll a, ll b) { return (a + (b - 1)) / b; }
ll myfloor(ll a, ll b) { return a / b; }
vector<vector<ll>> matrix(vector<vector<ll>> &a, vector<vector<ll>> &b)
{
    vector<vector<ll>> ans(3, vector<ll>(3, 0));

    REP(i, 3)
    {
        REP(j, 3)
        {
            REP(k, 3)
            {
                ans[i][j] = ans[i][j] + a[i][k] * b[k][j];
            }
        }
    }
    return ans;
}

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
    cin >> xy[i][0] >> xy[i][1];

    ll m;
    cin >> m;
    char op;
    ll p;
    vector<vector<vector<ll>>> op_list(m + 3, vector<vector<ll>>(3, vector<ll>(3, 0)));
    op_list[0][0][0] = 1;
    op_list[0][1][1] = 1;
    op_list[0][2][2] = 1;

    vector<vector<ll>> op1{{0, 1, 0}, {-1, 0, 0}, {0, 0, 1}};
    vector<vector<ll>> op2{{0, -1, 0}, {1, 0, 0}, {0, 0, 1}};

    vector<vector<ll>> op3{{1, 0, -2}, {0, -1, 0}, {0, 0, 1}};
    vector<vector<ll>> op4{{-1, 0, 0}, {0, 1, -2}, {0, 0, 1}};

    REP(i, m)
    {
        cin >> op;

        if (op == '1')
        {
            op_list[i + 1] = matrix(op_list[i], op1);
        }
        else if (op == '2')
        {
            op_list[i + 1] = matrix(op_list[i], op2);
        }
        else if (op == '3')
        {
            cin >> p;
            op3[0][2] = -2 * (ll)p;

            REP(j, 3)
            {
                REP(k, 3)
                {
                    cout << op3[j][k] << ' ';
                }
                cout << endl;
            }

            op_list[i + 1] = matrix(op_list[i], op3);
        }
        else if (op == '4')
        {
            cin >> p;
            op4[1][2] = -2 * (ll)p;
            op_list[i + 1] = matrix(op_list[i], op4);
        }

        REP(j, 3)
        {
            REP(k, 3)
            {
                cout << op_list[i + 1][j][k] << ' ';
            }
            cout << endl;
        }
        cout << endl;
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
        REP(i, 3)
        {
            x += op_list[a][0][i] * xy[b - 1][i];
            y += op_list[a][1][i] * xy[b - 1][i];
        }
        cout << x << ' ' << y << endl;
    }
}