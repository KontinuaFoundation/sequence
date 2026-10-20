// array_stack.cpp
// A stack backed by a fixed-size array.
// Compile and run:
// g++ array_stack.cpp -o array_stack
// ./array_stack

#include <iostream>

const int CAPACITY = 5;

struct ArrayStack {
    int data[CAPACITY];
    int top;   // index of the top element; -1 means empty
};

bool isEmpty(const ArrayStack& s) {
    return s.top == -1;
}

bool isFull(const ArrayStack& s) {
    return s.top == CAPACITY - 1;
}

void push(ArrayStack& s, int value) {
    if (isFull(s)) {
        std::cout << "push(" << value << ") failed: stack overflow" << std::endl;
        return;
    }
    s.top++;
    s.data[s.top] = value;
    std::cout << "push(" << value << ") -> data[" << s.top << "] at address "
              << &s.data[s.top] << std::endl;
}

int pop(ArrayStack& s) {
    if (isEmpty(s)) {
        std::cout << "pop() failed: stack underflow" << std::endl;
        return -1;
    }
    int value = s.data[s.top];
    std::cout << "pop() -> data[" << s.top << "] at address "
              << &s.data[s.top] << std::endl;
    s.top--;
    return value;
}

int peek(const ArrayStack& s) {
    return s.data[s.top];
}

int main() {
    ArrayStack s;
    s.top = -1;   // start empty

    std::cout << "Underlying array is contiguous in memory:" << std::endl;
    for (int i = 0; i < CAPACITY; i++) {
        std::cout << "  &data[" << i << "] = " << &s.data[i] << std::endl;
    }
    std::cout << std::endl;

    push(s, 10);
    push(s, 20);
    push(s, 30);

    std::cout << "Top of stack: " << peek(s) << std::endl;

    // Fill the stack past its capacity to see overflow handling.
    push(s, 40);
    push(s, 50);
    push(s, 60);   // stack is full at CAPACITY = 5, this one is rejected

    std::cout << "\nPopping everything:" << std::endl;
    while (!isEmpty(s)) {
        int value = pop(s);
        std::cout << "Popped: " << value << std::endl;
    }

    // One more pop to see underflow handling.
    pop(s);

    return 0;
}
