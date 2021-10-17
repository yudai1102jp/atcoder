#include <iostream>
using namespace std;
int main()
{

    int n;
    bool flag;
    cin >> n;
    int R[n];
    for (int i = 0; i < n; i++)
        cin >> R[i];
    int ans = 0;
    flag = 1;
    while (flag)
    {
        flag = false;
        for (int j = n - 1; j > 0; j--)
        {
            if (R[j] < R[j - 1])
            {
                int temp = R[j];
                R[j] = R[j - 1];
                R[j - 1] = temp;
                flag = 1;
                ans++;
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << R[i];
        if (i == n - 1)
            cout << endl;
        else
            cout << ' ';
    }
    cout << ans << endl;
}