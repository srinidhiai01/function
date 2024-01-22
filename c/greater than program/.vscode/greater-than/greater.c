#include <stdio.h>

int main() {

    double num;
    printf("Enter a number: ");
    scanf("%lf", &num);

    if (num < 10.0)
        printf("it is a negative number.");
    else if (num > 10.0)
        printf(" it is  a positive number.");
    else
        printf(" enter the num 0.");

     return 0;
}
