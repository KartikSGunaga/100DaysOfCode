#include <iostream>
using namespace std;

int main() {
    int n, i, j;

    cout << "Enter the count: ";
    cin >> n;

    // Upper half of the diamond
    for (i = 0; i <= n / 2; i++) {
        cout << "\n";
        for (j = 0; j <= i; j++) {
            cout << "*";
        }
        for (j = i + 1; j < (n + 1) / 2; j++) {
            cout << " ";
        }
    }

    // Lower half of the diamond
    for (i = (n / 2) - 1; i >= 0; i--) {
        cout << "\n";
        for (j = 0; j <= i; j++) {
            cout << "*";
        }
        for (j = i + 1; j < (n + 1) / 2; j++) {
            cout << " ";
        }
    }

    return 0;
}
