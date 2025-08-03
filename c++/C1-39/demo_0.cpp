//
// Created by puras on 2025/8/3.
//
#include<iostream>
using namespace std;

bool isPrime(int n) {
    int f = 1;
    if (n < 2) {
        f = 0;
    } else {
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                f = 0;
                break;
            }
        }
    }
    return f;
}

int sayHello(int n) {
    n = n - 5;
    cout << "num=" << n << endl;
    return n;
}

int main() {
    int n = 10;
    n = sayHello(n);
    cout << "n=" << n << endl;
//    int n;
//    cin >> n;
//    int f = isPrime(n);
//    if (f) {
//        cout << "yes";
//    } else {
//        cout << "no";
//    }
    return 0;
}