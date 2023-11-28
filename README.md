# HashMap in Python 

This program was written as practice to complement what 
I am currently learning in data structures, as we don't really do much
coding of the actual data structure itself, instead focusing on 
implementation. I find it easier to improve if I learn how a data structure works from
the inside out, and since I didn't know how things like resizing worked, I decided to start
practicing by making my own programs in Python (and hopefully Java when I have time) so I can get used
to the inner workings of each ADT.

## How it works

In essence, this ADT works similarly to a Python dictionary in trying to achieve a good balance
between space and time complexity. The array used for the hash map resizes every time the array
is 75% full or more. I think that if it were to fill up too quickly space would become more of an issue,
and too slowly means time would become an issue. 75% was a number chosen on a whim, though.

## Things I learned how to implement

### 1) Resizing

I learned about how load size is read and how to resize the hash map directly. By
using a prime number sized list, we are more likely to reduce collisions (which I'm
accounting for using linear probing because it's faster than quadratic and easier to
write up than chaining.)

I wanted to see if I can eventually use keywords like `async` and `await` or something
of the sort to try and have the code always check if it's updated, but in retrospect it
seems slower than just checking load size after every insertion.

### 2) Docstrings

Seems random because I had them in prior programs on here, but most of those were given by
teachers with instructions and I had to follow those instructions. Docstrings seem really
important for anyone who codes in Python, so I decided to include them here.

