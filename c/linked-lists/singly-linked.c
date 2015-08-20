#include <stdio.h>
#include <stdlib.h>

typedef struct node_struct {
    char data;
    struct node_struct *next;
} node;

node* newNode(char inChar)
{
    node *tmpNode = (node*)malloc(sizeof(node));
    tmpNode->data = inChar;
    tmpNode->next = NULL;
    return tmpNode;
}


node* createList(char inList[],int inArraySize)
{
    int i;
    node *tmpList = newNode(inList[0]);
    node *currentNode = tmpList;
    for(i = 1; i < inArraySize; i++)
    {
        currentNode->next = newNode(inList[i]);
        currentNode = currentNode->next;
    }
    return tmpList;
}

void printList(node *inList)
{
    node *currentNode = inList;
    while(currentNode != NULL)
    {
        printf("%c,", currentNode->data);
        currentNode = currentNode->next;
    }
}

void deleteList(node *inList)
{
    node *currentNode = inList;
    node *nextNode = inList;
    while(currentNode != NULL)
    {
        nextNode = currentNode->next;
        free(currentNode);
        currentNode = nextNode;
    }
}

// -- MAIN --
void main(void)
{
    node *head = NULL;
    char aList[] = {'a','b','c','d','e','f','g'};
    head = createList(aList, sizeof(aList));
    printList(head);
    return;
}

