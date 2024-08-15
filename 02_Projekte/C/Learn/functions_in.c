#include <stdio.h>

void birthday()
{
    char name[15];

    printf("Who's birthday is it?\n");
    scanf("%s", &name);

    printf("\nHaaaappy birthday to you");
    printf("\nHappy birthday TO you");
    printf("\nHappy BIRTHDAY dear %s", name);
    printf("\nHappy birthday to YOUU");
}

int main()
{

    birthday();

    return 0;
}