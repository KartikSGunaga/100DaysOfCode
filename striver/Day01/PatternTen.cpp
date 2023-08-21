#include <iostream>
using namespace std;

int main() {
    int i, j, num, n;

    cout << "Enter the count: ";
    cin >> n;

    for (i = 0; i <= n; i++) {
        cout << "\n";
        
        if (i % 2 == 0) {
            num = 0;
        }
        if (i % 2 != 0) {
            num = 1;
        }
        
        for (j = 0; j < i; j++) {
            cout << num;
            num = 1 - num;  // Toggle between 0 and 1
        }

        for (j = n - i; j > 0; j--) {
            cout << " ";
        }
    }
    return 0;
}
