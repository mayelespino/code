#include <iostream>
using namespace  std;

template <typename T>
class node {
    T data;
    node<T> *left;
    node<T> *right;
public:
    ~node();
    node(T iData);
    void setLeft(node<T> *iLeft);
    void setRight(node<T> *iRight);
    T getData(void);
    node<T>* getLeft(void);
    node<T>* getRight(void);
    void addNode(T iData);
};

template <typename T>
node<T>::node(const T iData){
    data = iData;
    left = NULL;
    right = NULL;
}

template <typename T>
node<T>::~node() {
//    if(left != NULL)
//        delete(left);
//    if(right != NULL)
//        delete(right);
}

template <typename T>
void node<T>::setLeft(node<T> *iLeft) {left = iLeft;}

template <typename T>
void node<T>::setRight(node<T> *iRight) {right = iRight;}

template <typename T>
T node<T>::getData(void) { return data;}

template <typename T>
node<T>* node<T>::getLeft(void) { return left;}

template <typename T>
node<T>* node<T>::getRight(void) { return right;}

template <typename T>
void node<T>::addNode(T iData) {
    if(iData > data)
        if (right == NULL)
            setRight(new node<T>(iData));
        else
            right->addNode(iData);
    else
        if(left == NULL)
            setLeft(new node<T>(iData));
        else
            left->addNode(iData);
    return;
}

///
template <typename T>
void printInOrder(node<T> currentNode){
    cout << "L ";
    node<T>* left = currentNode.getLeft();
    if(left != NULL){
        printInOrder(*left);
    }

    cout << currentNode.getData() << endl;

    cout << "R ";
    node<T>* right = currentNode.getRight();
    if(right != NULL){
        printInOrder(*right);
    }

}

///
template <typename T>
void printPreOrder(node<T> currentNode){
    cout << currentNode.getData() << endl;

    cout << "L ";
    node<T>* left = currentNode.getLeft();
    if(left != NULL){
        printPreOrder(*left);
    }

    node<T>* right = currentNode.getRight();

    cout << "R ";
    if(right != NULL){
        printPreOrder(*right);
    }
}

///
template <typename T>
void printPostOrder(node<T> currentNode){
    cout << "L ";
    node<T>* left = currentNode.getLeft();
    if(left != NULL){
        printPostOrder(*left);
    }

    cout << "R ";
    node<T>* right = currentNode.getRight();
    if(right != NULL){
        printPostOrder(*right);
    }

    cout << currentNode.getData() << endl;
}

/// Main()
/// \return void

int main() {
    node<int> rootNode = node<int>(50);
    rootNode.addNode(20);
    rootNode.addNode(19);
    rootNode.addNode(12);
    rootNode.addNode(3);

    cout << endl << "printInOrder" << endl;
    printInOrder(rootNode);
    cout << endl << "printPreOrder" << endl;
    printPreOrder(rootNode);
    cout << endl << "printPostOrder" << endl;
    printPostOrder(rootNode);
}
