#include <stdio.h>
#include <stdbool.h>

char upcase(char inChar){
    if(inChar >= 'a' ) return(inChar-32);
    return(inChar);
}
char* strcmpr(char* str1, char* str2, int max, bool ignoreCase){
    int count = 0;
    while(*str1 != '\0' && *str2 != '\0' && count < max){
        if(ignoreCase){
            if(*str1 > *str2) return(1);
            if(*str1 < *str2) return(-1);
        } else {
            if(upcase(*str1) > upcase(*str2)) return(1);
            if(upcase(*str1) < upcase(*str2)) return(-1);
        }
        ++str1;
        ++str2;
        ++count;
    }
    return(0);
}

int main() {
    printf("%d", strcmpr("aa", "bA", 2, false));
    return 0;
}