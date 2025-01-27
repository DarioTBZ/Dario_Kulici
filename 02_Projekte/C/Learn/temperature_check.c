#include <stdio.h>
#include <stdbool.h>

int main() {

    float temp = 25;
    bool sunny = true;

    if (temp >= 0 && temp <= 30 && sunny) {
        printf("The wether is good.");
    }
    else {
        printf("The wether is bad.");
    }


    return 0;
}