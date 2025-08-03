//
// Created by puras on 2025/4/13.
//
#include<iostream>
using namespace std;
int main() {
    char ch;
    int sum = 0;
    while (true) {
        cin >> ch;
        if (ch == '@') {
            break;
        }
        if (ch >= '0' && ch <= '9') {
            sum += (ch - '0');
        }
    }
    cout << sum;
    return 0;
}