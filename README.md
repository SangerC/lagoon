# The Lagoon Programming Language

(This is a fun project and this readme is not meant to be taken seriously)


Modern programming language are too complicated utilizing objects and different data types and remembering variable names. Thats why lagoon was created as a simple and easy language to program in. This repository contains an interpreter and a few example files for the lagoon language.

## Memory
To be as easy as possible to the programmer lagoon's memory is stored in a single array of 324 signed integers which are initialized to 0.


Memory is addressed by using only the index in memory ex: 0 is the 0th index in memory


## Pools
There are 4 "pools" which are sets of indexes in the array: increment, decrement, input, output. Lagoon relies on the concept of a tick, when a tick is ran all items in each set will have the sets operation performed on them.


A tick is ran in a program with character

;


Addresses in memory's status in pools is toggled by using the index and the pool operator ex:


0+            Toggles address 0 in the increment pool

7- Toggles address 7 in the decrement pool

6i Toggles address 6 in the input pool

5o  Toggles address 5 in the output pool

## Pointers
The value in an address can be treated as a pointer to another address in the array using 

<


ex: <7

Points to the address of the value stored in the 7th index of memory

Pointers can also be doubled, <<7 points to the address of the value stored in the address of the value stored in the address of 7

## Loops
While loops are defined within []

a | seperates the guard coming first, with the expression after

[guard|expression]

the expression is written in standard lagoon

### Guard statments
In the guard a memory address or pointer is given the while loop will run as long as the value in the address is equal to 0, if an ! is placed before the address for the loop to run while the value is not equal to 0. Multiple conditions can be serperated with a , which represents or

## Example
Here is a hello world program written in lagoon


```
100+7+;;;;;;;;0+1+2+3+4+5+6+100+7+[!100|100-;100-;;;;;;;;]7+0+0o;0+0o100+;;;;4+100+[!100|100-;100-;;;;;]7+0+1+1o;1o;4+;;;;7-2o;2+;2o;3o;5+3o7o;7o4o;4o5o;6+5o6o;6o2o;2o0o;
```
