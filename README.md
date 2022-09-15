# restart - Semester 2 - 2022

# Previous Courses
* [Semester 1 2022](https://github.com/kris-classes/restart-s1-2022)
* [Summer School 2021](https://github.com/kris-classes/restart-ss-2021)

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
  * Regions, Availability Zones, Data Centers, Latency
  * Different pricing models for EC2: on-demand, spot, reserve
* [AWS Pricing Calculator](https://calculator.aws)
* More Looping & `in` keyword
* Stack & Queue concepts

## Day 2
* More Git
* More Looping, Lists, Dictionaries, Iterators (concept)
* CSV files
* Project group exercises

## Day 3
* Sets - `union &`, `intersection |`
* More functions - no variable, default value, *arg, **kwargs
* Hardware: CPU, RAM/Memory, Storage, GPUs, Cores, Threads
* [CPU-Z (Windows)](https://www.cpuid.com/softwares/cpu-z.html)
* Supplementary: [UserBenchmark.com](https://www.userbenchmark.com))

## Day 4
* Linux
* [LinuxJourney.com](https://linuxjourney.com/)
* [Linux Filesystem Hierarchy Standard](https://www.linuxfordevices.com/tutorials/linux/linux-filesystem-hierarchy)
* ssh
* [Windows 11 permission issues with SSH private keys](https://superuser.com/questions/1296024/windows-ssh-permissions-for-private-key-are-too-open)

## Day 5
* Symmetric vs Asymmetric Key Cryptography (basics)
* More Linux
* Building programs from source code
* Permissions
* Supplemental: [History of Unix](https://en.wikipedia.org/wiki/History_of_Unix)

# Week 3

## Day 1
* Shells (configuring, aliases, differences, some history, different shells)
* Creating our own with Python's `os` module.
* Directory & File permissions.
* Hashbang: `#!`
* PATH
* `strace`


## Day 2
* [DistroWatch](https://distrowatch.com/), [GNU](https://en.wikipedia.org/wiki/GNU), [FSF](https://en.wikipedia.org/wiki/Free_Software_Foundation)
* More on OS internals (protected mode, drivers, monolithic vs microkernel, kernelspace/userspace (ring0/ring3 on Linux)
* stdin, stdout, stderr & file redirection
* Piping, `env` & environment variables 
* `sl`, `cowsay`, `jq`, `grep`, `wc`, `tr`, `sort`
* Interacting with APIs using `curl`
* [Modern Unix Utilities](https://github.com/ibraheemdev/modern-unix)
* Bash scripting basics & automating installation
* `sudo amazon-linux-extras install epel`
* Supplementary: Some other utils/tools/libs mentioned by learners: `gtop`, `sherlock`, `gping`, `tldr`, `chalk`, `fig`, `zsh-autosuggestions`, [Scott Hanselman - Microsoft Terminal](https://www.youtube.com/watch?v=FC-gLkYWXLw), `neofetch`, `pi-hole`, `hoppscotch`, `jsonhero-web`, `shellcheck`, `click`, `beets`, `n8n`, `bubbletea`, `fork-cleaner`, `spicetify-cli`, `social-analyzer`

## Day 3
* [Art of Command Line](https://github.com/jlevy/the-art-of-command-line)
* Job Control: `Ctrl-Z`, `jobs`, `bg`, `fg`, `&`, `kill`, `head`, `tail
* Logging & /var/log/secure (SSH log on Amazon Linux)
* try/except & error handling basics in Python
* Managing Users Basics: `adduser`, `passwd`, `chown`, `chgrp`
* Python: classes: (methods, self) yield, generators
* `w`, `curl ifconfig.me`
* Basics of HTTPs, CAs, Chain of Trust
* Endianness (concept)


## Day 4
* Programming Paradigms
* Concurrency Basics
* Regular Expressions
* Navigating StackOverflow & StackExchange platform
* Group exercise: Complete overview of Linux filesystem & important files across it


## Day 5
* /proc, /dev, package manager repositories
* Networking Basics: IPv4, Ports, TCP, UDP, netcat
