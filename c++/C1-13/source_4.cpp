//
// Created by puras on 2025/5/25.
//
#include<iostream>
using namespace std;
int main() {
    int n, t, max, min;
    cin >> n;
    cin >> t;
    max = t;
    min = t;
    for (int i = 0; i < n - 1; i++) {
        cin >> t;
        if (t > max) {
            max = t;
        } else if (t < min) {
            min = t;
        }
    }
    cout << max - min << endl;
    return 0;
}