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

struct hwt
{
    int h;
    int w;
    int t;
    hwt(const int &_h, const int &_w, const int &_t) : h(_h), w(_w), t(_t){};
};

V<V<int>>
mat_mul(const V<V<int>> &A, const V<V<int>> &B, const int n)
{
    V<V<int>> ans(n, V<int>(n, 0));
    REP(i, n)
    REP(k, n)
    REP(j, n)
    ans[i][j] += A[i][k] * B[k][j];
    return ans;
}
int solve(int &H, int &W, V<string> &MAP, int &gw, int &gh, int noww, int nowh, int time, V<V<pair<int, int>>> &alpabet, V<int> &alpabet_num, V<bool> alpabet_char)
{
    V<V<bool>> used(H, V<bool>(W, false));
    queue<hwt> que;
    que.emplace(nowh, noww, time);
    hwt now(0, 0, 0);
    while (true)
    {
        if (que.empty())
            return -1;
        now = que.front();
        que.pop();
        if (now.h == gh && now.w == gw)
            return now.t;
        if (MAP[now.h][now.w] == '#' || used[now.h][now.w])
            continue;


        used[now.h][now.w] = true;
        if (now.h + 1 < H)
        {
            que.emplace(now.h + 1, now.w, now.t + 1);
        }
        if (now.h - 1 >= 0)
        {
            que.emplace(now.h - 1, now.w, now.t + 1);
        }
        if (now.w + 1 < W)
        {
            que.emplace(now.h, now.w + 1, now.t + 1);
        }
        if (now.w - 1 >= 0)
        {
            que.emplace(now.h, now.w - 1, now.t + 1);
        }
        char c = MAP[now.h][now.w];
        int c_num = c - 'a';
        if (islower(c) && alpabet_char[c_num])
        {

            vector<pair<int, int>> alpa = alpabet[c_num];
            REP(i, alpabet_num[c_num])
            {
                que.emplace(alpa[i].F, alpa[i].S, now.t + 1);
            }
            alpabet_char[c_num] = false;
        }
    }
}
int main()
{
    //小数の桁数の出力指定
    ios::sync_with_stdio(false);

    int H, W, sw, sh, gw, gh;
    cin >> H >> W;
    V<string> MAP;
    string temp;
    V<V<pair<int, int>>> alpabet('z' - 'a' + 1, V<pair<int, int>>());
    V<int> alpabet_num('z' - 'a' + 1, 0);
    V<bool> alpabet_char('z' - 'a' + 1, false);
    REP(h, H)
    {
        cin >> temp;
        REP(w, W)
        {
            if (islower(temp[w]))
            {

                alpabet[temp[w] - 'a'].emplace_back(int(h), int(w));
                alpabet_num[temp[w] - 'a']++;
                alpabet_char[temp[w] - 'a'] = true;
            }
            if (temp[w] == 'S')
            {
                sw = w;
                sh = h;
            }
            if (temp[w] == 'G')
            {
                gw = w;
                gh = h;
            }
        }
        MAP.push_back(temp);
    }

    int ans = (solve(H, W, MAP, gw, gh, sw, sh, 0, alpabet, alpabet_num, alpabet_char));
    cout << ans << endl;
}