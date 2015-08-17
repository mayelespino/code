#include<stdio.h>

typedef struct node_struct {
    char data[1];
    node * next;
} node;

node *head = NULL;
node *current = NULL;

node* newNode(char inChar)
{
    node *tmpNode = (node*)malloc(sizeof(node));
    tmpNode->data = inChar;
    return tmpNode;
}

void main(void)
{
    head = newNode('a');
}