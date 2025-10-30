//
// Created by puras on 2025/8/24.
//
#include<iostream>
using namespace std;
int main() {
//    int n = 1;
//    int i = 1;
//    while (n < 100) {
//        cout << n << " ";
//        if (i % 5 == 0) {
//            cout << "\n";
//        }
//        n = n + i;
//        i++;
//    }
    for (int i = 1, n = 1; n < 100; n = n + i, i++) {
        cout << n << " ";
    }
}