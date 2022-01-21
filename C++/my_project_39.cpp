#include <iostream>
using namespace std;
int main() {
    double a, b;
    char op;
    cout << "Enter first number: ";
    cin >> a;
    cout << "Enter operator (+, -, *, /): ";
    cin >> op;
    cout << "Enter second number: ";
    cin >> b;
    switch(op) {
        case '+': cout << "Result: " << a + b; break;
        case '-': cout << "Result: " << a - b; break;
        case '*': cout << "Result: " << a * b; break;
        case '/': cout << (b != 0 ? a / b : 0); break;
        default: cout << "Invalid operator!";
    }
    return 0;
}