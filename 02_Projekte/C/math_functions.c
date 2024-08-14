#include <stdio.h>
#include <math.h>

int main() {

    // special operations
    double SquareRoot = sqrt(64);
    int Round = round(5.673);
    int Round_Up = ceil(3.12);
    int Round_Down = floor(4.9);

    // classic operations
    float a = 5;
    float b = 7;

    float c = a + b;

    float d = b - a;

    float e = a * b;

    float f = a / b;

    printf("%.2f", f);
    

    return 0;
}