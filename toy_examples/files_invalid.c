#include <stdio.h>

int main() {
    FILE *fp;
    fp = fopen("test.txt", "w+");
    fclose(fp);
    fclose(fp);
    return 0;
}