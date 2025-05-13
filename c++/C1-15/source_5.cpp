//
// Created by puras on 2025/4/13.
//
#include<iostream>
using namespace std;
int main() {
    int num;

    cin >> num;

    int tmp, cnt = 0, sum = 0;
    for (int i = 1; i <= num; i++) {
//        cout << i << endl;
        tmp = i;
        while (tmp != 0) {
            tmp /= 10;
            cnt++;
        }
        tmp = i;
        int a;
        while (tmp != 0) {
            a = tmp % 10;
//            cout << a << " " << cnt;
            int sa = 1;
            for (int j = 0; j < cnt; j++) {
                sa *= a;
            }
//            cout << " " << sa << endl;
            sum += sa;
            tmp /= 10;
        }
        if (sum == i) {
            cout << i << " " << "yes" << endl;
        } else {
//            cout << i << "no" << endl;
        }
        cnt = 0;
        sum = 0;
    }

    return 0;
}