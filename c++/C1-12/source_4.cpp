//
// Created by puras on 2025/2/14.
//
#include<iostream>
using namespace std;
int main() {
    long long ans = 1;
    for (int i = 1; i <= 1992; i++) {
        ans = (ans * 1992) % 100;
        cout << "*" << ans << endl;
    }
    cout << ans << endl;
    return 0;
}