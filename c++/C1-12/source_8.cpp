//
// Created by puras on 2025/2/14.
//
#include<iostream>
using namespace std;
int main() {
    float q, ai = 1, sum = 1;
    int n;
    cin >> q >> n;
    for (int i = 1; i <= n; i++) {
        ai *= q;
        sum += ai;
    }
    cout << sum;
    return 0;
}