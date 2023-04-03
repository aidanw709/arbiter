#include <stdio.h>
#include <stdlib.h>

int main() {
    char *ptr = (char*)malloc(100*sizeof(char));
    char *ptr2 = (char*)malloc(100*sizeof(char));
    ptr[0] = 'h';
    ptr[1] = 'e';
    ptr[2] = 'l';
    ptr[3] = 'l';
    ptr[4] = 'o';
    ptr[5] = ' ';
    ptr[6] = 'e';
    ptr[7] = 'w';
    ptr[8] = 'o';
    ptr[9] = 'r';
    ptr[10] = 'l';
    ptr[11] = 'd';
    ptr[12] = '\0';
    printf("%s", ptr);
    free(ptr);
    printf("%s", ptr);
    free(ptr2);
    return 0;
}