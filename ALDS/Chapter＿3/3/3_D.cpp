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

typedef struct info
{
    ll key;
    struct info *next;
    struct info *pre;
} INFO;
INFO *head;
INFO *tail;

void deleteFirst()
{
    head = head->next;
    // delete head->pre;
}
void deleteLast()
{
    INFO *last1 = tail->pre;
    if (last1 == head)
    {
        head = tail;
    }
    else
    {
        INFO *last2 = last1->pre;
        last2->next = tail;
        tail->pre = last2;
    }
    // delete last1;
}
int main()
{
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);

    ios::sync_with_stdio(false);

    string c;
    cin >> c;
    int len = c.length();
    int que[20002];
    int battery[10002];
    int battery_height[10002];
    int battery_num = 0;

    int now = 0;
    ll ans = 0;

    REP(i, len)
    {
        if (c[i] == '\\')
        {
            que[now++] = i;
        }
        else if (c[i] == '/' && now != 0)
        {
            int start = que[--now];
            ans += i - start;
            battery_height[battery_num] = start;
            battery[battery_num] = i - start;

            ll temp = 0;
            int new_num = battery_num;
            REPD(j, battery_num + 1)
            {
                temp += battery[j];
                if (battery_height[j] > start)
                {
                    battery[j] = temp;
                    new_num = j;
                }
            }
            battery_num = ++new_num;
        }
    }
    cout << ans << endl;
    cout << battery_num;
    REP(i, battery_num)
    {
        cout << ' ' << battery[i];
    }
    cout << endl;
}