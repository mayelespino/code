#include <stdio.h>
#include <stdlib.h>

typedef struct node_struct {
    char data;
    struct node_struct *next;
} node;

node *head = NULL;
node *current = NULL;

node* newNode(char inChar)
{
    node *tmpNode = (node*)malloc(sizeof(node));
    tmpNode->data = inChar;
    return tmpNode;
}


node* createList(char inList[])
{
    int Len = sizeof(inList);
    int i;
    node *tmpList = newNode(inList[0]);
    node *currentNode = tmpList;
    for(i = 1; i < Len; i++)
    {
        currentNode->next = newNode(inList[i]);
        currentNode = currentNode->next;
    }
    return tmpList;
}

void printList(node *inList)
{
    node *currentNode = inList;
    while(currentNode->next != NULL)
    {
        printf("%c|", currentNode->data);
        currentNode = currentNode->next;
    }
}


void main(void)
{
    char aList[4] = {'a','b','c','d'};
    head = createList(aList);
    printList(head);
    return;
}