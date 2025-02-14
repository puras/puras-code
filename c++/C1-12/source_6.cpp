//
// Created by puras on 2025/2/14.
//
#include<iostream>
using namespace std;
int main() {
    long long an = 0;
    long long sum = 0;
    int a1, a2, n, d;
    cin >> a1 >> a2 >> n;
    d = a2 - a1;
    an = a1 + (n - 1) * d;
    sum = (a1 + an) * n / 2;
    // 公式 Sn = (a1 + an) x n / 2
    cout << sum;
    return 0;
}