//
// Created by puras on 2025/3/16.
//
#include<iostream>
using namespace std;

int main() {
    int num1, num2, num3;
    cin >> num1 >> num2 >> num3;
    int max;
    if (num1 > num2) {
        max = num1;
    } else {
        max = num2;
    }
    if (num3 > max) {
        max = num3;
    }
//    int max = num1;
//    if (num2 > max) {
//        max = num2;
//    }
//    if (num3 > max) {
//        max = num3;
//    }

    cout << max * max << endl;
    return 0;
}