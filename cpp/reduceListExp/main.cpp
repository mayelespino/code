#include <iostream>

int sizeOfArray = 4;
int inArray[4] = {2,1,5,9};
int outArray[4];

int calculateProduct(int *theArray, int currentElement, int sizeOfTheArray)
{
    int currentValue = theArray[currentElement];
    theArray[currentElement] = 1;
    int product = 1;

    for(int i = 0; i < sizeOfTheArray; ++i)
    {
        product *= theArray[i];
    }
    theArray[currentElement] = currentValue;
    return(product);
}
void reduceArray(int *inputArray, int *outputArray, int sizeOfArray)
{
    for(int i = 0; i < sizeOfArray; ++i)
    {
        outputArray[i] = calculateProduct(inputArray, i, sizeOfArray);
    }
    return;
}

int main() {
    std::cout << "Start!" << std::endl;
    reduceArray(inArray, outArray, sizeOfArray);
    for(int i = 0; i < sizeOfArray; ++i)
        std::cout << outArray[i] << "  ";
    return 0;
}