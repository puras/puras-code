//
// Created by puras on 2025/7/13.
//
#include<iostream>
using namespace std;
int main() {
    int a[105];
    int n;
    cin >> n;

    for (int i = 1; i <= 100; i++) {
        a[i] = i;
    }
    for (int i = 1; i <= n; i++) {
        int x, y;
        cin >> x >> y;
        a[x] = y;
    }
    int s1 = 0;
    int s2 = 0;
    for (int i = 1; i != a[i]; i = a[i]) {
        cout << "i=" << i << "-" << a[i] << endl;
        s1++;
    }
    for (int i = 2; i != a[i]; i = a[i]) {
        cout << "i=" << i << "-" << a[i] << endl;
        s2++;
    }
    cout << s1 << endl;
    cout << s2 << endl;

    return 0;
}