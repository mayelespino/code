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
    tmpNode->next = inNext;
    return tmpNode;
}


node* createList(char inList[])
{
    int Len = sizeof(inList);
    node *tmpList = newNode(inList[0]);
    node *currentNode = tmpList;
    for(int i = 1; i < Len; i++)
    {
        currentNode->next = newNode(inList[i]);
        currentNode = currentNode->next;
    }
}

void main(void)
{
    head = newNode('a',NULL);
    printf ("char:%c\n",head->data);
    return;
}