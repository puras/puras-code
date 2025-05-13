//
// Created by puras on 25-5-11.
//
#include<iostream>
using namespace std;

int main() {
    int n, sum = 0;
    int d;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> d;
        sum += d;
    }
    cout << sum / n << endl;
    printf("%.2f", sum * 1.0 / n);
}