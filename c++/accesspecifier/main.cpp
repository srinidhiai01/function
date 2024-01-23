#include <iostream>

using namespace std;
class salaryprint{
private:
    int salary;
public:
    string empname;
    void setsalary(int s){
    salary=s;

    }
int getsalary(){
    return salary;

}
  int getsalaryprint(){
 cout<<salary;

}
void getsalaryprint1(){
cout<<salary;
}
};

int main()
{
 salaryprint sp;
 sp.setsalary(50);
 cout<<sp.getsalary()<<endl;
 sp.getsalaryprint();
 sp.getsalaryprint1();


 if( sp.getsalary()==50){
    cout<<"Its a return type"<<endl;

 }
if( sp.getsalaryprint()==50){
    cout<<"Its a return type"<<endl;
}
    return 0;
}
