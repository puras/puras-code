//
// Created by puras on 25-5-11.
//
#include<iostream>
using namespace std;
int main() {
    int n, cnt = 0;
    cin >> n;

    int d = 2;
    bool flag = 1;
    while (cnt != n) {
//        cout << d;
        flag = 1;
        if (d == 2) {
            flag = 1;
        } else if (d % 2 == 0) {
            flag = 0;
        } else {
            for (int i = 2; i < d; i++) {
                if (d % i == 0) {
                    flag = 0;
                    break;
                }
            }
        }

        if (flag == 1) {
            cnt++;
        }
        d++;
    }
    cout << --d;
    return 0;
}