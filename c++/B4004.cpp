//
// Created by puras on 2025/10/26.
//
#include<iostream>
using namespace std;
int main() {
    int t;
    cin >> t;
    for (int z = 0; z < t; z++) {
        int n;
        cin >> n;
        int A[10000] = {};
        for (int i = 1; i <= n; i++) {
            cin >> A[i];
        }
        int ret = 0, flag;
        for (int i = 1; i <= n; i++) {
            flag = 1;
            for (int k = 1; k <= n; k++) {
                if (A[i] % A[k] != 0) {
                    flag = 0;
                    break;
                }
            }
            if (flag == 1) {
                ret = 1;
                break;
            }
        }
        if (ret) {
            cout << "Yes";
        } else {
            cout << "No";
        }
        cout << endl;
        n--;
    }
    return 0;
}