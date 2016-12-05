# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

Expecting two parameters.
  if the first parameter is not a string:
    the function returns zero
  otherwise go through the string with a for loop:
    if one of the letters are equal to the given letter:
      increment count with one
  the function returns the amound of matches when the loop ends

### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer:

One of the optional tool is to use TkInter. There are built-in functions for creating a canvas and also for creating a rectangle:
    canvas = Canvas(root, width, height)
    canvas.create_rectangle(x0, y0, x1, y1, ... )

### What does V stand for in MVC? [2p]
#### Your answer:

"V" represents View. The View is responsible for displaying the output information of the program. View is controlled by the Controller (so the Controller tells it what to do and when).
