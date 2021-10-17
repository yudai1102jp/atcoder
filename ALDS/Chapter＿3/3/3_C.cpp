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
        tail->pre=last2;
    }
    // delete last1;
}
int main()
{
    //小数の桁数の出力指定
    //cout<<fixed<<setprecision(10);

    ios::sync_with_stdio(false);

    ll n;
    cin >> n;

    string op;
    ll key;

    INFO *optemp = new INFO;

    INFO *dammy = new INFO;
    head = tail = dammy;

    int len = 0;
    REP(i, n)
    {
        cin >> op;

        if (op == "deleteFirst")
            deleteFirst();
        else if (op == "deleteLast")
            deleteLast();
        else
        {
            cin >> key;
            if (op[0] == 'i')
            {
                INFO *newinfo = new INFO;
                newinfo->key = key;
                newinfo->next = head;
                head->pre = newinfo;

                head = newinfo;
            }
            else
            {

                INFO *now = head;
                ll pre;
                optemp = head;
                while (now != tail)
                {
                    if (now->key == key)
                    {
                        if (now == head)
                            deleteFirst();

                        else if (now->next == tail)
                            deleteLast();
                        else
                        {
                            INFO *temp = now->pre;
                            temp->next = now->next;
                            now = now->next;
                            now->pre = temp;
                        }
                        // delete now;
                        break;
                    }

                    now = now->next;
                }
            }
        }
        // INFO *pri = head;
        // while (pri != tail)
        // {
        //     cout << pri->key << ' ';
        //     pri = pri->next;
        // }
    }
    if (head == tail)
        cout << endl;
    else
    {
        while (true)
        {
            if (head->next == tail)
            {
                cout << head->key << endl;
                break;
            }
            cout << head->key << ' ';
            head = head->next;
        }
    }
}