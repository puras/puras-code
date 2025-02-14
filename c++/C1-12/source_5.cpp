//
// Created by puras on 2025/2/14.
//
#include<iostream>
using namespace std;
int main() {
    int d;
    long long ai = 0;
    long long sum = 0;
    int a1, a2, n;
    cin >> a1 >> a2 >> n;
    d = a2 - a1;
    for (int i = 1; i <= n; i++) {
        ai += d;
        sum += ai;
    }

    cout << sum;
    return 0;
}