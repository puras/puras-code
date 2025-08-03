//
// Created by puras on 2025/6/15.
//
#include<iostream>
using namespace std;
int main() {
    int num, d;
    cin >> num;
//    if (num == 0) {
//        cout << num << endl;
//    } else
    if (num < 0) {
        num = num * -1;
    }
    while (1) {
        d = num % 10;
        cout << d << endl;
        num = num / 10;
        if (num == 0) {
            break;
        }
    }
    return 0;
}