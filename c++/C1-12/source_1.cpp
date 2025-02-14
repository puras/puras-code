//
// Created by puras on 2025/2/14.
//
#include<iostream>

using namespace std;

int main() {
    int cnt = 0;
    float t;
    for (int i = 0; i < 10; i++) {
        cin >> t;
        if (t > 20) {
            cnt++;
        }
    }

    cout << cnt;

    return 0;
}