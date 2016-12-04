#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* minWindow(char* s, char* t) {
    int lenS = sizeof(s)/sizeof(char);
    int lenT = sizeof(t)/sizeof(char);
    char *result = (char*)malloc((lenS+1)*sizeof(char));
    //result[0] = 0;

    if (lenS <= lenT)
    {
        int rc = strcmp(s,t);
        if (rc == 0)
            return (t);
        else
            return(result);
    }

    for(int i=0; i < lenT; i++)
    {

    }
    return(result);
}

int main(void)
{
    char stringS[] = {'A','D','O','B','E','C','O','D','E','B','A','N','C'};
    char stringT[] = {'A','B','C'};
    char *result = nullptr;

    result = minWindow( stringS, stringT);
    printf("%s", result);
    return(0);
}
