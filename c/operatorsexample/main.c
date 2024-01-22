
#include <stdio.h>

int program()
{
    int a=5;
    int b=9;
    float z;
    additionprogram(a,b);
    subtractionprogram(a,b);
    multiplicationprogram(a,b);
    divisionprogram(a,b);
    modulusprogram(a,b);
    Incrementprogram(a,b);
    greaterprogram(a,b);
    lesser(a,b);
    equalprogram(a,b);
    addprogram(a,b);
    locationprogram(a,b);
    logicalprogram(a,b);
    return 0;
}
int additionprogram(int a,int b)
{
    int z=a+b;
    printf("\n ADDITION PROGRAM");
    printf("\n******** *********");
    printf("Added value for z is: %d",z);
}

int subtractionprogram(int a,int b)
{
    int z=a-b;
     printf("\nSUBTRACTION PROGRAM");
    printf("\n ******** *******");
    printf("\nSubtracted value for z is:%d",z);
}
int multiplicationprogram(int x,int y)
{
    int z=x*y;
    printf("MULTIPLICATION PROGRAM");
    printf("\n******** *******");
    printf("\nMultiplicated value for z is:%d",z);
}
int divisionprogram(int x,int y)
{
    float z=(float) x/y;
    printf("\nDIVISION PROGRAM");
    printf("\n******** *******");
    printf("\n quotitent value for z is:%f",z);
}
int modulusprogram(int x,int y)
{
    int z=x%y;
     printf("\nMODULUS PROGRAM");
    printf("\n******** *******");
    printf("\n reminder  value for z is:%d",z);
}
int Incrementprogram(int x,int y)
{
    while (x<5)
    {
        printf("\nINCREMENT PROGRAM");
        printf("\n******* ********");
        printf("\nEnter the value of x:%d",x);
        x++;
    }
}


int greaterprogram(int x,int y)
{
    if (x>y)
    {
         printf("\nGREATER PROGRAM");
         printf("\n******** *******");
        printf("\n x is greater than y");
    }
    else
    {
        printf("\n x is less than y");
    }
}
int lesser(int x,int y) {
   x = 5;
   y = 3;
  printf("%d", x< y); // returns 0 (false) because 5 is not less than 3

}

int equalprogram(int x,int y)
{
 int g = 5;
  int h = 3;
       printf("\nEQUAL PROGRAM");
        printf("\n******** *******");
        printf(" the given value is%d\n", g == h);
}
int addprogram(int x,int y)
{
    for (x=0;x<10;x++)
    {
        printf("\nADD PROGRAM PROGRAM");
         printf("\n******** *******");
        printf("\nEnter the value of x:%d",x);
    }
    for (y=10;y>5;y--)
    {
        printf("\nEnter the value of y:%d",y);
    }


}
int locationprogram(int x,int y)
{
    switch (x)
    {
    printf("\nLOCATION PROGRAM");
    printf("\n******** *******");
    case 1:
        printf("\nMy location is madurai");
        break;
    case 2:
        printf("\nMy location is Chennai");
        break;
    default:
        printf("\nNo available location");
    }
}


int logicalprogram(int x,int y)
{
   printf("\nLOGICAL PROGRAM");
   printf("\n******* ********");
   printf(" the and operator is:%d\n", x > 3 && x < 10);
   printf(" the or operator is:%d\n", x > 3 || x < 4);
   printf(" the not operator is:%d\n", !(x > 3 && x < 10));
  return 0;
}





