#include <stdio.h>

int main() {

    char grade;

    printf("Enter a letter grade: ");
    scanf("%c", &grade);

    switch (grade)
    {
    case 'A':
        printf("Yooo duuuddde you're the best!");
        break;
    case 'B':
        printf("Oh nice good grade!");
        break;
    case 'C':
        printf("Mh okay, well at least not a D or worse.");
        break;
    case 'D':
        printf("What? You got a D??? Get the hell out of my house!");
        break;
    case 'E':
        printf("You're grounded.");
        break;
    default:
        printf("Dude just enter a grade.");

    
    }



    return 0;
}