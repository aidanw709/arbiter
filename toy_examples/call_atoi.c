#include <stdio.h>
#include <stdlib.h>

int main() {
    char str[100];

    gets(str);
    int x = atoi(str);

    return 0;
}