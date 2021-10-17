#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#define repeat(i, n) for (int i = 0; (i) < (n); ++(i))
#define repeat_from(i, m, n) for (int i = (m); (i) < (n); ++(i))
using namespace std;
double sq(double x) { return x * x; }
int main()
{
    int k;
    cin >> k;
    vector<int> a(k);

    vector<double> p(k);
    repeat(i, k) p[i] = 1 / k;
    vector<double> dp(1 << k);
    repeat_from(s, 1, 1 << k)
    {
        double p_s = 0;
        repeat(i, k) if (s & (1 << i))
        {
            p_s += p[i];
        }
        dp[s] += 1 / p_s;
        repeat(i, k) if (s & (1 << i))
        {
            int t = s & ~(1 << i);
            dp[s] += (p[i] / p_s) * dp[t];
        }
    }
    // output
    printf("%.12lf\n", dp[(1 << k) - 1]);
    return 0;
}