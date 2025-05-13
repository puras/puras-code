//
// Created by puras on 2025/3/15.
//
#include<iostream>
using namespace std;

int main() {
    int max_1 = 0;
    int max_2 = 0;
    int tmp;
    int n ;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        if (tmp > max_1) {
            max_2 = max_1;
            max_1 = tmp;
        } else {
            if (tmp > max_2 && tmp != max_1) {
                max_2 = tmp;
            }
        }
    }
    cout << max_2;
    return 0;
}