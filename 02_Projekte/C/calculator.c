#include <stdio.h>

int main() {
    
    char calculation[25];

    printf("What calculation would you like to run?\n");
    scanf("%s", calculation);

    if (calculation == "+") {
        printf("ist +");
    } else {
        printf("Else");
    }


    return 0;
}