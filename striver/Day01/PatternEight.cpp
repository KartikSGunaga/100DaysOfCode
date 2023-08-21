#include<bits/stdc++.h>

using namespace std;

int main(){
    int i, n, j;
    cout<<"Enter the count: ";
    cin>>n;

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= i; j++) {
            cout << " ";
        }
        for (j = 2 * (n - i) + 1; j > 0; j--) {
            cout << "*";
        }
        for (j = 1; j <= i; j++) {
            cout << " ";
        }
        cout << "\n";
    }
}