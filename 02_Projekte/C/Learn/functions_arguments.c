#include <stdio.h>

void birthday(char name[])
{
    printf("\nHaaaappy birthday to you");
    printf("\nHappy birthday TO you");
    printf("\nHappy BIRTHDAY dear %s", name);
    printf("\nHappy birthday to YOUU");
}

int main()
{
    char name[] = "Dario";


    birthday(name);

    return 0;
}