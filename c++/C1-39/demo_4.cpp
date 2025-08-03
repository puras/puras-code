//
// Created by puras on 2025/7/27.
//
#include<iostream>
using namespace std;
bool isPrime(int n) {
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
    return flag;
}
int reverseNumber(int n) {
    int d, fj = 0;
    while (n > 0) {
        d = n % 10;
        n = n / 10;
        fj = fj * 10 + d;
    }
    return fj;
}

int main() {
    int n, m;
    cin >> n >> m;
    for (int j = n; j <= m; j++) {
        if (isPrime(j) && isPrime(reverseNumber(j))) {
            cout << j << " ";
        }
    }
    return 0;
}