#include <stdio.h>
#include <stdbool.h>

int main()
{

    char calculation;
    bool valid_calc = false;
    double first_digit;
    double second_digit;
    double sum;
    char accuracy;

    printf("What calculation would you like to run?(+ - * /)\n");
    scanf("%c", &calculation);

    printf("Enter first digit:");
    scanf("%lf", &first_digit);
    printf("Enter second digit:");
    scanf("%lf", &second_digit);

    switch (calculation)
    {
    case '+':
        sum = first_digit + second_digit;
        break;
    case '-':
        sum = first_digit - second_digit;
        break;
    case '*':
        sum = first_digit * second_digit;
        break;
    case '/':
        sum = first_digit / second_digit;
        break;

    default:
        printf("%c is not a valid type.", calculation);
        break;
    }

    printf("\nHow accurate should the result be? readable(r), accurate(a), very accurate(v)");
    scanf(" %c", &accuracy);

    switch (accuracy)
    {
    case 'r':
        printf("\n%.1lf %c %.1lf = %.1lf", first_digit, calculation, second_digit, sum);
        break;
    case 'a':
        printf("\nAccurate: ");
        printf("%.3lf %c %.3lf = %.3lf", first_digit, calculation, second_digit, sum);
        break;
    case 'v':
        printf("\nVery accurate: ");
        printf("%lf %c %lf = %lf", first_digit, calculation, second_digit, sum);
        break;

    default:
        printf("\nPrinting readable version: ");
        printf("%.1lf %c %.1lf = %.1lf", first_digit, calculation, second_digit, sum);
        break;
    }

    return 0;
}