#include<iostream>
#include<conio.h>
using namespace std;
// C++ program to demonstrate function overloading

/*
class arithmetic
{

private:
    int al;

    void dataprivate()
    {

    }
public:

int x, y;

void getdata()
{
cout<<"Enter the value of x:=";
cin>>x;
cout<<"Enter the value of y:=";
cin>>y;
}
void arithmetic_op()
{
cout<<"Sum is:="<<(x+y)<<endl;
cout<<"Difference is:="<<(x-y)<<endl;
cout<<"Multiplication is:="<<(x*y)<<endl;
cout<<"Division is:="<<(x/y)<<endl;
cout<<"Modulus is:="<<(x%y)<<endl;


}
};
int main()
{
arithmetic obj;
obj.getdata();
obj.arithmetic_op();
getch();
return 0;
}


// C++ program to demonstrate constructor overloading
class construct
{
public:
    int a, b;
    construct()
    {
        a = 80;
        b = 67;
    }
};
int main()
{
    cout<<"constructor overloading:"<<endl;
    construct c;
    cout<< "a:" <<c.a<<endl
        << "b:" <<c.b;
}

*/


void add(int x,int y)
{

    cout<<"the addition of the value is:"<<(x+y)<<endl;

}
void sub(double x,double y)
{
    cout<<"the subtraction of the value is:"<<(x-y)<<endl;

}
void multiplication(float x,float y)
{
    cout<<"the multiplication of the value is:"<<(x*y)<<endl;
}
void division(float x,float y)
{
    cout<<"the reminider of the value is:"<<(x/y)<<endl;
}
int main()
{

    add(5,11);
    sub(7.6,11.9);
    multiplication(4.3f,6.4f);
    division(3.2f,9.8f);
    return 0;
}
