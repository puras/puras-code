//
// Created by puras on 2025/7/20.
//
#include<iostream>
using namespace std;
int main() {
    int n, m; // 定义人数和水龙头数
    cin >> n >> m;
    int ar[10000] = {}, mr[100] = {};
    // 每个人接水量初始
    for (int i = 0; i < n; i++) {
        cin >> ar[i];
    }
    // 每个水龙头初始化
    for (int i = 0; i < m; i++) {
        mr[i] = ar[i];
    }
    // 下一个接水的人
    int y = m;
    int flag; // 假设全都接完水啦
    int t = 0; // 接水总时长
    while (1) {
        // 各个水龙头下接水数量减1
        for (int i = 0; i < m; i++) {
            cout << "before mr[" << i << "]" << mr[i] <<endl;
            mr[i]--;
            cout << "after mr[" << i << "]" << mr[i] << endl;
            // 如果接完水，换下一个人，直接N个人都完成
            if (mr[i] == 0 && y < n) {
                mr[i] = ar[y];
                y++; // 下一人索引加1
            }
        }
        t++;
        flag = 1;
        // 检查是否所有人都接完水
        for (int i = 0; i < m; i++) {
            if (mr[i] > 0) {
                flag = 0;
            }
        }

        if (flag) {
            break;
        }
    }
    cout << t;
    return 0;
}