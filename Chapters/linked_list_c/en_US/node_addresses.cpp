// node_addresses.cpp
// Compile and run:
// g++ node_addresses.cpp -o node_addresses
// ./node_addresses

#include <iostream>
#include <cstddef>

struct DoublyNode {
    int data;
    DoublyNode* next;
    DoublyNode* prev;
};

int main() {
    // Create nodes (Doubly Linked)
    DoublyNode* head = new DoublyNode();
    DoublyNode* second = new DoublyNode();
    DoublyNode* third = new DoublyNode();
    DoublyNode* tail = new DoublyNode();

    // Assign data
    head->data = 1;
    second->data = 2;
    third->data = 3;
    tail->data = 4;

    // Link nodes forward
    head->next = second;
    second->next = third;
    third->next = tail;
    tail->next = nullptr;   // tail has no successor

    // Link nodes backward
    head->prev = nullptr;   // head has no predecessor
    second->prev = head;
    third->prev = second;
    tail->prev = third;

    // Print the address of each node, and the addresses stored in its
    // prev/next fields, so you can see both directions of the chain.
    std::cout << "head   is at: " << head   << "   prev: " << head->prev   << " (nullptr)" << "   next: " << head->next   << std::endl;
    std::cout << "second is at: " << second << "   prev: " << second->prev << "   next: " << second->next << std::endl;
    std::cout << "third  is at: " << third  << "   prev: " << third->prev  << "   next: " << third->next  << std::endl;
    std::cout << "tail   is at: " << tail   << "   prev: " << tail->prev   << "   next: " << tail->next   << " (nullptr)" << std::endl;

    // Each DoublyNode takes up a fixed number of bytes in memory -- one
    // more pointer than the singly linked Node, so it's larger.
    std::cout << "\nsizeof(DoublyNode) = " << sizeof(DoublyNode) << " bytes" << std::endl;

    // Pointer subtraction between same-typed pointers gives the distance
    // between them in "how many DoublyNodes apart", not raw bytes. As
    // before, this only measures what actually happened -- new() never
    // guarantees consecutive allocations end up adjacent.
    std::ptrdiff_t nodeSize = static_cast<std::ptrdiff_t>(sizeof(DoublyNode));

    std::ptrdiff_t headToSecond  = second - head;
    std::ptrdiff_t secondToThird = third  - second;
    std::ptrdiff_t thirdToTail   = tail   - third;

    std::cout << "second - head   = " << headToSecond  << " Node-widths (approx. " << headToSecond  * nodeSize << " bytes)" << std::endl;
    std::cout << "third  - second = " << secondToThird << " Node-widths (approx. " << secondToThird * nodeSize << " bytes)" << std::endl;
    std::cout << "tail   - third  = " << thirdToTail   << " Node-widths (approx. " << thirdToTail   * nodeSize << " bytes)" << std::endl;

    // Clean up the memory
    delete head;
    delete second;
    delete third;
    delete tail;

    return 0;
}
