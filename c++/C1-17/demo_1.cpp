//
// Created by puras on 2025/9/7.
//
#include<iostream>
using namespace std;
int main() {
    for (int a = 0; a <= 9; a++) {
//        cout << "a-->" << a << "\n";
        for (int b = 0; b <= 9; b++) {
//            cout << "b--->" << b << "\n";
            for (int c = 0; c <= 9; c++) {
//                cout << "c---->" << c << "\n";
                cout << "a=" << a << ",b=" << b << ",c=" << c << endl;
            }
        }
    }
    return 0;
}