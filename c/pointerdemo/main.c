#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=50,  b=40;
    printf("Value of a :%d\n",a);
    printf("Address of a:%d\n",&a);
    printf("-------\n");

    printf("Value of b :%d\n",b);
    printf("Address of b:%d\n",&b);
    printf("-------\n");

    int *p=&a;
    printf("Value of p:%d\n",p);
    printf("Address of p:%d\n",&p);
    printf("value stored in the address of p:%d\n",*p);
    printf("-------\n");

    int **q=&p;
    printf("Value of q:%d\n",q);
    printf("Address of q:%d\n",&q);
    printf("value stored in the address of q:%d\n",**q);
    printf("-------\n");

    int ***r=&q;
    printf("Value of r:%d\n",r);
    printf("Address of r:%d\n",&r);
    printf("value stored in the address of r:%d\n",***r);
    printf("-------\n");


    float c=4.5;
    printf("Value of c:%f\n",c);
    printf("Address of c:%p\n",&c);
    printf("value stored in the address of c:%f\n",c);
    printf("-------\n");
}

