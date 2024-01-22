#include <stdio.h>
#include <stdlib.h>

int main()
{
   int a;
   int b;
   float c;
   scanf("%d",&a);
   scanf("%d",&b);
    additionprogram(a,b);
    subtractionprogram(a,b);
     multiplicationprogram(a,b);
     divisionprogram(a,b);
     modulusprogram(a,b);
     Incrementprogram(a);
      greaterprogram( a,b);
      lesserprogram(a,b);
      equalprogram(a,b);
       addprogram(a,b);
       locationprogram(a,b);
        logicalprogram(a,b);


      return 0;
}
int additionprogram(int a,int b)
{


    int c=a+b;
    printf("Addition of two value is:%d\n",c);

}
int subtractionprogram(int a,int b)
{

    int c=a-b;
    printf("Subtraction of two value is:%d\n",c);

}
int multiplicationprogram(int a,int b)
{

    int c=a*b;
    printf("Multiplication of two value is:%d\n",c);

}
int divisionprogram(int a,int b)
{

    float c=(float)a/b;
    printf("Quonient of two value is:%d\n",c);

}
int modulusprogram(int a,int b)
{

    float c=a%b;
    printf("Reminder of two value is:%d\n",c);

}

int Incrementprogram(int a)
{
    while (a<5)
    {

        printf("Increment the value of a:%d/n",a);
        a++;
    }
}
int greaterprogram(int a,int b)
{
    if (a>b)
    {
        printf(" a is greater than b\n");
    }
    else
    {
        printf(" a is less than b\n");
    }
}
int lesserprogram(int a,int b) {

  printf(" the lesser value is %d\n", a< b);
}
int equalprogram(int a,int b)
{

        printf(" the given value is%d\n", a == b);
}
int addprogram(int a,int b)
{
    for (a=0;a<10;a++)
    {

        printf("Enter the value of a:%d\n",a);
    }
    for (b=10;b>5;b--)
    {
        printf("Enter the value of b:%d\n",b);
    }


}
int locationprogram(int a,int b)
{
    switch (a)
    {

    case 1:
        printf("My location is madurai\n");
        break;
    case 2:
        printf("My location is Chennai\n");
        break;
    default:
        printf("No available location\n");
    }
}
int logicalprogram(int a,int b)
{

   printf(" the and operator is:%d\n", a > 3 && a < 10);
   printf(" the or operator is:%d\n", b > 3 || b< 4);
   printf(" the not operator is:%d\n", !(a > 3 && a < 10));

}
