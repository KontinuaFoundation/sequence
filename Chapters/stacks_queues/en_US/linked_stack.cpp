// linked_stack.cpp
// A stack backed by a singly linked list -- no fixed capacity.
// Compile and run:
// g++ linked_stack.cpp -o linked_stack
// ./linked_stack

#include <iostream>

struct Node {
    int data;
    Node* next;
};

struct LinkedStack {
    Node* top;   // nullptr means empty
};

bool isEmpty(const LinkedStack& s) {
    return s.top == nullptr;
}

void push(LinkedStack& s, int value) {
    Node* n = new Node();
    n->data = value;
    n->next = s.top;   // the new node points at the old top
    s.top = n;          // the new node becomes the top
}

int pop(LinkedStack& s) {
    if (isEmpty(s)) {
        std::cout << "pop() failed: stack underflow" << std::endl;
        return -1;
    }
    Node* oldTop = s.top;
    int value = oldTop->data;
    s.top = oldTop->next;
    delete oldTop;
    return value;
}

int peek(const LinkedStack& s) {
    return s.top->data;
}

int main() {
    LinkedStack s;
    s.top = nullptr;   // start empty

    push(s, 10);
    push(s, 20);
    push(s, 30);

    std::cout << "Top of stack: " << peek(s) << std::endl;

    // Able to keep pushing, no capacity
    push(s, 40);
    push(s, 50);
    push(s, 60);

    std::cout << "\nPopping everything:" << std::endl;
    while (!isEmpty(s)) {
        std::cout << "Popped: " << pop(s) << std::endl;
    }

    // One more pop to see underflow handling.
    pop(s);

    return 0;
}
