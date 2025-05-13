//
// Created by puras on 2025/5/4.
//
#include<iostream>

using namespace std;
int main() {
    int n;
    cin >> n;
    int c = 0;
    int cnt = 0;
    for (int i = 1; i <= n; i++) {
        cnt++;
        if (n % i == 0) {
            c++;
        }
        if (c == 3) {
            break;
        }
    }

    if (c == 2) {
        cout << "prime";
    } else {
        cout << "No";
    }
    cout << "\n" << cnt;
//    int cnt = 0;
//    for (int i = 1; i <= n; i++) {
//        if (n % i == 0) {
//            cnt++;
//        }
//        if (cnt == 3) {
//            break;
//        }
//    }
//    if (cnt == 3 && n != 1) {
//        cout << "No";
//    } else {
//        cout << "prime";
//    }
}