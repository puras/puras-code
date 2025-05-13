//
// Created by puras on 2025/4/20.
//
#include<iostream>
using namespace std;
int main() {
    int n, tmp, c=0, sum=0;
    cin >> n;
    tmp = n;
    while (tmp != 0) {
        tmp /= 10;
        c++;
    }
    tmp = n;
    int a;
    while (tmp != 0) {
        a = tmp % 10;
        int sa = 1;
        for (int i = 0; i < c; i++) {
            sa *= a;
        }
        sum += sa;
        tmp /= 10;
    }
    if (sum == n) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }

    return 0;
}