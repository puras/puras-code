//
// Created by puras on 2025/7/20.
//
#include<iostream>
using namespace std;
int main() {
    int ar[100] = {}, n;
    cin >> n;
    bool f = true;
    // 输入数组数据
    for (int i = 0; i < n; i++) {
        cin >> ar[i];
    }

    // 判断数组数据是否是回文
    int j = n - 1;
    for (int i = 0; i < n / 2; i++) {
        if (ar[i] != ar[j]) {
            f = false;
            break;
        }
        j--;
    }
    if (f) {
        cout << "yes";
    } else {
        cout << "no";
    }

    return 0;
}