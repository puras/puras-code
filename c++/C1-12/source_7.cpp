//
// Created by puras on 2025/2/14.
//
#include<iostream>
using namespace std;
int main() {
    int n, a_pre, a_des;
    cin >> n;
    cin >> a_pre >> a_des;
    int d = a_des - a_pre;
    int i;
    for (i = 3; i <= n; i++) {
        a_pre = a_des;
        cin >> a_des;
        if (a_des != a_pre + d) {
            cout << "False";
            break;
        }
    }
    if (i == n + 1) {
        cout << "True";
    }
    return 0;
}