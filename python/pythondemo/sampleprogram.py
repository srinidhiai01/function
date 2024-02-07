"""
#Leap year
year=int(input("Enter the leap year check:"));
if(year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print("It is leap year");
        else:
            print("not a leap year");
    else:
        print("it is leap year");
else:
    print("not a  leap year");

#fibonacci series
print("Program to print the fibonacci series");
print("*************************************");
num=int(input("enter value for x(>2):"));
a1=0;
a2=1;
sum=2;
if num<=0:
    print("enter only positive number ");

elif num==1:
     print("fibonacci sequence is:",a2);

else:
     print("fibonacci sequence is:");
     print(a1);
     print(a2);
while sum<num:
          seq=a1+a2;
          print(seq);
          a1=a2;
          a2=seq;
          sum+=1;
"""
#array
birds=["parrot","peacock","hen","penguin"];
a = birds[0]
print(a);
#len array
a= len(birds);
print(a);
#loop array
for a in birds:
  print(a);
#adding array
birds. append ("crow")
print(birds);
#remove array
birds.pop(2)
print(birds);
birds.remove("crow")
print(birds);
#clear
birds=["parrot","peacock","hen","penguin"];
birds.clear()
print(birds);
#copy
birds=["parrot","peacock","hen","penguin"];
a=birds.copy()
print(a);
#count
birds=["parrot","peacock","hen","penguin"];
a=birds.count(1)
print(a);
#extend
birds=["parrot","peacock","hen","penguin"];
fruits=["apple","cherry","fig","jackfruit"];
birds.extend(fruits)
print(birds);
#index
birds=["parrot","peacock","hen","penguin"];
b=birds.index("parrot")
print(b);
#insert
birds.insert(4, "dove")
print(birds)
#pop
birds.pop(4)
print(birds)
#remove
birds.remove("hen")
print(birds)
#reverse
birds.reverse()
print(birds)
#sort
birds.sort()
print(birds)
