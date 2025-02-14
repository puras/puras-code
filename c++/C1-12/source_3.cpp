//
// Created by puras on 2025/2/14.
//
#include<iostream>
using namespace std;

int main() {
    long long r = 1;
    int n;
    cin >> n;
    cout << n << "!=";
    for (int i = 1; i <= n; i++) {
        if (i < n) {
            cout << i << "*";
        } else if (i == n && i != 1) {
            cout << i << "=";
        }
        r *= i;
    }

    cout << r << endl;

    return 0;
}