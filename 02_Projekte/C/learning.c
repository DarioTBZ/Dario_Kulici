#include <stdio.h>

int main(){

    // Commenting in C

    /*  Escape Sequences  
        \n = newline
        \t = tab
    
    printf("1\t2\t3\t4\n\n");
    
    printf("\"I like Pizza\" - Abraham Lincoln\n\n");
     */

    int age = 16;
    char letter = "I"; // single letter
    char name[] = "Bro"; // array of characters, basically a string

    printf("Good morning %s\n", name);
    printf("You are %d years old\n", age);

    return 0;
}