//
// Created by puras on 2025/2/14.
//
#include<iostream>
using namespace std;
int main() {
    double sum = 1, k;
    int n = 1;
    cin >> k;

    while (sum <= k) {
        ++n;
        sum += 1.00 / n;
        cout << k << " " << sum << " " << n << endl;
    }

    cout << n;

    return 0;
}