//
// Created by puras on 2025/10/19.
//
#include<iostream>
using namespace std;
bool isRun(int y) {
    return y % 4 == 0 && y % 100 != 0 && y % 400 == 0;
}
int main() {
    int y1, y2, m2, d2, s = 0;
    char ch;
    cin >> y2 >> ch >> m2 >> ch >> d2;
    cin >> y1;
    for (int i = y1; i < y2; i++) {
        if (isRun(i)) {
            s += 366;
        } else {
            s += 365;
        }
    }
    for (int i = 1; i < m2; i++) {
        if (i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12) {
            s += 31;
        } else if (i == 2) {
            if (isRun(y1)) {
                s += 29;
            } else {
                s += 28;
            }
        } else {
            s += 30;
        }
    }
    s += d2;

    cout << s;
    return 0;
}