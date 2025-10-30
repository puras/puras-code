//
// Created by puras on 2025/8/17.
//
#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
int main() {
    srand((unsigned) time(0));
    int num = rand();
    cout << num << endl;
    num = rand();
    cout << num << endl;
    num = rand();
    cout << num << endl;
    return 0;
}