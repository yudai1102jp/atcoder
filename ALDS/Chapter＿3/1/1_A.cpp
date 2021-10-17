#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int R[n + 10];
    int v, j;
    for (int i = 0; i < n; i++)
        cin >> R[i];
    for (int i = 1; i < n; i++)
    {

        for (int i = 0; i < n; i++)
        {
            cout << R[i];
            if (i < n - 1)
                cout << ' ';
            else
                cout << endl;
        }
    
        v = R[i];
        j = i - 1;
        while (j >= 0 && R[j] > v)
        {
            R[j + 1] = R[j];
            j--;
        }
        R[j + 1] = v;
    }

    for (int i = 0; i < n; i++)
    {
        cout << R[i];
        if (i < n - 1)
            cout << ' ';
        else
            cout << endl;
    }
}