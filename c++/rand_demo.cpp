//
// Created by puras on 2025/8/17.
//
#include<iostream>
#include<cstdlib>

using namespace std;

int rand_num(int a, int b) {
    srand((unsigned) time(0));
    int num = rand() % (b - a + 1) + a;
    return num;
}

int main() {
    cout << time(0) << endl;
    int num = rand_num(100, 1000);
    cout << num << endl;
}