//
// Created by puras on 2025/4/13.
//
#include<iostream>
using namespace std;
int main() {
    int n, s=0;
    cin >> n;
    int i = 1;
//    while (n > 0) {
//        s += n; //  s = s + n
//        n--;
//    }
    while (i <= n) {
        s += i;
        i++;
    }
    cout << s;
    return 0;
}