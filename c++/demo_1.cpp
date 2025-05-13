//
// Created by puras on 2025/3/17.
//
#include<iostream>
using namespace std;
int main() {
    int i;
    for (i = 0; i < 100; i++) {
        if (i < 90) {
            continue;
//break;
        }
        cout << i << "\n";
    }
    cout << i;
    return 0;
}