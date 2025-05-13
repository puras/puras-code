//
// Created by puras on 2025/4/13.
//
#include<iostream>
using namespace std;
int main() {
    int sum = 0;
    char ch;
    while (ch != '@') {
        cin >> ch;
        if (ch >= '0' && ch <= '9') {
            sum += ch - '0';
        }
    }
    cout << sum;
    return 0;
}