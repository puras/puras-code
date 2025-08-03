//
// Created by puras on 2025/6/15.
//
#include<iostream>
using namespace std;
int main() {
    int num1, num2, tmp = 1;
    cin >> num1 >> num2;
    for (int i = 1; i <= num2; i++) {
        cout << i << endl;
        if (num1 % i == 0 && num2 % i == 0) {
            tmp = i;
        }
    }
    cout << tmp;
    return 0;
}