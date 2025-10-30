//
// Created by puras on 2025/10/19.
//
#include<iostream>
using namespace std;
bool isRun(int y) {
    return y % 4 == 0 && y % 100 != 0 || y % 400 == 0;
}
int main() {
    int y1, m1, d1, y2, m2, d2;
    char ch;
    cin >> y1 >> ch >> m1 >> ch >> d1;
    cin >> y2 >> ch >> m2 >> ch >> d2;
    // Y1这一年从1月1日到y1-m1-d1
    int c = 0;
    // y2这一年从1月1日到y2-m2-d2
    int b = 0;
    // y1年到y2-1年，完整年过去的天数
    int a = 0;
    for (int i = 1; i < m1; i++) {
        if (i == 2) {
            if (isRun(y1)) {
                c += 29;
            } else {
                c += 28;
            }
        } else if (i == 4 || i == 6 || i == 9 || i == 11) {
            c += 30;
        } else {
            c += 31;
        }
    }
    c += d1;
    for (int i = 1; i < m2; i++) {
        if (i == 2) {
            if (isRun(y2)) {
                b += 29;
            } else {
                b += 28;
            }
        } else if (i == 4 || i == 6 || i == 9 || i == 11) {
            b += 30;
        } else {
            b += 31;
        }
    }
    b += d2;
    for (int i = y1; i < y2; i++) {
        if (isRun(i)) {
            a += 366;
        } else {
            a += 365;
        }
    }
    cout << a + b - c;
    return 0;
}