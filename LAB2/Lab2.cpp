#include <iostream>
using namespace std;

int main() {



    int fb_n;
    do {
        cout << "Please enter a number between 10 and 100: ";
        cin >> fb_n;
        if (fb_n < 10 || fb_n > 100) cout << "Invalid input." << endl;
    } while (fb_n < 10 || fb_n > 100);

    int fizz = 0, buzz = 0, fizzbuzz = 0;
    for (int i = 1; i <= fb_n; i++) {
        if (i % 7 == 0)
            continue;
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzbuzz++;
        } else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizz++;
        } else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzz++;
        } else {
            cout << i << endl;
        }
    }
    cout << "Summary\nFizz count: " << fizz << "\nBuzz count: " << buzz << "\nFizzBuzz count: " << fizzbuzz << endl;


}