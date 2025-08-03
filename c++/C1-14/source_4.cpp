//
// Created by puras on 2025/7/20.
//
#include<iostream>
using namespace std;
int main() {
    int num, n=0;
    cin >> num;
    int d, f = 1;
    while (num > 0) {
        d = num % 10;
        num = num / 10;

        n = n * 10 + d;

//        if (d != 0) {
//            cout << d;
//        } else {
//            if (f != 1) {
//                cout << d;
//            }
//        }
//
//        if (!(d == 0 && f == 1)) {
//            f++;
//        }
    }
    cout << n;
    return 0;
}