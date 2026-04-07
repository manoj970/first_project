# DSA in python #

## Arrays and Lists in python ##

What is list in python?

- List are ordered index based collection items that allow fast access by position

How is list is different from tuple?

-In python list is dynamic it will strink/grow but tuple is immutable

What does mutuable meand for lists?

-It means it can strink / grow autometically , it can be changed

How do you access the last item in the list?

-by giving the list variable name along with the index -1

What happens when you do lst[10] when you have only 5 items?

-it will display the IndexError : list index out of range

Explain the difference between append() and extend()?

-the append() methond will add the element at the end of list ,if we give the another list it will creates the nest list inside it will not unpack it, but extend() will unpack the list and add the items at the end of the list.

How do you remove an item by value vs by index?

-the item is removed by the value is by giving the list variable name along with the value ` remove(list["manoj"]) ` by the index we can remove it by giving the position `remove(list[0])`

What is list slicing ? Give example?

-Extracting the portion(sublist) from the existing list` numbers = [10, 20, 30, 40, 50, 60]

# slice from index 1 to 4
result = numbers[1:4]

print(result)`

Why do we use list.copy() instead of new = list?

- `new = list ` is we are assigning it will point to the same address 

-`list.copy()` will the the list to the another address
`a = [1, 2, 3]
b = a.copy()

b.append(4) 

print(a)
print(b)`

what is the output of [] == [] vs [] is []?

-[] == [] it will check the value equality elements of the list

-[] is [] it will check the identity whether they both the pointed to the same object in the memory


### list methods ###
-append(item)
-extend([list])
-insert(index, item)
-remove(item)
-pop(index)
-clear()
-index(item)
-count(item)
-sort()
-reverse()
-copy()

# Strings in python #

Why are strings immutable in Python?

-Once a string is created it is replaced but not changed because of memory efficiency(reuse of objects) and security (data cannot be changed)

What is the time complexity of string concatenation using + in a loop?

-the time complexity is O(n^2) it is not good to use this instead we can use .join()

How do you reverse a string in Python?

-by using the indexing 
` name = "chintu" 
print(name[:: -1]) `

Explain the difference between find() and index().

-find() will return -1 if the element is not present if it present it will give the position where the element is present
-index() will raise the ValueError if the element is not in the string other wise it will display the position .It is safe to use 

How do you check if two strings are anagrams?

-we can check it by using the comparison operator ** == **
`s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
print("Anagram")
else:
print("Not anagram")`

What is string slicing? Give example of reverse.

-string slicing means extracting parts from string ` s = "python" print(s[1:4])` it displays yth

Why use .join() instead of + for building strings?

-Because + will take more time because it creates new string everytime time complexity is O(n^2) so we use .join() O(n)

How to remove all spaces from a string?

``` 
s = "hello world"
print(s.replace(" ", ""))
```

Explain isalpha(), isdigit(), isalnum().

-isalpha() will return True when the string all alphabets
-isdigit() will return True when the string is numbers
-isalnum() will return True when the string contains bothe numbers and letters

What is palindrome? Write function to check.

-A palindrome reads same in forward and backward
```
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
```





