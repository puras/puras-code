//
// Created by puras on 2025/6/22.
//
#include<iostream>
using namespace std;

int main() {
    int num;
    cin >> num;
    int d, nn = 0, k = 1;
    while(num != 0) {
        d = num % 10;
        num = num / 10;
        if (d != 0) {
            cout << d << endl;
            nn = nn + d * k;
            k *= 10;
        }
    }

    cout << nn;

    return 0;
}