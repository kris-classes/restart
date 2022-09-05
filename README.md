# restart - Semester 2 - 2022

# Admin
- Contact [@krp](https://github.com/krp) or [@mechatroNick](https://github.com/mechatroNick) for Zoom & Discord links.
- Class runs from 10AM-3PM Mon-Fri. August 29th - November 18th 2022.

Student Expectations: ~5 hours of lectures and ~3 hours of homework per day.

# Supplementary Videos

# Core Topics
- Python Programming
- Career
- Cloud Foundations
- Linux
- Networking
- Databases
- AWS
- Exam Preparation

# Extra resources

**Note: Github Student Pack requires you to have a student email @myunitec.ac.nz**

- [Github Student Pack](https://education.github.com/)
- [Frontend master - good place to learn Frontend Javascripts React/Vue/Angular](https://frontendmasters.com/)
- [Markdown guide](https://www.markdownguide.org/)
- [JetBrains PyCharm IDE - can be free if registered with a student email](https://www.jetbrains.com/pycharm/)
- [VSCode IDE - free](https://code.visualstudio.com/)
- [Install Python for Window - always tick Add Python to PATH option](https://www.python.org/downloads/)
- [Install Python for Mac - best option is to use Homebrew aka `brew` command line](https://docs.python-guide.org/starting/install3/osx/)

# Week 1

## Core Topics

- Programming & Tool basics

## Day 1
- Setting up & browsing GitHub
- Setting up & using Discord
- Markdown & [Markdown Tutorial](https://www.markdowntutorial.com/)

## Day 2

- Installing VSCode
- Installing Python
- Python primitive data types: `int`, `float`, `str`
- Output with `print()`
- Input with `input()`
- Getting `type` of variable with `type(var)`

## Day 3
- Interpreted vs Compiled Programming Languages
- Python REPL / Shell
- [AREPL](https://marketplace.visualstudio.com/items?itemName=almenon.arepl) VSCode Extension
- Some string functions: .upper(), .lower(), .capitalize(), .split(), etc
- Lists: Creating, accessing elements, `.append()`, `.pop()`, `.extend()`, `.sort()` (in-place) vs `sorted(my_list)` (copy)
- Reading code (basics): [aws-cli](https://github.com/aws/aws-cli) - Comments, multi-line comments & docstrings, `import`, `class` (as a concept) 
- Functions (`def` and `return`), function parameters/arguments
- "Scope" (variable names can be reused in different functions)
- Loop basics: `while`, `break` and common gotchas
- Refactoring (rewriting your code to simplify things)
- [@krp/python-examples](https://github.com/krp/python-examples)
- Supplementary: [The Coding Train - What was coding like 40 years ago?](https://www.youtube.com/watch?v=7r83N3c2kPw)

## Day 4
* Reading and writing files by creating file handles with `open("filename.txt")` in Python
* New-line characters and line endings.
* Python's `random` module, `seed()`, `random()`, `randint()`, `choice()` and randomness with Pseudo-random number generators (PRNGs)
* Notable mention: [Debian PRNG bug](https://threatpost.com/how-debian-openssl-bug-almost-spawned-disaster-051809/72669/), [Dual_EC_DRBG Backdoor](https://arstechnica.com/information-technology/2015/01/nsa-official-support-of-backdoored-dual_ec_drbg-was-regrettable/), [Eddie Tipton Hot Lotto RNG Backdoor](https://en.wikipedia.org/wiki/Hot_Lotto_fraud_scandal)
* Python's `time` module and understanding [Unix Time](https://time.is/Unix_time) (`time.time()` and `time.sleep(5)`. 
* Installing libraries with `pip` and the [Python Package Index](https://pypi.org/)
* Using the `requests` module (installed with `pip install requests`) to make web requests using Python.
* [Python Module Of The Week - PyMOTW](https://pymotw.com/3/)
* [GitHub: @vinta/awesome-python](https://github.com/vinta/awesome-python)
* Directory navigation with `pwd`, `cd`, `ls` and gotchas around it.
* [Pyxel library](https://github.com/kitao/pyxel) - Great for learning Python
* [@kris-classes/pyxel-snippets](https://github.com/kris-classes/pyxel-snippets/) - Collection of simple snippets for learning to code with Python & pyxel


## Day 5

* Python String Formatting
* More looping
* [Debugging in VSCode](https://code.visualstudio.com/Docs/editor/debugging)
* Dictionaries, Sets, Tuples
* [PyQt Examples for Graphical User Interfaces (GUIs)](https://github.com/pyqt/examples)
* [More Python examples](https://github.com/geekcomputers/Python)


# Week 2

## Day 1
* AWS Console Basics & EC2 instance types
* [AWS Pricing Calculator](https://calculator.aws)
* More Looping & `in` keyword
* Stack & Queue concepts


## Day X (planned)

* Revise Lists, Tuples, Sets
  * List maintains order + mutable
  * Tuples maintains order + immutable
  * Sets does not maintain order + mutable + item uniqueness
* Common manipulation
  * Find unique within Lists -> Convert List to Sets `set(my_list)`
  * Find intersection between 2 Lists -> use Sets intersection `list(set(list1).intersection(list2))`
  * Find only unique items in 2 Lists -> Use Sets symmetric difference `list(set(x).symmetric_difference(set(f)))`
* Flow control
  * if, else, elif
* For loop
  * For item in List, Set, or Tuple
  * For item in range(x)
  * For item, index in List, Set, or Tuple
* While loop

## Day 2 (planned)

* List comprehension
* More dictionary
* Complex types
  * Dict of List
  * List of Dict
* JSON
* Dict vs. JSON

