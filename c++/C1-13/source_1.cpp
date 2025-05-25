//
// Created by puras on 2025/5/18.
//
#include<iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int m = 0; // 存最大小
    int a; // 存每个人的成绩
//    cin >> a;
//    m = a;
    for (int i = 0; i < n; i++) {
        cin >> a;
        if (a > m) {
            m = a;
        }
    }
    cout << m;
}