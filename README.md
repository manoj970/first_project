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


==============Functions==============================

1.What is a function in Python?

A function means you can group the code you can name it and use it when you need

2.Why do we use functions instead of writing code directly?

To avoid repeatation organize code in structured form if we want to make any changes we only change a particular function not the entire code


3.What is the difference between parameters and arguments?

parameter means variable listed in the function 'def add(x,y)' ,arguments means actual passed to the function when calling it'add(5,4)'


4.What does return do? What if a function has no return?

return send the value back to the caller and immediately exits the function


5.Explain default parameters with example.

you can assign default parameters to the function

def greet(name="Guest", greeting="Hello"):

    print(f"{greeting}, {name}!")

6.What are *args and **kwargs?

*args collects extra positional arguments to tuple

**kwargs collects extra key words arguments to dictionary

7.What is function scope? What is local vs global variable?

Function scope means where variables live local means within the function,global means out of the function

8.Can a function call itself? (hint: recursion – later topic)

9.How do you call a function with keyword arguments?

by specifying the parameter name explicitily when calling
`def person(name, age, city):
    print(f"{name} is {age} years old from {city}")

 Keyword arguments (order can change)
person(age=30, city="Hyderabad", name="Manoj")`

10.What happens if you forget () when calling a function?

the output displays <function say_hello at 0x0000026128BFBB60>



==============Regular Expressions ================================











* special methods:
- these are predefined methods in python that have special meaning and are used to define the behavior of the class, they are also called magic methods or dunder methods (double underscore), they are used to implement operator overloading, object representation, and other special behaviors of the class
__init__: called when an object is created, used to initialize the attributes of the class
__str__: called when the object is printed, used to define the string representation of the object
__repr__: called when the object is printed in the interactive shell, used to define the official string representation of the object
__add__: called when the + operator is used, used to define the behavior of the + operator for the class
__sub__: called when the - operator is used, used to define the behavior of the - operator for the class
__mul__: called when the * operator is used, used to define the behavior of the * operator for the class
__truediv__: called when the / operator is used, used to define the behavior of the / operator for the class
__len__: called when the len() function is used, used to define the behavior of the len() function for the class
__eq__: called when the == operator is used, used to define the behavior of the == operator for the class
__lt__: called when the < operator is used, used to define the behavior of the < operator for the class
__gt__: called when the > operator is used, used to define the behavior of the > operator for the class
__call__: called when the object is called as a function, used to define the behavior of the object when it is called as a function
__getitem__: called when the object is indexed, used to define the behavior of the object when it is indexed
__setitem__: called when the object is indexed and assigned a value, used to define the behavior of the object when it is indexed and assigned a value
__delitem__: called when the object is indexed and deleted, used to define the behavior of the object when it is indexed and deleted
__iter__: called when the object is iterated over, used to define the behavior of the object when it is iterated over
__next__: called when the object is iterated over, used to define the behavior of the object when it is iterated over
__enter__: called when the object is used in a with statement, used to define the behavior of the object when it is used in a with statement
__exit__: called when the object is used in a with statement, used to define the behavior of the object when it is used in a with statement

# Python OOP — Today's Learning Summary

---

## 1. The `__init__` Constructor

`__init__` is automatically called when an object is created. It initializes the object's attributes upfront instead of setting them manually after creation.

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

user1 = User("Vinod", "vinod@example.com")
```

**Why `self`?**
When you call `user1.greet()`, Python rewrites it as `User.greet(user1)` — automatically passing the instance as the first argument. That's `self`. It can be named anything, but `self` is the convention.

---

## 2. Types of Methods

### Instance Methods
The most common type. Operate on a specific object's data. Receive `self` as the first parameter.

```python
def bark(self):
    print(f"{self.name} barks!")
```

### Class Methods (`@classmethod`)
Operate on the **class itself**, not a specific instance. Receive `cls` as the first parameter. Can be called directly on the class.

```python
@classmethod
def get_count(cls):
    print(f"Total dogs: {cls.total_dogs}")
```

> **Key insight:** Without `@classmethod`, Python treats the method as an instance method. If you call it on the class directly (e.g. `Dog.get_count(10)`), `cls` just receives `10` — not the class. The decorator is what tells Python to **automatically inject the class** as the first argument.

### Static Methods (`@staticmethod`)
Utility functions that belong to the class logically but don't need access to instance or class data. No `self` or `cls`.

```python
@staticmethod
def info():
    print("Dogs are loyal animals.")
```

| | Instance Method | Class Method | Static Method |
|---|---|---|---|
| First arg | `self` (instance) | `cls` (class) | nothing |
| Access instance data | ✅ | ❌ | ❌ |
| Access class data | via `self.__class__` | ✅ | ❌ |
| Call on class directly | ❌ | ✅ | ✅ |

---

## 3. Dunder / Magic Methods

Special methods with double underscores that define how objects behave with built-in operations.

### Representation
```python
def __str__(self):   # used by print() — for end users
    return f"User: {self.name}"

def __repr__(self):  # used in console/debugging — for developers
    return f"User(name='{self.name}')"
```

> **Always define `__repr__`** at minimum — if `__str__` is missing, Python falls back to it. Without either, you get `<__main__.User object at 0x...>`.

### Arithmetic Operators
```python
def __add__(self, other):      # +
def __sub__(self, other):      # -
def __mul__(self, other):      # *
def __truediv__(self, other):  # /
```

> **Common mistake:** Using `print()` inside `__add__` instead of `return`. This makes the result `None` when you do `user3 = user1 + user2`.

### Comparison Operators
```python
def __eq__(self, other):   # ==
def __lt__(self, other):   # <
def __gt__(self, other):   # >
def __len__(self):         # len()
```

### Other Useful Dunders

| Method | Triggered by |
|---|---|
| `__call__(self)` | `obj()` — calling the object like a function |
| `__getitem__(self, key)` | `obj[key]` |
| `__setitem__(self, key, val)` | `obj[key] = val` |
| `__delitem__(self, key)` | `del obj[key]` |
| `__iter__(self)` | `for x in obj` |
| `__enter__` / `__exit__` | `with obj:` block |

---

## 4. Key Takeaways

- **`__init__`** sets up each object's unique state at creation time
- **`self`** is automatically passed by Python — it's the instance calling the method
- **`@classmethod`** injects the class; without it, Python sees a regular instance method
- **Always `return`** from `__add__` and other operator methods — never `print` inside them
- **Always define `__repr__`** so your objects display meaningfully instead of memory addresses

