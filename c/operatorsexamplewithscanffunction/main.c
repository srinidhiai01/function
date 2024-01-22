#include <stdio.h>
#include <stdlib.h>

#include<stdio.h>
 int main(){
additiontat(getb(),geta());
subtractionat(getb(),geta());
multiplicationat(getb(),geta());
divisionat(getb(),geta());
modulusat(getb(),geta());
 Incrementat(geta(),getb());
  greaterat(geta(),getb());
 return 0;
}



int geta()
{
    int a;
    printf("enter the given  value is:\n");
    scanf("%d",&a);
    return a;
}
int getb()
{
    int b;
    printf("enter the given value is:\n");
    scanf("%d",&b);
    return b;
}
int additiontat(int a, int b)

{
    int c;
    c=b+a;
    printf("Addition two value is:%d\n",c);
    return 0;

}
int subtractionat(int a, int b)
{
    int c;
    c=b-a;
    printf("Subtraction two value is:%d\n",c);
    return 0;

}
int multiplicationat(int a, int b)
{
    int c;
    c=b*a;
    printf("Multiplication two value is:%d\n",c);
    return 0;

}
int divisionat(int a, int b)
{
    float c;
    c=(float)b/a;
    printf("Quotient two value is:%f\n",c);
    return 0;
}
int modulusat(int a, int b)
{
    float c;
    c=b%a;
    printf("Reminder two value is:%f\n",c);
    return 0;

}
int Incrementat(int a,int b)
{
    while (a<10)
    {

        printf("Enter the value of a:%d\n",a);
        a++;
    }
}

int greaterat(int a,int b)
{
    if (a>b)
    {
        printf(" a is greater than b\n");
    }
    else
    {
        printf("\n a is less than b");
    }
}





