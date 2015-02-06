#include <iostream>

using namespace std;

char * reverseStringInPlace(char *inString){

    //get the lentgh
    int64_t lengtOfString = 0;
    char *pStartOfString = inString;
    char *pEndOfString = inString;
    while(*pEndOfString != NULL)
    {
        lengtOfString++;
        pEndOfString++;
    }
    pEndOfString--;

    //while(pEndOfString != pStartOfString)
    for(int64_t counter = (lengtOfString/2); counter; counter-- )
    {
        char temporary = ' ';
        temporary = *pStartOfString;
        *pStartOfString = *pEndOfString;
        *pEndOfString = temporary;
        pStartOfString++;
        pEndOfString--;
    }

    return inString;
}


int main() {
    cout << "Start" << endl << endl;
    char stringExample1[25] = "1234567890123456789x";
    cout << "original String " << stringExample1 << endl << endl;
    cout << "reverserd String " << reverseStringInPlace(stringExample1) << endl << endl;
    cout << "--1--" << endl;
    char stringExample2[2] = "g";
    cout << "original String " << stringExample2 << endl << endl;
    cout << "reverserd String " << reverseStringInPlace(stringExample2) << endl << endl;
    cout << "--2--" << endl;
    char stringExample3[3] = "go";
    cout << "original String " << stringExample3 << endl << endl;
    cout << "reverserd String " << reverseStringInPlace(stringExample3) << endl << endl;
    cout << "--3--" << endl;
    char stringExample4[4] = "go4";
    cout << "original String " << stringExample4 << endl << endl;
    cout << "reverserd String " << reverseStringInPlace(stringExample4) << endl << endl;
    cout << "--4--" << endl;
    char stringExample5[1] = "";
    cout << "original String " << stringExample5 << endl << endl;
    cout << "reverserd String " << reverseStringInPlace(stringExample5) << endl << endl;



    cout << endl << "End" << endl;
    return 0;
}