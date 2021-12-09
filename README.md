# Generator

This game will alow the user to show off what they have learned from this README file. Going through the game the user should jump on the correct answer and go through all 6 maps.

# Development Environment

* Python 3.8.0
* Arcade 2.5.7

# Useful Websites

* [Arcade Resoucres](https://api.arcade.academy/en/latest/resources.html)
* [Simple Platformer Example](https://api.arcade.academy/en/latest/examples/platform_tutorial/index.html)

# Useful Information

- Question 1:

  Print statements are often used and simply display the designated text to the terminal. Using "print()" you can display strings numbers, and variables to the terminal.

  ```
  print("Hello World")
  print("Hello " + "World")

  # output: Hello World
  ```

  These will both have the same output because you can concatenate strings inside of print statements.

- Question 2:

  Variables are easy to create and assign a value. A few simple rules must be followed: names must start with a letter or underscore, a variable name cannot start with a number, and a variable name can only contain alpha-numeric characters and underscores. To assign a value you would simply state (varable_name) = (value).

  ```
  # set my_variable equal to 3
  my_variable = 3

  # display my_variable
  print(my_variable)

  # output: 3
  ```

- Question 3:

  Recieving user input is easy and helps a program be interactive! To recieve user input you need to creat a variable and then set it equal to input(). You can insert a statement to tell the user what you are looking for.

  ```
  # create variable and prompt user
  user_input = input("What is your name?: ")

  # display user_input
  print(user_input)

  # This will output whatever the user typed as their name.
  ```

- Question 4:

  Many data types exist and can be used. To create a list you would set a variable equal to brackets, "my_list = []". you could add different values to the list or preassign them like so: my_list = ["apple", "banana", "orange"]. To display these in the terminal you could do the following:

  ```
  # define the list
  my_list = ["apple", "banana", "orange"]

  # display the list
  print(my_list)

  # output: ['apple', 'banana', 'orange']
  ```

  To display this in a more friendly way we would need to use a for loop. For now, all you need to know s that a loop is designed to iterate through a given range. Since our list holds multiple items it will go through the list and print out each item.

  ```
  # create the for loop notice the print statement is inside the loop.
  for item in my_list:
      print(item)

  # output:   apple
              banana
              orange

  ```

  \*\* Note that for loops can be more complex, but this is only an introduction.

- Question 5:

  Sometimes we need to test values and depending on what they are, make a decision. To do this we would use an if/then statement. Here is a worded example: We all know 5 + 5 = 10. so if we wanted a program to test what 5 + 5 is, we could test the mathematical problem and if it is equal to 10 print out True. Or if the number comes out not equal to 10, then we would print out false. Look at the example below.

  ```
  # test the equation.. if it is true, print true.
  if 5 + 5 == 10:
      print("True")

  # if the above test case failed, then it is false.. print false.
  else:
      print("False")

  # output: True
  ```

  \*\* Note that if/then statements can be more complex, but this is only an introduction.

- Question 6:

  As many would guess, these operators do what you think: + addition, - subtraction, \* multiplication, / division. Numbers can be performed on as well as variables (As long as the variable holds an integer). additional mathematical operation are: \*\* exponet, and // integer division.

  ```
  # variables used
  x = 10
  y = 5

  print(x + y) # 15
  print(x + y) # 5
  print(x * y) # 50
  print(x / y) # 2.0
  print(2 ** 5) # 32
  print (5 // 3) # 1
  ```
