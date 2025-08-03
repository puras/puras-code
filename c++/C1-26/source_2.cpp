//
// Created by puras on 2025/7/13.
//
#include<iostream>
using namespace std;
int main() {
    int ar[4] = {}, n, d;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> d;
        if (d < 60) {
            ar[d / 20]++;
        } else {
            ar[3]++;
        }
    }

    for (int i = 0; i < 4; i++) {
        printf("%.2f%%\n", ar[i] * 1.0 / n * 100);
    }
    return 0;
}