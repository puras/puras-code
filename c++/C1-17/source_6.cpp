//
// Created by puras on 2025/5/29.
//
#include<iostream>
using namespace std;
int main() {
    for (int i = 1; i <= 20; i++) {
        for (int j = 1; j <= 33; j++) {
            int z = 100 - i - j;
            if (z % 3 == 0 && 5 * i + 3 * j + z / 3 == 100) {
                cout << i << " " << j << " " << z << endl;
            }
        }
    }
    return 0;
}