//
// Created by puras on 2025/5/4.
//
#include<iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int c = 0;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            c++;
        }
    }
    cout << c << endl;
    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            cout << i << " ";
        }
    }
}