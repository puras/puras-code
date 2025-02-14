//
// Created by puras on 2025/2/14.
//
#include<iostream>
using namespace std;
int main() {
    double sum = 3, q, ai = 3;
    int n = 1;
    cin >> q;
    while (sum < 100) {
        ai *= q;
        sum += ai;
        n++;
        cout << ai << " " << sum << " " << n << endl;
    }
    cout << n - 1;
    return 0;
}