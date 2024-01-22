#include<stdio.h>
int operator()  
{  
    int a, b,c;  
    
  
    printf("Enter your operator\n");  
    printf("1. +\n2. -\n3. *\n4. /\n");  
    scanf("%d", & c);  
  
    if( c > 4 )  
    {  
        printf("enter  the operator!\n");  
    }  
    else  
    {   
        printf("Enter 2 integer numbers\n");  
        scanf("%d %d", &a, &b);  
    }  
  
  
    switch(c)      
    {  
        case 1:
                
                printf("  the Addition of a+b  is :%d + %d = %d\n" ,a, b, (a+b));  
                break;  
  
        case 2: printf(" subtration  of two values is :%d + %d = %d\n", a, b, (a-b));  
                break;  
  
        case 3: printf("multiplication of two values is :%d + %d = %d\n", a, b, (a*b));  
                break;  
  
        case 4: if( b != 0)  
                    printf("division of two values is :%d + %d = %d \n", a, b, (a/b));  
                else  
                    printf("do not be divided by 0\n");  
                break;  
  
        default: printf("You entered error may be occur\n");  
                 break;  
    }  
  
    return 0;  
}  

