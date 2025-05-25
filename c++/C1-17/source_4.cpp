//
// Created by puras on 2025/5/25.
//
#include<iostream>
using namespace std;
int main() {
    int h1, m1, s1, h2, m2, s2;
    char ch;
    cin >> h1 >> ch >> m1 >> ch >>s1;
    cin >> h2 >> ch >> m2 >> ch >>s2;
    int flag_s = 0, flag_e = 1;
    for (int h = 0; h < 24 && flag_e == 1; h++) {
        for (int m = 0; m < 60 && flag_e == 1; m++) {
            for (int s = 0; s < 60; s++) {
                if (h1 == h && m1 == m && s1 == s) {
                    flag_s = 1;
                }

                if (flag_s == 1) {
                    printf("%02d:%02d:%02d\n", h, m, s);
                }

                if (h2 == h && m2 == m && s2 == s) {
                    flag_e = 0;
                    break;
                }
            }
        }
    }
}