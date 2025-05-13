//
// Created by puras on 2025/3/16.
//
#include<iostream>
using namespace std;
int main() {
    int n, x, y, m;
    cin >> n >> x >> y;
    if (y % x == 0) {
        m = y / x;
    } else {
        m = y / x + 1;
    }

    if (n - m > 0) {
        cout << n - m;
    } else {
        cout << "0";
    }
}