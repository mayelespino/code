#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

struct test_struct
{
    int val;
    struct test_struct *next;
};

struct test_struct *head = NULL;
struct test_struct *ptr = NULL;
struct test_struct *current = NULL;

struct test_struct* makeNode(void)
{
	struct test_struct *tmpPtr = (struct test_struct*)malloc(sizeof(struct test_struct));
	if(NULL == tmpPtr)
	{
		printf("\n Node creation failed \n");
	  	exit(-1);
	}
	return tmpPtr;
}

void createCircularList()
{
	int counter = 50;
	head = makeNode();
	head->next = NULL;
	current = head;
	
	while(--counter)
	{
		ptr = makeNode();
		current->val = counter;
		current->next = ptr;
		current = ptr;
	}
	current->next = head;
}

void printCircularList()
{
		int counter = 0;
		current = head;
		while(counter++ < 55)
		{
			printf("value:%i\n",current->val);
			current = current->next;
		}
}

void isListCircular()
{
	struct test_struct *firstIterator = head;	struct test_struct *secondIterator = head->next;
	int counter = 55;
	while(firstIterator != secondIterator && counter--){
		printf("value:%i\n",secondIterator->val);
		secondIterator = secondIterator->next;
	}
	
}

int main(int argc, char *argv[]) {
	createCircularList();
	//printCircularList();
	isListCircular();
}