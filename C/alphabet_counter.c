#include <stdio.h>
void main() {
    int i = 0; int j = 0; int count = 0;
    char string[100];
    printf("Enter a string.\n");
    fgets(string, 100, stdin);
    while(string[i] != '\0'){
        j = 0;
        count = 0;
        while(string[j] != '\0'){
            if(string[i] == string[j]){
                count++;
            }
            j++;
        }
        printf("The count of %c is %d\n", string[i], count);
        i++;
    }
}