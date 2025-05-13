//
// Created by puras on 2025/2/14.
//
#include<iostream>
using namespace std;
int main() {
    int d, a1, a2, n, sum = 0;
    cin >> a1 >> a2 >> n;
    d = a2 - a1;
    sum = a1 + a2;
    for (int i = 3; i <= n; i++) {
        a2 = a2 + d;
        sum += a2;
    }
    cout << sum;
    return 0;
}