//
// Created by puras on 2025/2/14.
//
#include<iostream>

using namespace std;

int main() {
    float temp;
    int cnt = 0; // 存满足条件的个数

    for (int i = 0; i < 10; i++) {
        cin >> temp;
        if (temp > 20) {
            cnt++;
        }
    }

    cout << cnt;

    return 0;
}