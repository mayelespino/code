//
// Created by mayel espino on 12/24/17.
//
//Implement strstr().
//Solution:
//        O(nm) runtime, O(1) space – Brute force:
#include <iostream>
#include <cassert>

int StrStr(const char *subString, const char *targetString){
    char firstCharInSub = subString[0];
    int location = 0;

    if(strlen(subString) == 0) {
        return(0);
    } else if(strlen(targetString) == 0) {
        return(-1);
    } else if (strlen(subString) > strlen(targetString)) {
        return(-1);
    }

    while(*targetString != '\0' && *targetString != firstCharInSub) {
        ++location;
        ++targetString;
    }

    if(*targetString == '\0'){
        return(-1);
    }

    for(int index = 0; targetString[index] != '\0' && subString[index] != '\0'; ++index) {
        if(targetString[index] != subString[index]){
            return (-1);
        }
    }

    return(location);
}

int main() {

    int location = StrStr("issi", "mississippi");
    std::cout << "search for issi in mississippi " << "location: " << location << std::endl;
    assert( location == 1);

    location = StrStr("issi", "mxxxissippi");
    std::cout << "search for issi in mxxxissippi " << "location: " << location << std::endl;
    assert( location == 4);

    location = StrStr("ba", "aaaba");
    std::cout << "search for ba in aaaba " << "location: " << location << std::endl;
    assert( location == 3);

    return 0;
}


