//
// Created by puras on 2025/5/25.
//
#include<iostream>
using namespace std;
int main() {
    for (int i = 1; i <= 9; i++) {
        for (int j = 1; j <= i; j++) {
            cout << i << "*" << j << "=" << i * j << " ";
        }
        cout  << endl;
    }
    return 0;
}