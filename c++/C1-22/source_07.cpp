//
// Created by puras on 2025/10/8.
//
#include<iostream>
using namespace std;
int main() {
    int n, k = 2;
    cin >> n;
    cout << n << "=";
    while (n != 1) {
        if (n % k == 0) {
            cout << k;
            if (n / k != 1) {
                cout << "*";
            }
            n = n / k;
        } else {
            k = k + 1;
        }
    }

    return 0;
}