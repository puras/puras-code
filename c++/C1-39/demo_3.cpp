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
            int t = j;
            int d, fj = 0;
            while (t > 0) {
                d = t % 10;
                t = t / 10;
                fj = fj * 10 + d;
            }
            int flag = 1;
            if (fj <= 1) {
                flag = 0;
            } else if (fj == 2) {
                flag = 1;
            } else {
                for (int i = 2; i * i <= fj; i++) {
                    if (fj % i == 0) {
                        flag = 0;
                        break;
                    }
                }
            }
            if (flag) {
                cout << j << " ";
            }
        }
    }
    return 0;
}