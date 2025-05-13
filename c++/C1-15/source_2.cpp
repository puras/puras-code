//
// Created by puras on 2025/4/13.
//
#include<iostream>
using namespace std;

int main() {
    int n;
    int i;
    for (i = 0; i < 10; i++) {
        cin >> n;
        if (n == 3) {
            break;
        }
    }

    if (i == 10) {
        cout << "No";
    } else {
        cout << (i + 1);
    }

    return 0;
}