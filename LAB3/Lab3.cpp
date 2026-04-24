#include <iostream>
using namespace std;

void swapValues(int* p1, int* p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

void printArray(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        cout << *(arr + i);
        if (i < size - 1) cout << " ";
    }
    cout << endl;
}

int findMax(int* arr, int size) {
    int max = *arr;
    for (int i = 1; i < size; i++) {
        if (*(arr + i) > max) {
            max = *(arr + i);
        }
    }
    return max;
}

void reverseArray (int* arr, int size) {
    int left = 0;
    int right = size - 1;
    while (left < right) {
        int tmp = *(arr + left);
        *(arr + left) = *(arr + right);
        *(arr + right) = tmp;
        left++;
        right--;
    }
}

int* createArray(int size) {
    int* arr = new int[size];
    return arr;
}

void deleteArray(int* arr) {
    delete[] arr;
    cout << "Memory released successfully." << endl;
}

int main() {
        cout << "Creating dynamic array..." << endl;

        int size;
        cout << "Enter array size: ";
        cin >> size;

        int* arr = createArray(size);

        cout << "Enter values: ";
        for (int i = 0; i < size; i++) {
            cin >> *(arr + i);
        }
        cout << endl;

        cout << "Array elements:" << endl;
        printArray(arr, size);

        cout << endl;

        cout << "Maximum Element: " << findMax(arr, size) << endl;

        cout << "----------------------------------------" << endl;


        cout << "Swapping two numbers" << endl;

        int a = 5, b = 8;
        cout << "Before swap" << endl;
        cout << "a = " << a << endl;
        cout << "b = " << b << endl;

        swapValues(&a, &b);

        cout << "After swap" << endl;
        cout << "a = " << a << endl;
        cout << "b = " << b << endl;

        cout << "----------------------------------------" << endl;


        cout << "Reversing Array..." << endl;
        reverseArray(arr, size);

        cout << "Array after reverse:" << endl;
        printArray(arr, size);

        cout << "----------------------------------------" << endl;


        cout << "Deleting array..." << endl;
        deleteArray(arr);
        arr = nullptr;


    return 0;
}