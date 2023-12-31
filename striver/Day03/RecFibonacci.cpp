

#include <iostream>
using namespace std;

int fibonacci(int num) {
    if (num == 0 || num == 1) {
        return num;
    }
    return fibonacci(num - 1) + fibonacci(num - 2);
}

int main() {
    int num;

    cout << "Enter the range: ";
    cin >> num;

    cout << "Fibonacci sequence for range " << num << ": ";
    for (int i = 0; i < num; i++) {
        cout << fibonacci(i) << " ";
    }

    return 0;
}
