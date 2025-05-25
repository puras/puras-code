//
// Created by puras on 2025/5/18.
//
#include<iostream>
using  namespace std;

int main() {
    bool flag = 0;
    for (int n1 = 0; n1 <= 9; n1++) {
        for (int n2 = 0; n2 <= 9; n2++) {
            for (int n3 = 0; n3 <= 9; n3++) {
                if (n1 + n2 + n3 == 19 &&
                n2 + 1 == n1 + n3 &&
                n1 * 1.5 == n3) {
                    cout << n1 << " " << n2 << " " << n3 << "\n";
                    flag = 1;
                    break;
                }
            }
            if (flag == 1) {
                break;
            }
        }

        if (flag == 1) {
            break;
        }
    }
    return 0;
}