#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int size = argc;
    char *ptr = (char*)malloc(size);
    char *ptr2 = (char*)malloc(100*sizeof(char));
    char *ptr3 = (char*)calloc(200, sizeof(char));
    char *ptr4 = (char*)realloc(ptr, size * 2);

    return 0;
}