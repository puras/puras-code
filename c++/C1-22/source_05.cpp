//
// Created by puras on 2025/10/8.
//
#include<iostream>
using namespace std;
int main() {
    int n = 12, arr[20] = {1, 1};
    for (int i = 2; i < n; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    cout << arr[n - 1];
//    int n1 = 1, n2 = 1, n3, n;
//    cin >> n;
//    if (n < 3) {
//        cout << 1;
//    } else {
//        for (int i = 3; i <= n; i++) {
//            n3 = n1 + n2;
//            n1 = n2;
//            n2 = n3;
//        }
//        cout << n3;
//    }
    return 0;
}