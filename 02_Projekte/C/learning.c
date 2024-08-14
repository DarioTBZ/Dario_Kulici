#include <stdio.h>

int main(){
    
    char name[25];
    int age;

    printf("What is your name?\n");
    //scanf("%s", name); // Without Whitespaces
    fgets(name, 25, stdin);

    printf("How old are you?\n");
    scanf("%d", &age);    

    printf("\nYou're name is %s and you are %d years old\n\n",name, age);

    return 0;
}