//
// Created by puras on 2025/7/13.
//
#include<iostream>
using namespace std;
int main() {
    int w[10001], ar[101];
    int n, m, i, k, j, max;
    cin >> n >> m;
    for (i = 1; i <= n; i++) {
        cin >> w[i];
    }
    for (i = 1; i <= n; i++) {
        ar[i] = w[i];
    }
    for (i = m + 1; i <= n; i++) {
        cout << "i=" << i << endl;
        k = 1;
        for (j = 2; j <= m; j++) {
            cout << "j=" << j << endl;
            if (ar[j] < ar[k]) {
                k = j;
            }
        }
        ar[k] = ar[k] + w[i];
    }
    max = 0;
    for (i = 1; i <= m; i++) {
        if (ar[i] > max) {
            max = ar[i];
        }
    }
    cout << max;
    return 0;
}