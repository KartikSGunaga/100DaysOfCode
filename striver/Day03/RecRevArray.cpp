#include <iostream>
using namespace std;

void revArray(int arr[], int start, int end) {
    if (start >= end) {
        return;
    }
    int temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;

    revArray(arr, start + 1, end - 1);
}

int main() {
    int arr[100], num, i;

    cout << "Enter the array length: ";
    cin >> num;

    cout << "Enter the array elements: ";
    for (i = 0; i < num; i++) {
        cin >> arr[i];
    }

    revArray(arr, 0, num - 1);

    cout << "\nReversed array: ";
    for (i = 0; i < num; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
