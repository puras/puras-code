//
// Created by puras on 2025/7/27.
//
#include<iostream>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    for (int j = n; j <= m; j++) {
        int flag = 1;
        if (j <= 1) {
            flag = 0;
        } else if (j == 2) {
            flag = 1;
        } else {
            for (int i = 2; i * i <= j; i++) {
                if (j % i == 0) {
                    flag = 0;
                    break;
                }
            }
        }
        if (flag) {
            cout << j << " ";
        }
    }
    return 0;
}