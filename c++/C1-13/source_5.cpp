//
// Created by puras on 2025/5/25.
//
#include<iostream>
using namespace std;
int main() {
    int n, t, max, max_i, min, min_i;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> t;
        if (i == 1) {
            max = t;
            max_i = 1;
            min = t;
            min_i = 1;
        } else if (t > max) {
            max = t;
            max_i = i;
        } else if (t < min) {
            min = t;
            min_i = i;
        }
    }
    cout << max_i << " " << min_i << endl;
    return 0;
}