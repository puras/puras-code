//
// Created by puras on 2025/3/2.
//
#include<iostream>
using namespace std;

int main() {
    int x = 5;
    if (x % 2 != 0) {
        cout << "A ";
    }
    if (x < 4) {
        cout << "B ";
    }
    if (x != 6) {
        cout << "C ";
    }
    if (x % 3 == 0) {
        cout << "D ";
    }
    if (8 % x == 0) {
        cout << "E ";
    }
    if (5 <= x && x <= 10) {
        cout << "F ";
    }
    return 0;
}