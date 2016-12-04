#include <iostream>

typedef struct node {
    node *prev;
    int   value;
    node *next;
} node;

int main( ) {
    node node1;
    node node2;
    node node3;
    node node4;
    //
    node1.prev = nullptr;
    node1.value = 10;
    node1.next = &node2;
    //
    node2.prev = &node1;
    node2.value = 20;
    node2.next = &node3;
    //
    node3.prev = &node2;
    node3.value = 30;
    node3.next = &node4;
    //
    node4.prev = &node3;
    node4.value = 40;
    node4.next = nullptr;

    node *current = &node1;
    std::cout << "start" << std::endl;
    do
    {
        std::cout << "current value " << current->value << std::endl;
        current = current->next;
    } while (current->next != nullptr);
    std::cout << "current value " << current->value << std::endl;
    std::cout << "end" << std::endl;

    std::cout << "2ndLoop" << std::endl;
    for ( node *current = &node1; current->next != nullptr; current = current->next)
        std::cout << "current value " << current->value << std::endl;
    std::cout << "current value " << current->value << std::endl;
    std::cout << "end" << std::endl;
    return 0;
}