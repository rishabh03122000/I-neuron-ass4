#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ASSIGNMENT 
get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')
The two values of the Boolean data type are True and False. They are written in Python as True and False, respectively.
get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')
The three different types of Boolean operators are and, or, and not.
3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).
Truth table for and:

A	B	A and B
False	False	False
False	True	False
True	False	False
True	True	True
Truth table for or:

A	B	A or B
False	False	False
False	True	True
True	False	True
True	True	True
Truth table for not:

A	not A
False	True
True	False
(5 > 4) and (3 == 5) --> False
not (5 > 4) --> False
(5 > 4) or (3 == 5) --> True
not ((5 > 4) or (3 == 5)) --> False
(True and True) and (True == False) --> False
(not False) or (not True) --> True



get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 &gt; 4) and (3 == 5)
not (5 &gt; 4)
(5 &gt; 4) or (3 == 5)
not ((5 &gt; 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
 sol.5 > 4) and (3 == 5) --> False
not (5 > 4) --> False
(5 > 4) or (3 == 5) --> True
not ((5 > 4) or (3 == 5)) --> False
(True and True) and (True == False) --> False
(not False) or (not True) --> True
get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')
solThe six comparison operators are:

> (greater than)
< (less than)
>= (greater than or equal to)
<= (less than or equal to)
== (equal to)
get_ipython().system('= (not equal to)')


# In[ ]:


6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one
The equal to operator == is used to check whether two values are equal. It returns a Boolean value of True if the values are
equal, and False otherwise. The assignment operator = is used to assign a value to a variable. For example, x = 5 assigns the
value 5 to the variable x.
 to the variable x.
7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print(&#39;eggs&#39;)
if spam &gt; 5:
print(&#39;bacon&#39;)
else:
print(&#39;ham&#39;)
print(&#39;spam&#39;)
print(&#39;spam&#39;)
      sol. The first block sets the value of spam to 0. The second and third blocks are if statements that check the value of
      spam and print different messages depending on whether spam is greater than 5 or equal to 10. The fourth and fifth blocks
      print the messages 'spam' and 'spam' regardless of the value of spam
8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.
      sol.if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')
     sol.  If a program is stuck in an endless loop, the keys you'll press depend on the programming environment.
      In most environments, you can try pressing Ctrl + C (or Command + C on a Mac) to interrupt the program and stop the loop.
get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')
       sol. The break statement is used to exit out of a loop completely, while the continue statement is used to skip over
      an iteration of a loop and continue with the next iteration. When a break statement is encountered, the loop stops
      executing and control passes to the statement immediately following the loop. When a continue statement is encountered,
      the current iteration of the loop is terminated, and the control moves to the next iteration.
11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
   sol.  In a for loop, the three arguments to the range() function determine the starting point, the stopping point, 
      and the increment of the loop. range(10) starts from 0 (the default starting point), ends at 10 (exclusive), and 
      increments by 1 (the default increment). range(0, 10) also starts from 0 (explicitly specified), ends at 10 (exclusive),
      and increments by 1 (default). range(0, 10, 1) is the same as range(0, 10), as 1 is the default increment value.  
12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.?
     sol.  for i in range(1, 11):
           print(i)


# In[ ]:


get_ipython().set_next_input('13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')
sol. To call the bacon() function from the spam module, you would use dot notation: spam.bacon(). This assumes that you have
    already imported the spam module using import spam.

