# first_project
This is my first project
------------------------
1. What is a variable?

 A variable is a container that can store the data in a program it will easy to save and reuse when they are needed

2. Give 5 rules for naming variables in python?

-variables in python must start with underscore(_) or alphabets(a-z)
-variables are case sensitive **Age** and **age** are not same

-donot use python keywords(if ,else , class etc...)

-they cannot start with numbers

-dont use single word variables(a = 10) instead use descriptive type vaiables that will make easy to read and understand(User_name = "manoj")

3.What happens if you write x=10 and then x="hai"?

python uses dynamic typing here the variable x is reassigned .initially the integer is assigned to the variable then after the string is reassigned to the variable

4.Difference between = and ==?

** = ** is an assignment operator 
** == ** is an comparison operator

5.why do we use descriptive type names User_name instead of Un?

the descriptive type names are easy to read and understand it will avoid confusion

6.What error you will get if you use variable before assigning?

Nameerror : name is not found

7.how do you swap two variables in one line?

a,b = b,a

8.What is dynamic typing?

means you dont need to declare variable type(a = 10) python will consider it has integer

9.Can variable name start with numbers?why or Why not?

No,

10.What does del do to the variable?

it will delete the variables

=========================================Data Types====================================================

1.What is a data type in Python?

A data type will tells the python what kind of values is holds by the variable and what are the operations allowed to perform

2.Name the main built-in data types.

int ,float ,boolean ,string ,list ,tuple ,dictionary ,set 

4.What is the difference between mutable and immutable types?

Mutable :which can be changed or modified

Immutable :which cannot be changed or modified

5.Is int primitive or non-primitive in Python? Explain.

int is non primitive,because python do not have primitive data types int has methods to perform in python

6.What does type() function do?

type()function will displays the data type of the variable

7.What happens when you convert float to int?

python will remove the decimal part and returns integer data

8.Why do we need different data types?

Different data types will helps in memory management we can use memory efficently ,it helps in operations allowed to be performed and it will make the code easy to understand 

9.Give an example of when to use list vs tuple.

Lists are used when data is need to change they are mutable,Tuples are used when the data is not need of mofication or changes because tuples are immutable

10.What is a dictionary used for?

dictionary will store the data in **Key - Value** form they used for fast lookups


==================Integers=================================

1. What makes Python integers different from those in languages like C or Java?

Because they support **Arbitary Precision** (they can grow to any size limit by availbe memory).
In python all are non premitive data types in python integers are also objects they have in-built methods.

2. Explain arbitrary precision and give an example where it's useful.

It means integers can have unlimited number of digits it is usefull in big number multiplications eg(2**1000+1)

3. What is the difference between / and // for integer division?

(/) operator performs the true division(5/2 == 2.5). (//) operator performs floor division (5//2 == 2,-5//2 == -3 )

4. How do you represent and convert binary/octal/hex integers?

To represent the different integer bases, for binary we use **0b** prefix octal with **0o** and hexadecimal with **0x** . For convertions we use bin() for binary ,oct() for octal and hex() for hexadecimal

5. What happens if you try int("abc") and how to handle it?

It displays the value error ,to handle it we have to change the int object to string(str)

6. Why are integers immutable, and what does that mean for performance?

In python there are fixed hash values for integers for safety and predictablity integers are immutable ones they exist theeir value is fixed

7. Integer caching in Python (and its range)

It means python caches small integers to avoid repeated allocations it ranges (-5 to 256)

8. How does bit_length() work, and when is it useful?

bit_length() method returns the number of bits necessary to represent the value of an integer it is useful in bit manipulation,determining storage need or algorithms

9. Explain negative integers in binary representation in Python.

we use bin() method eg: bin(-3) == -'ob11'

10. Is int primitive or non-primitive in Python, and why does it matter?

int is non primitive in python it matters for its flexibility









