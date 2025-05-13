//
// Created by puras on 2025/3/16.
//
#include<iostream>
using namespace std;
int main() {
    int num;
    cin >> num;
    float m = num * 95;

    if (m >= 300) {
        m = m * 0.85;
    }

    printf("%.2f", m);
}