//
// Created by puras on 2025/10/19.
//
#include<iostream>
using namespace std;
int main() {
    int y, m, d, sum=0;
    char ch;
    cin >> y >> ch >> m >> ch >> d;
    bool r = y % 4 == 0 && y % 100 != 0 && y % 400 == 0;
    for (int i = 1; i < m; i++) {
        if (i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12) {
            sum += 31;
        } else if (i == 2) {
            if (r) {
                sum += 29;
            } else {
                sum += 28;
            }
        } else {
            sum += 30;
        }
    }
    cout << sum + d;
    return 0;
}