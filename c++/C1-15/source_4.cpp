//
// Created by puras on 2025/4/20.
//
#include<iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int flag = 1;
    int a = 0;
    int tmp = n;
    while (tmp > 0) {
        tmp /= 10;
        a++;
    }

    tmp = n;
    int d;
    int r = 0;
    while (tmp > 0) {
        d = tmp % 10;
        tmp = tmp / 10;
        int s = 1;
        cout << "d=" << d << endl;
        for (int i = 0; i < a; i++) {
            s *= d;
        }
        r = r + s;
        cout << "s=" << s << endl;
    }
    cout << "r=" << r << endl;

    flag = r == n;
    if (flag) {
        cout << "yes";
    } else {
        cout << "no";
    }

    return 0;
}