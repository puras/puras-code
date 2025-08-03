//
// Created by puras on 2025/7/13.
//
// 共n个球，用C表示他们的颜色，问连续k个球里，最多有几种不同的颜色
// 输入2行
// n k
// n个c
// 示例 7 3
//     1 2 1 2 3 3 1
//     3
#include<iostream>
using namespace std;
int main() {
    int ar[100] = {};
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> ar[i];
    }
    int max = 0;

    for (int i = 0; i < n; i++) {
        int r[100] = {};
        for (int j = i; j < i + k && j < n; j++) {
            r[ar[j]]++;
        }
        int num = 0;
        for (int j = 0; j < n; j++) {
            if (r[j] > 0) {
                num++;
            }
        }
        if (num > max) {
            max = num;
        }
    }
    cout << max;

    return 0;
}