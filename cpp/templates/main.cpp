#include <iostream>

/*
 *  Example of template function
 *
 */
template <typename T> T largest(T rhValue, T lhValue)
{
    if( rhValue >= lhValue)
        return rhValue;
    else
        return lhValue;
}

/*
 * Example of template class
 *
 */

/** NODE **/
template <typename T>
struct Node {
    T Value;
    Node *Next;
    Node *Previous;
};

/** CLASS **/
template <class T>
class List
{
private:
    Node<T> *Start;
    Node<T> *End;
    Node<T> *Current;
public:
    void printList(void);
    void addLink(const T inValue);
    List();
    ~List();
    void operator<<(const T& inValue);
};


template <class T>
List<T>::List() {
    Start = new Node<T>;
    Start->Next = NULL;
    Start->Previous = Start;
    End = Start;
    Current = Start;
}

template <class T>
List<T>::~List() {
    Node<T> *Iterator = Start;
    Node<T> *Current;
    do
    {
        Current = Iterator;
        Iterator = Iterator->Next;
        delete Current;
    } while(Iterator != NULL);
}

template <class T>
void List<T>::addLink(const T inValue) {
    Current->Value = inValue;
    Current->Next = new Node<T>;
    Current->Previous = Current;
    Current = Current->Next;
    Current->Next = NULL;
    End = Current;
}


template <class T>
void List<T>::printList() {
    Node<T> *Iterator = Start;
    do
    {
        std::cout << Iterator->Value << " ";
        Iterator = Iterator->Next;
    } while(Iterator->Next != NULL);
}

template <class T>
void List<T>::operator<<(const T& inValue){
    List<T>::addLink(inValue);
}

/*
 * MAIN
 */

int main() {
    std::cout << "Start" << std::endl;
    int i=10, j=15;
    std::cout << largest(j, i) << std::endl;
    char x='a', y='z';
    std::cout << largest(x, y) << std::endl;
    std::cout << "Class Template Example" << std::endl;
    Node<int> intNode;
    List<int> intList;
    intList.addLink(1);
    intList.addLink(2);
    intList.addLink(3);
    intList.addLink(40);
    intList.addLink(45);
    intList << 50;
    intList.printList();
    std::cout << std::endl << "End" << std::endl;
    return 0;
}