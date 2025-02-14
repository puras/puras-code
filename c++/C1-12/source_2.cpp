//
// Created by puras on 2025/2/14.
//
#include<iostream>

using namespace std;

int main() {
    int n;
    int ret = 1;
//    long long ret = 1;
    cin >> n;
    for (int i = n; i > 0; i--) {
        ret *= i;
    }
    cout << ret;

    return 0;
}