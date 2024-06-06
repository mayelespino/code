/*
 * This is my implementation of a min and max heap algorithm.
 * I believe this is the best way to implement, instead of using a binary tree.
 * The runtime complexity (O of) the selection sort is: O(n^2), however, we only need to do
 * N operations where N is the number of max or min elements you want.
 * O complexity: https://en.wikipedia.org/wiki/Selection_sort
 * So I believe the actuall complexity would be O(N*M) where N =  elements in Array and M is the
 * number of elements you want in your heap.
 * In this case, N = 100 and M = 10 => O(1000) and not O(100^2)
 * -- Mayel Espino - 2022
*/
#include <iostream>
#include <list>
#include <stdlib.h>
#include <time.h>

void generateRandomList(int size, std::list<int> *arrayToFill) {
    srand(time(NULL));
    for (int i = 0; i < size; i++) {
        int randomNumber = rand() % 100 + 1;
        arrayToFill->push_back(randomNumber);
    }
}

void minHeapfy(int size, std::list<int> *arrayToFill){
    std::list<int>::iterator unsortedPartition, currentMinimum, currentItem;
    unsortedPartition = arrayToFill->begin();
    currentMinimum = arrayToFill->begin();
    currentItem = arrayToFill->begin();
    int tempValue = 0;
    int count = 0;
    while(count < size){
        while(currentItem != arrayToFill->end()){
            if(*currentItem < *currentMinimum) {
                currentMinimum = currentItem;
            }
            currentItem++;
        }
        tempValue = *unsortedPartition;
        *unsortedPartition = *currentMinimum;
        *currentMinimum = tempValue;
        unsortedPartition++;
        currentItem = unsortedPartition;
        currentMinimum = unsortedPartition;
        count++;
    }
}

void maxHeapfy(int size, std::list<int> *arrayToFill){
    std::list<int>::iterator unsortedPartition, currentMinimum, currentItem;
    unsortedPartition = arrayToFill->begin();
    currentMinimum = arrayToFill->begin();
    currentItem = arrayToFill->begin();
    int tempValue = 0;
    int count = 0;
    while(count < size){
        while(currentItem != arrayToFill->end()){
            if(*currentItem > *currentMinimum) {
                currentMinimum = currentItem;
            }
            currentItem++;
        }
        tempValue = *unsortedPartition;
        *unsortedPartition = *currentMinimum;
        *currentMinimum = tempValue;
        unsortedPartition++;
        currentItem = unsortedPartition;
        currentMinimum = unsortedPartition;
        count++;
    }
}

int main()
{
    int arraySize = 100;
    std::list<int> randomArray;
    generateRandomList(arraySize, &randomArray);

    std::cout << "generateRandomList" << std:: endl;

    for(std::list<int>::iterator it = randomArray.begin(); it != randomArray.end(); it++)
        std::cout << *it << ",";
    std::cout << std::endl;

    std::cout << "minHeapfy" << std::endl;
    minHeapfy(10, &randomArray);
    for (std::list<int>::iterator it = randomArray.begin(); it != randomArray.end(); it++)
        std::cout << *it << ",";
    std::cout << std::endl;

    std::cout << "maxHeapfy" << std::endl;
    maxHeapfy(10, &randomArray);
    for (std::list<int>::iterator it = randomArray.begin(); it != randomArray.end(); it++)
        std::cout << *it << ",";
    std::cout << std::endl;
    std::cout << "Done." << std::endl;
}

// Credits:
// how to implement a selection Sort: https://youtu.be/g-PGLbMth_g

/*
* Sample output:
generateRandomList
7,12,15,75,20,58,16,86,92,49,47,37,17,65,44,95,46,57,69,100,44,33,57,24,54,95,13,74,63,96,99,70,44,92,74,15,18,34,36,82,40,45,86,37,58,69,17,50,69,17,84,52,96,9,17,44,67,99,34,27,96,79,36,44,99,87,26,82,35,76,28,97,64,25,63,2,66,39,55,19,66,45,81,59,96,21,26,18,88,65,71,6,28,32,69,23,70,10,6,81,
minHeapfy -  min 
2,6,6,7,9,10,12,13,15,15,47,37,17,65,44,95,46,57,69,100,44,33,57,24,54,95,86,74,63,96,99,70,44,92,74,92,18,34,36,82,40,45,86,37,58,69,17,50,69,17,84,52,96,20,17,44,67,99,34,27,96,79,36,44,99,87,26,82,35,76,28,97,64,25,63,75,66,39,55,19,66,45,81,59,96,21,26,18,88,65,71,16,28,32,69,23,70,58,49,81,
maxHeapfy -  min 
100,99,99,99,97,96,96,96,96,95,47,37,17,65,44,15,46,57,69,2,44,33,57,24,54,95,86,74,63,10,6,70,44,92,74,92,18,34,36,82,40,45,86,37,58,69,17,50,69,17,84,52,12,20,17,44,67,6,34,27,13,79,36,44,7,87,26,82,35,76,28,9,64,25,63,75,66,39,55,19,66,45,81,59,15,21,26,18,88,65,71,16,28,32,69,23,70,58,49,81,
Done.

*/