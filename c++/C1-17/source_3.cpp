//
// Created by puras on 2025/5/18.
//
#include<iostream>
using namespace std;
int main() {
    int h, m, s;
    char ch;
    cin >> h >> ch >> m >> ch >> s;
    for (int i = 0; i <= h; i++) {
        for (int j = 0; j < 60; j++) {
            for (int z = 0; z < 60; z++) {
                cout << i << ":" << j << ":" << z << endl;
                if (i == h && j == m && z == s) {
                    return 0;
                }
            }
        }
    }
}