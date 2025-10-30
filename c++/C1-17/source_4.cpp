//
// Created by puras on 2025/5/25.
//
#include<iostream>
using namespace std;
int main() {
    int h1, m1, s1, h2, m2, s2;
    char ch;
    int flag = 1;
    int flag1 = 0;
    cin >> h1 >> ch >> m1 >> ch >> s1;
    cin >> h2 >> ch >> m2 >> ch >> s2;
    for (int i = 0; i < 24 && flag; i++) {
        for (int j = 0; j < 60 && flag; j++) {
            for (int k = 0; k < 60; k++) {
                if (i == h1 && j == m1 && k == s1) {
                    flag1 = 1;
                }
                if (flag1 == 1) {
                    printf("%02d:%02d:%02d\n", i, j, k);
                }

                if (i == h2 && j == m2 && k == s2) {
                    flag = 0;
                    break;
                }
            }
        }
    }
}