//
// Created by puras on 2025/7/27.
//
#include<iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int flag = 1;
    if (n <= 1) {
        flag = 0;
    } else if (n == 2) {
        flag = 1;
    } else {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                flag = 0;
                break;
            }
        }
    }
    if (flag) {
        cout << "yes";
    } else {
        cout << "no";
    }
    return 0;
}