#include <iostream>
using namespace std;

template<typename T>
class Node {
  public:
  T data;
  Node* next;
  Node(T value): data(value), next(nullptr) {};
  Node* getNext() const {return next; }
};


int main() {
  Node<int>* head = new Node<int>(10);
  Node<int>* currentNode = head;
  head->next = new Node<int>(29);
  while( currentNode != nullptr){
    std::cout << currentNode->data << "->";
    currentNode = currentNode->next;
  }
  std::cout << "null" << endl;
}

