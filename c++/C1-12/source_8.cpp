//
// Created by puras on 2025/2/14.
//
#include<iostream>
using namespace std;
int main() {
    int n;
    float q, a = 1, sum = 1;
    cin >> q >> n;
    for (int i = 0; i < n; i++) {
        a = a * q;
        sum += a;
    }
    cout << sum;
    return 0;
}