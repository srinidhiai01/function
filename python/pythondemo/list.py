#list
a=["rose","sunflower","lily","lotus"];
print("list value is:",a);
#access list
print("Access list is:",a[1]);
#change list
a[1]="daisy";
print("Change list is:",a);
#change a range
a[1:3]=["tulip","marigold"];
print("Change a Range of list is:",a)
#len
a=["rose","sunflower","lily","lotus"];
print(len(a))
#list item
a=["rose","sunflower","lily","lotus"];
b = [1, 5, 7, 9, 3];
c= [True, False, False];

print(a)
print(b)
print(c)
#type()
a=["rose","sunflower","lily","lotus"];
print(type(a))
# list() Constructor
a=list(("rose","sunflower","lily","lotus"));
print(a)
#insert
a=["rose","sunflower","lily","lotus"];
a.insert(2,"button rose");
print(a)
#append
a.append("kurinji");
print(a)
#extend
a=["rose","sunflower","lily","lotus"];
b=["hibiscus","iris","poppy","snowdrop"];
a.extend(b)
print(a);
#Iterable extend with (tuple,set,dictionaries )
a=["rose","sunflower","lily","lotus"];
b=("hibiscus","iris","poppy","snowdrop");
a.extend(b)
print(a);
#Remove Specified Item
a=["rose","sunflower","lily","lotus"];
a.remove("lily")
print(a)
#Remove Specified Index(using pop)
a=["rose","sunflower","lily","lotus"];
a.pop(1)
print(a)
#Remove Specified Index(using pop())
a=["rose","sunflower","lily","lotus"];
a.pop()
print(a)
#delete list
a=["rose","sunflower","lily","lotus"];
del a
#Clear the List
a=["rose","sunflower","lily","lotus"];
a.clear()
print(a)
#loop through a list
a=["rose","sunflower","lily","lotus"];
for x in a:
    print(x)
#loop though a index number
a=["rose","sunflower","lily","lotus"];
for i in range(len(a)):
    print(a[i])
    



