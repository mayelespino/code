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


node* createList(char inList[])
{
    int Len = sizeof(inList)/sizeof(char);
    int i;
    node *tmpList = newNode(inList[0]);
    node *currentNode = tmpList;
    for(i = 1; i < Len; i++)
    {
        currentNode->next = newNode(inList[i]);
        currentNode = currentNode->next;
        printf("added:%c\n", currentNode->data);
        if (currentNode->next == NULL)
            printf("NULL\n");
        else
            printf("*next\n");
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


void main(void)
{
    node *head = NULL;
    char aList[4] = {'a','b','c','d'};
    head = createList(aList);
    printList(head);
    return;
}

