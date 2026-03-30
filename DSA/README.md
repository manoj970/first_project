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


