//
// Created by puras on 2025/5/4.
//
#include<iostream>

using namespace std;
int main() {
    int n, c=0;
    cin >> n;
    for (int i = 2; i <= n; i++) {
//        cout << i << " ";
        int cnt = 0;
        for (int j = 1; j <= i; j++) {
            if (i % j == 0) {
                cnt++;
            }
            if (cnt > 2) {
                break;
            }
        }
        if (cnt == 2) {
            cout << i << " ";
            c++;

            if (c % 5 == 0) {
                cout << endl;
            }
        }
    }
    cout << "\n" << c;
    return 0;
}