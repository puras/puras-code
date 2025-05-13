//
// Created by puras on 2025/5/4.
//
#include<iostream>

using namespace std;
int main() {
    int n;
    cin >> n;
    int flag = 1;
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            flag = 0;
            break;
        }
    }
    if (flag == 1 && n != 1) {
        cout << "prime";
    } else {
        cout << "No";
    }
}