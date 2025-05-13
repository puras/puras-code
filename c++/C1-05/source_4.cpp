//
// Created by puras on 2025/2/23.
//
#include<iostream>
using namespace std;
int main() {
    int sc;
    cin >> sc;
    if (sc <= 6 || sc >= 60) {
        cout << 25;
    } else {
        cout << 50;
    }
    return 0;
}