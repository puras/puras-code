//
// Created by puras on 2025/2/24.
//
#include<iostream>
using namespace  std;

int main() {
    int y, k, n;
    int j = 0;
    cin >> y >> k >> n;
    for (int i = 1; i * k <= n; i++) {
        if (k * i >= y) {
            cout << i * k - y << " ";
            j++;
        }
    }

    if (j == 0) {
        cout << -1;
    }

    return 0;
}