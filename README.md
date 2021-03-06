# restart

# Admin
* [Canvas](https://awsrestart.instructure.com/)
* Contact the lecturer for Zoom & Discord links.

* Classes run from 9:45AM-3PM Mon-Thu and 10AM-2PM Fri.
* Student Expectations: ~5 hours of lectures and ~3 hours of homework 5 days/week.

# Supplementary Videos
* [1963 Timesharing - How Computers Work](https://www.youtube.com/watch?v=Q07PhW5sCEk) - Still relevant
* [1982 UNIX](https://www.youtube.com/watch?v=tc4ROCJYbm0) - See Brian Kernighan's demo @ 4:00. Also still relevant.
* [Hackers: The History of Hacking](https://www.youtube.com/watch?v=FufYSx2_6Bg)

* [Socratica - Python Tutorial](https://www.youtube.com/watch?v=bY6m6_IIN94&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-)
* [TechWithTim - The Complete Python Course for Beginners](https://www.youtube.com/watch?v=sxTmJE4k0ho)


# Core Topics
* Career
* Cloud Foundations
* Linux
* Networking
* Python Programming
* Databases
* AWS
* Exam Preparation

# Week 1

## Core Topics
* Hardware Basics
* Virtual Machine Basics
* Database Concepts
* Cloud Service Models (IaaS, PaaS, SaaS, FaaS)

### Day 1
* Basic Computing Concepts
* Brief history of computing & operating systems
* CPU / Central Processing Unit
* [Moore's Law](https://upload.wikimedia.org/wikipedia/commons/0/00/Moore%27s_Law_Transistor_Count_1970-2020.png)
* RAM/Memory
* Storage: Mechanical Hard Drives, Solid State Drives (SSD), Tape Storage, CD/DVD/BluRay
* Brief history of Cloud Computing

### Day 2
* Virtual Machines & Amazon Machine Images (AMIs)
* Database Basics: Relation vs Non-Relational/NoSQL (Key-Value, Document/Object, Graph)
* EC2 Lab demonstration - Deploying a virtual machine
* Shared Responsibility Model Basics
* Memcached & Redis Basics (get/set): [Try Redis](https://try.redis.io/)
* [StackShare](https://stackshare.io/)

### Day 3
* Amazon S3 Basics
* Brief history of Internet (Phreaking, Dialup, ADSL, Fibre)
* Brief history of World Wide Web, HTML, and using [archive.org](http://archive.org/)
* Linux Basics: `cd`, `mkdir`, `pwd`, `ls`, `man`, `/bin directory`, running programs.
* [Linux Directory Structure](https://linuxhandbook.com/linux-directory-structure/)
* [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) - Bookmark this for use later in the course.

### Day 4
* AWS Compute Options: EC2, Lambda, ECS, and others.
* [Hypervisor](https://en.wikipedia.org/wiki/Hypervisor) vs [Containers](https://aws.amazon.com/getting-started/deep-dive-containers/)
* Infrastructure as a Service (IaaS)
* Platform as a Service (PaaS) - e.g. Heroku, ElasticBeanstalk
* Software as a Service (SaaS)
* Function as a Service (FaaS)
* Continuous Integration / Continuous Deployment (CI/CD)
* Infrastructure as Code (IaC) Basics
* Application Programming Interfaces (APIs)
* [RosettaCode](http://www.rosettacode.org/wiki/Hello_world/Text)
* Installing `python3` with `sudo yum install python3`

### Day 5
* Personal branding workshop
* Python String data type `str`
* Python Numerics data types `int`, `float`
* Print to console `print()`
* Takes input from console `input()`

# Week 2

## Core Topics
* Python Basics
* Git Basics

### Day 1
* Python: Lists `my_list = [1, "hello", 3.14]`, Tuples `my_tuple = (4, "blah", 1.23)`
* Functions (`def my_function():`)
* Conditionals (`if`/`else`/`elif`)
* Comments (`#`)
* Debugging: Breakpoints, Stepping, Inspecting values

### Day 2
* Python Dictionaries `my_dictionaries = {"innovation": "something new"}`
* Python Boolean type `my_bool = True | False`
* Nested data types: Lists within Dictionary, Dictionaries within List, Lists within List (2D array)
* Using `pip`
* [awesome-python](https://github.com/vinta/awesome-python) - List of popular Python packages
* Using `pylint`
* Local vs. Global scope
* Classes (basics - grouping of data and functions/methods)
* Interpreted programming languages vs compiled programming languages
* AI brief introduction - Tensorflow, Keras, PyTorch
* Sets `my_set = {1, 3, 'hello', 3, 5}`, Intersection and Union methods
* List slices & some methods (append, insert)

* [Keybr.com](https://www.keybr.com/) - Learn to touch type & speed up your typing.

### Day 3
* Python conditionals: `if`, `elif`, `else`
* Exceptions, custom exceptions with `raise`, `try`, `except`, `else`, `finally`
* Combine exception handling with functions and `return`
* `assert` and raising `AssertionError`
* [Sentry](https://sentry.io) for error tracking
* Create / `import` modules in Python
* Using `pytest` and `assert` statement for software testing.
* Continuous Integration providers: Travis-CI, CircleCI
* [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development) basics: Standups, Kanban, Sprints, [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))
* GitHub platform in depth: Forking, Pull requests, Topics, Issue tracking, Project Management, Contributors / Bus Factor, etc

### Day 4
* Using loops (`while`, `for`, `range`, `enumerate`)
* List comprehensions aka easily making a list from an iterable.
* Looping through dictionaries using `.keys()`, `.values()`, and `.items()`.
* Printing with `f-strings`
* More testing with `pytest`
* More on using modules
* [Entry point](https://en.wikipedia.org/wiki/Entry_point)
* Python's `in` keyword (`'b' in ['a', 'b', 'c']`, and in `for` loops)
* Using `turtle` for small visualizations and understanding loops

### Day 5
* How git is used for teams of software engineers to collaborate
* How to create a Github repo, also called a `remote` repository
* `git clone` from `remote` repository
* `git init`
* `git add remote` if there isn't `remote` repository linked already
* see status of staged and unstaged changes with `git status`
* view git history with `git log`
* `git commit`
* `git branch`
* `git checkout`
* `git pull` from `remote` repository
* `git push` from local to `remote` repository
* rewrite git history, squash N number of commits history with `git rebase -i HEAD~N`

# Week 3

## Core Topics
* Linux Basics (Filesystem layout, navigating, working with files/processes)

### Day 1
* Kernel / Daemons
* Python Revision
* Command Line Revision
* Git Revision

### Day 2
* Linux Basics Revision
* Linux GUI vs CLI
* Continuous Integration, Continuous Delivery, Continuous Deployment concepts
* `which`, `alias`, `unalias`, `export`, `unset`, `env`, `less`, `sudo !!`, `cat`, `sleep`
* `PATH`, accessing environment variables e.g. `$HOME` and setting `PATH`, `.bashrc` basics. 
* `/proc` basics
* Processes & Process ID's
* Job control basics: `Ctrl-Z`, `bg`, `fg`, Running a task in the background with `&`
* `strace` basics & system calls (syscalls) overview/purpose
* File Descriptors and `/proc/<process_id>/fd/`, `stdin`, `stdout`, `stderr` - More on these later.
* tmux Basics: Prefix key (`Ctrl-B`), Vsplit `%`, Hsplit `"`, New window `c`, Next window `n`, Previous window `p`, Switching panes `arrow keys`
* Types of interprocess communication: [Wikipedia - Inter-process Communication](https://en.wikipedia.org/wiki/Inter-process_communication)

### Day 3
* More Linux: `head`, `tail`, `file`, Symbolic Links (symlinks), Permission basics: `chmod +x` (so far)
* `/etc/passwd`
* `chsh`, `/etc/shells` and different shell examples (`zsh`, `fish`)
* `gcc` (aka `cc`) and compiling simple C programs
* `/lib` directory, shared objects (`.so` and equivalent `.dll` files)
* Binary ([ELF](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format)) vs Text ([Shell script](https://en.wikipedia.org/wiki/Shell_script)) and `#!` at the top of scripts.
* Using `time.sleep(30)` in Python and the `nanosleep()` syscall.
* Created a simple shell script
* [awesome-shell](https://github.com/alebcay/awesome-shell) - List of great programs

### Day 4
* Linux `cd`, `pwd`, `ls *` (list all files in nested folders) vs. `ls`
* `cp`, `mv`, `mkdir`, `nano`
* Python `argsparser` to run Python program with customizable input
* Makefile, and Makefile command with input
* Makefile command shortcut to run Python program with customizable input
* Explained on a high level what API is, and most common API command `GET`, `POST`, `PUT`, `DELETE`
* More Linux: `useradd`, `groupadd`, `sudo su -`, `/etc/sudoers`, `/etc/passwd`, `/etc/group`, `/etc/shadow`, `vipw`, `vigr`, and `vipw -s` (don't edit these files directly)
* `!!`, `!$`, `history` and `!<n>`
* More Bash scripting & handling arguments (`$1`, `$2`, etc in Bash & `sys.argv` in Python)
* Linux permissions: [chmod codes cheat sheet](https://gist.github.com/juanarbol/c44e736be70279c1fd5d68aa24f9d8be), `ugo+rwx` (symbolic), `421` (numeric), output of `ls -al`
* [LinuxJourney.com](https://linuxjourney.com/) - Thanks Ben
* [Bash Cheat Sheet](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh) - Plan to learn these during your career

Optional vim stuff:
* [Vim Adventures](https://vim-adventures.com/) - Thanks Jarryd
* [VSCode Vim Plugin](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim) - Optional
* [VSCode Learn Vim Plugin](https://marketplace.visualstudio.com/items?itemName=vintharas.learn-vim) - Also optional
* [Advanced vim cheatsheet](https://vim.rtorr.com/) - Bookmark for later in your career if you decide to use vim.

### Day 5
* CV workshops
* Flows and conditions with Linux bash scripting: `if else elif`, `for loop with {1..N}`, `for loop with StringArray()`, `case`, `conditions []`

Other resources for interview preps:
* Algorithm coding interview: https://leetcode.com/
* All topics in Tech interview: https://interviewing.io/
* General programming interview, not algorithm heavy: https://exercism.org/ 
* System design interview: https://github.com/donnemartin/system-design-primer

Book recommendations:
* https://www.amazon.com/System-Design-Interview-Insiders-Guide-ebook/dp/B08B3FWYBX
* https://www.amazon.com/System-Design-Interview-Insiders-Guide/dp/1736049119

# Week 4

## Core Topics
* Networking Basics: Switches, Routers, TCP vs UDP, IP addresses, Ports

### Day 1
* Revision
* More on containerization vs virtualization.
* Architecture Basics: ARM vs x86 / x64 (aka amd64 or x86_64)
* Virtualbox Snapshots & Amazon Machine Images
* Demos/Presentations of useful utilities
* Debugging a non-ELF binary named `googlr` (created in Swift)
* Matthew: `atop`, `gitmux`, `nnn`
* [Dotfiles](https://dotfiles.github.io/) - Configure your own setups.
* Joe: `image-scraper`, `imgp`, `tiv`, and cool mod to Alice's pokemon guesser game
* Asimina: `cointop`, `has`
* Michael J: `prettyping`, `gogh` & debugging shell scripts
* Custom tmux configuration with [.tmux](https://github.com/gpakosz/.tmux)
* Installing Python 3.10 from source and using `grep`.
* Installing Go (see office hours recording) and extracting compressed files with `tar`.
* Installing Rust (also office hours)

[Software Engineering advices](https://www.amazon.com/gp/product/B073X6GNJ1/ref=dbs_a_def_rwt_hsch_vapi_tkin_p1_i1):
* Keep many CVs
* [Job tracking pipeline](https://enhancv.com/)
* [Learning plan](https://roadmap.sh/)
* [Manage learning pipeline](https://asana.com)
* Career progression (the technical track & the management track)
* Negotiation (pay, parking or gym perks, more WFH days, learning and certification stipends...)
* [Keeping and building a code snippet library](https://gist.github.com/) - curated pieces of code for Python, Bash...

### Day 2

* Router, Switch vs. Hub
* LAN vs. WAN
* IP vs. MAC
* Client Server vs. Peer to Peer
* Bus, Star, Mesh topologies and how you can go hybrid
* Introduce network layers, highlight layer 4 (TCP and UDP) and layer 7 (HTTP)
* Connection vs. Connectionless (session-less) protocol
* Binary & Hexadecimal - [Hexadecimal to Binary - Organic Chemistry Tutor](https://www.youtube.com/watch?v=D_YC6DSPpQE)
* Endianness: [Wikipedia](https://en.wikipedia.org/wiki/Endianness), [Computerphile](https://www.youtube.com/watch?v=NcaiHcBvDR4)
* Hex Editors: [HxD - Windows](https://mh-nexus.de/en/hxd/), [Hexinator - Linux](https://hexinator.com/hexinator-linux/), [HexFiend - MacOS](https://hexfiend.com/)
* [ASCII](https://www.ascii-code.com/)
* IPv4 Addresses
* Ports - [List of common port numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
* [Regional Internet Registries](https://en.wikipedia.org/wiki/Regional_Internet_registry)
* [ROT13 cipher](https://en.wikipedia.org/wiki/ROT13)
* Utils: `whois`, `nslookup` & DNS basics (A-record), `iftop`, `tcpdump`
* [Shodan](https://www.shodan.io/) & [Honeypots](https://en.wikipedia.org/wiki/Honeypot_(computing))

### Day 3

* IPv4 vs. IPv6
* CIDR
* VPC, Subnets, Avaiability Zone, Regions
* How VPC can connect together
* The concept of CDN in an example related to Netflix content distribution
* History of IP Address allocation
* Classful Addressing
* [IPv4 Address Exhaustion - Wikipedia](https://en.wikipedia.org/wiki/IPv4_address_exhaustion)
* [List of assigned /8 Blocks assigned to RIR's](https://en.wikipedia.org/wiki/List_of_assigned_/8_IPv4_address_blocks)
* [ipcalc](http://jodies.de/ipcalc) for CIDR & Subnetting
* `whois`ing IP ranges from [countryipblocks.net](https://www.countryipblocks.net/acl.php) and seeing who owns what.
* Feynman Technique for understanding and remember something: [Socratica](https://www.youtube.com/watch?v=q-16DPh_VWw), [Thomas Frank](https://www.youtube.com/watch?v=B8V5EfJLX9U)

### Day 4

* Private, Partnered (Paid), and Public APIs
* REST vs. gRPC vs. SOAP
* JSON vs. dictionary
* JSON vs. XML vs. Protobuf
* Building an IP Subnetting calculator API with Python, pytest, and FastAPI. 

### Day 5
* Friday: Good Friday (No class)

# Week 5

## Core Topics
* More Networking Basics: OSI & TCP/IP Models, IPv4 Subnetting

### Day 1 (Tuesday, no class on Easter Monday)
* Review of the following networking topics:
* OSI Model & TCP/IP Model
* Example: VPN -> OSI Layer 3 tunneling to by pass IP and domain name restriction
* Example: Network firewall -> OSI Layer 4, block IP address range and port range
* Example: Application firewall -> OSI Layer 7, looking at body of requests to intercept application level attack such as SQL injection
* Network Topology
* Ethernet and Switches (vs Hubs)
* Media Access Control (MAC) addresses
* Address Routing Protocol (ARP): Requests, Responses, and Spoofing/Poisoning
* Spearphishing and some OSINT
* Internet Control Message Protocol (ICMP, used for pings). Time To Live (TTL)
* Network Address Translation (NAT)
* Request For Comments (RFC's - Documents used for describing protocol specifications among other things)
* [Wireshark](https://www.wireshark.org/)
* [Tom7 - Using ICMP as a hard drive for SIGBOVIK'22](https://youtu.be/JcJSW7Rprio?t=146)
* [NetworkChuck - NAT](https://www.youtube.com/watch?v=8bhvn9tQk8o)
* [Professor Messer - OSI Model](https://www.youtube.com/watch?v=owDh6FNJUog&list=PLG49S3nxzAnlCJiCrOYuRYb6cne864a7G&index=2)
* [Professor Messer - Spoofing](https://www.youtube.com/watch?v=jUWgEowyvJE&list=PLG49S3nxzAnlCJiCrOYuRYb6cne864a7G&index=74)

### Day 2
* More VPC & Subnets, NAT, Internet Gateway, Security Group (layer 4 firewall)
* Public subnet, private subnet
* Security basics: Encryption in transit, encryption at rest, intelligent threat detection, anti virus/malware software
* Bitwise Operators: NOT `~`, AND `&`, OR `|`, XOR `^`, Shift-Left `<<`, Shift-Right `>>`, and Rotate Left/Right (no operator in Python).
* Subnetting deep dive.
* [SubnettingPractice.com](https://subnettingpractice.com/)

### Day 3
* Emerging networks: 5G, long range BlueTooth, IoT networks and applications
* VPC lab demonstration for creating VPC, Subnets, and NAT Gateway - Lab 52 in Modules
* Preparing for Interviews: Technical (technology you are learning vs. technology you know vs. similar technology you know vs. technology you cannot relate), and Behavioral (including scenarios based - tell a time me when you run into a conflict with co-worker, and open ended questions - tell me where you will be in 5 years time)
* Files
* Python's `with` keyword (context manager basics) and where you want to use it.
* Windows Registry
* Structs (examples in different programming languages)
* Classes & Objects / OOP Basics (`__init__ method`, `self`, `methods`, basic inheritance).

### Day 4
* Install Node.js, create React.js app with `npx create-react-app my-app`

# Week 6

## Core Topics
* HTML, CSS, and JavaScript Basics
* ReactJS Basics (stateless & stateful components)

Monday: ANZAC Day (No class)

### Day 1
* More React.js - started building a TODO App
* NodeJS & npm basics
* [HTML Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
* JS Basics: `var` vs `let` & `const`, defining `function`s
* Creating simple stateless components and basic use of `props`.

### Day 2
* ReactJS: `useState()` hooks, onClick events, event handler functions, events in React, create a counter with React
* CSS: id vs classes
* Threads, Multiprocessing
* Intro to async/await and `fetch()`

### Day 3
* ReactJS: `useRef()` hooks, get values out of a ref `name = myRef.current.value`, change value of element linked to ref `myRef.current.value = "new value"`, deconstructing a JavaScript array (only in ES6 JSX) with `new_list = ["new_item", ...my_list]`, validating input within a handler functions, `list.map()` to create a list of components
* Building a simple Todo list
* Connecting React frontend to FastAPI backend
* [FastAPI - Cross-Origin Resource Sharing (CORS)](https://fastapi.tiangolo.com/tutorial/cors/)
* [Cross-Origin Resource Sharing (CORS) MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) - Recommended reading

### Day 4
* Interview practice
* ReactJS: `useEffect()`, using `useEffect` to react to change of any particular state, if `useEffect` does not subscribe to anything -> will run once in the first render -> use this to initialize all data
* FastAPI: backend API with `GET request` to get data out of a `.json` file, and `POST request` to update the `.json` file
* Combine ReactJS + FastAPI: the simple Todo web app that can fetch initial data from file, and add more data to file. Reopenning the app will not lose data
* Homework: create a delete button on the React.js app, and make sure that all data is clear, test by refreshing the web browser

# Week 7

## Core Topics
* Database Basics
* Security Basics

### Day 1
* Revision: Linux, Git & GitHub, React, Parallels between Python & JavaScript, HTTP GET/POST, API setup
* Database Basics

### Day 2
* SQLite & [SQLite Sample Database](https://www.sqlitetutorial.net/sqlite-sample-database/)
* [SQLite Browser](https://sqlitebrowser.org/)
* SQL: `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`
* Connecting database to API
* [Computerphile - The Problem with Time & Timezones](https://www.youtube.com/watch?v=-5wpm-gesOY)
* Data Modeling Basics & [Entity-Relationship Diagrams](https://www.guru99.com/er-diagram-tutorial-dbms.html)
* Relations: One-to-One, Many-to-One/One-to-Many, Many-to-Many, Cardinality
* [Crypto Museum](https://cryptomuseum.com/)

### Day 3
* SQL string searching with `LIKE`
* get data from multiple tables with `JOIN`
* table short names
* multiple `JOIN`
* multiple `JOIN` with conditions `WHERE`
* [JetBrains DataGrip - Free for Students](https://www.jetbrains.com/datagrip/)
* Cryptography: Brief History, Ciphers (Caesar, Polybius, Cipher Machines), Feistel Network
* XOR operation, Block vs Stream Ciphers, Symmetric vs Asymmetric (Public Key) Cryptography
* [The Codebreakers Book by David Kahn for more history](https://archive.org/details/B-001-001-264)
* Certificate Authority Basics (and DigiNotar/Comodo hacks), browsers Chain of Trust
* Hashing Basics (Block size, Digest Size, MD5 / collisions, Pigeon-hole Principle, SHA3 contest)

### Day 4
* table relationships, dependency, order for adding and removing entries for inter-dependent tables (`ADD artists -> albums -> tracks` and `DELETE tracks -> albums -> artists`)
* `INSERT INTO` sql statement
* `DELETE` sql statement
* Back to React homework: button to remove all contents from Todo List
* Solving duplicate key problem for a List of `<div>`
* Guest Speaker: Thiago Canestraro
* More security: Hashing / Blockchains
* Recommended platforms for more cybersecurity: [TryHackMe](https://tryhackme.com), [HackTheBox](https://hackthebox.com) (in office hours)

### Day 5
* Presentation practice rounds, demo of highlights, sharing own plans with class
* DataGrip SQL IDE tutorials
* Revise React.js: `useState`, `useRef`, `useEffect`
* Todo App with complete checkbox and remove button


# Week 8

## Core Topics:
* Cloud

### Day 1
* React.js deployment Part I
* CI/CD concepts revisit
* Security revision: Symmetric vs Asymmetric (Public Key) Cryptography. Diffie-Hellman & RSA concepts.
* SSH, `ssh-keygen`, public key authentication (authorized_keys file, private key permissions)
* AWS Console vs `awscli`

### Day 2
* React.js deployment Part II (folder deployment_day_1)
* More SSH stuff
* Understanding an HTTP request
* Security Groups & `iptables` (Firewall) demo
* netcat & usage of sockets for networked services
* EC2 overview

### Day 3
* React.js & FastAPI deployment Part III (folder deployment_day_1)
* Secure password storage (bcrypt, scrypt, Argon2)
* [HaveIBeenPwned](https://haveibeenpwned.com/)
* Digital signature basics
* DNS and `dig`: (A, AAAA, CNAME, NS, MX, TXT, PTR records)
* Brief mention of Amazon SES (Simple Email Service)
* Containers Concepts & Docker installation

### Day 4
* Deploying a static site to S3 Part IV (folder deployment_day_2)
* Guest Speaker: Ash
* EC2 deep dive
* [AWS Cost Calculator](https://calculator.aws/)
* RDS & ElastiCache brief mention

### Day 5
* Linkedin workshop
* Docker: build and run
* Deploying a FastAPI app to Docker
* Docker port mapping
* Homework: deploy React.js from `react_day_6` with Docker, entry point is using `serve`

# Week 9
## Core Topics:
* Cloud

### Day 1
* Deploy React.js from `react_day_6` with Docker, entry point is using `serve`
* Docker Compose intro 
* Environment variable intro
* "Serverless" Computing with ([AWS Lambda](https://aws.amazon.com/lambda/))
* Different triggers for Lambda
* [Serverless Examples - FFMpeg to GIF](https://github.com/serverless/examples/tree/v3/aws-ffmpeg-layer) - Supplementary. Not required for the course.

### Day 2
* More deployment with Docker
* Virtual Private Cloud (VPC), Subnets, Route tables, Internet Gateways & deploying Web/Database servers to different subnets
* Infrastructure as Code (IaC) Concepts (CloudFormation, Terraform, Pulumi)

### Day 3
* More IaC: Pulumi & CloudFormation
* S3 & S3 Glacier
* Python virtualenvs (`python -m venv venv` and `source venv/bin/activate`)

### Day 4
* AWS IAM: User, Policy (Effect, Action, Resource), Role (User, Service, Cross Account)
* AWS CloudTrail: all API calls to AWS account are saved here
* Issue Tracking & Project Management
* Assignment Tips
* PowerShell
* EC2 Deployment & Elastic Block Store (EBS) Basics

### Day 5
* System Manager (Session Manager, Patch Manager, Compliance, Parameter - string and secrets)
* CloudWatch Metrics (given by default, and also Custom Metrics like RAM and %Drive)
* CloudWatch Alarms
* Auto Scaling Group
* EC2 Launch Template

# Week 10

### Day 1

* AWS ELB - Application vs. Network load balancing


|                                    | Application Load Balancer                                 | Network Load Balancer                                       |
|------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------|
| OSI Layer                          | Layer 7                                                   | Layer 4                                                     |
| Target                             | **Private/Public IP,  EC2 instance in ASG,  Also Lambda** | **Private/Public IP,  EC2 instance in ASG**                 |
| Protocol                           | HTTP/HTTPs/gRPC                                           | TCP/UDP/TLS                                                 |
| **LB Static IPs**                  | **No**                                                    | **Yes**                                                     |
| Session                            | Yes                                                       | Yes (new*)                                                  |
| Forward source IP                  | Yes (new*)                                                | Yes                                                         |
| Cross-AZ balancing                 | Yes (by default)                                          | Yes (not by default)                                        |
| SSL Offloading                     | Yes                                                       | Yes (new*)                                                  |
| **Authentication**                 | **Yes**                                                   | **No**                                                      |
| **Private network load balancing** | **Yes**                                                   | **Yes**                                                     |
| Typical applications 1             | General backend with Application level awareness          | Low latency media streaming (UDP) & connectivity (Gaming)   |
| Typical applications 2             | Complex authentications supported (SAML/LDAP/AD)          | Use static IPs to share/receive data with partner companies |


* Web Security
* [OWASP Top 10](https://owasp.org/Top10/)
* MITRE [ATT&CK](https://attack.mitre.org/) & [D3FEND](https://d3fend.mitre.org/)
* [CyberChef](https://cyberchef.org/) & Decoding Base64-encoded JWT's
* [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar)
* [HackerNews](https://news.ycombinator.com/)
* [Flow Charts - Group Exercise](https://en.wikipedia.org/wiki/Flowchart)
* [Sourcegraph Dev Tool Time Playlist](https://www.youtube.com/watch?v=GXxvxSlzJdI&list=PL6zLuuRVa1_iDEP4EicZ8972RgyccCRGF&index=2) - Has developers talking about their workflows

### Day 2

* FastAPI body, query string, input parameters
* Usecases for Docker ENV - default environment variable + dependency versioning
* EC2 Instance Store vs. EBS backed
* Type of EBS drives, and appropriate usecases for each
* SSH/Apache log files, hardening & configuration
* Sockets & Building network services with Python
* Analysis of log files with Python & UNIX utils
* Monitoring Basics (more to follow)

### Day 3

* React `props` and `children` (see react_day_8 folder)
* More on React
* Review of UI Component Libraries
* Review of programming paradigms & concepts
* [CodeWars](https://www.codewars.com/)

### Day 4

* CloudFront and benefits of CDN (security, cost, user experience)
* CloudFront usecases for caching static content: website hosting, paid content distribution, Lambda at Edge A/B testing, rerouting HTTP to HTTPS
* CloudFront usecases for caching dynamic content: Load Balancer distribution, HTTP response caching
* API gateway vs. Load Balancer
* Object Relational Mappings (ORMs)
* Abstracting interaction with databases
* Docker revision

### Day 5

* Meeting with [Spark](https://www.spark.co.nz/), [Datacom](https://datacom.com), and [Leaven](https://www.leaven.co.nz/).
* Continuation of CloudWatch with CloudWatch Logs (comparable to LogStash + ElasticSearch)
* ELK stack: LogStash for collecting log files, ElasticSearch for log searching and metrics generation, Kibana for visualizing metrics (comparable to CloudWatch dashboard)
* Billing console, billing report per product/department with Resource Tag
* StepFunction state machine, enabling more usecases with Lambda function
* RDS/Aurora - sync replication thinking of FailOver instance, async replication thinking of Read Replica
* Queue vs. Topic, Kafka overview concepts - topics, partition, replication factor...

# Week 11

### Day 1

* Topics vs. Queue revision
* Publish subcribe (subcribers are not aware of publisher) vs. Observer pattern (the opposite)
* SNS - push based - has many types of subscriber (email, txt messages, HTTP/HTTPs destination, SQS, Lambda...)
* SQS - pull based - for simple queue, if item pulled out -> item becomes invisible to other pollers
* ElastiCache in more depth
* RDS in more depth
* [CloudQuest](https://cloudquest.skillbuilder.aws/)
* [Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials)

### Day 2
* Migration with RDS
* Route53 & DNS revision
* nginx configuration & examples of using DNS
* [HowDNS.works](https://howdns.works)
* ElasticBeanstalk
* More docker revision

### Day 3
* Solution Architect discussion & [AWS Reference Architecture Diagrams](https://aws.amazon.com/architecture/reference-architecture-diagrams/)
* [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)
* Volumes (EBS, docker, and docker compose)
* Architecture for full-stack applications w/ both docker compose & AWS (frontend, backend, cache, db, queue)
* Cloud Practitioner Vouchers & Booking Exam Info
* Supplementary [Fireside Chat w/ Geoffrey Hinton](https://www.youtube.com/watch?v=UTfQwTuri8Y) relating to designing software after physical/biological systems.

### Day 4
* Advanced EC2 features - pricing models (Spot, Reserve, On demands), Placement Group, Host settings
* DMS - Database Migration Service (one off mode and continuous replication mode, schema migration tool to convert MySQL to PostgreSQL)
* General AWS limits (S3 APIs, EC2 number of instances, ECS number of tasks...)
* Presentation Practice
* Practice Test for Cloud Practitioner exam

### Day 5
* More AWS practice exam here [20 free practice questions for all exams](https://explore.skillbuilder.aws/learn/course/9153/play/30290/access-instructions-aws-certification-official-practice-question-sets-english)
* Advising on topics selection for the marked presentation [source for basic topics](https://aws.amazon.com/getting-started/hands-on/), [source for advanced topics](https://aws.amazon.com/prescriptive-guidance/)
* AWS CodeCommit, CodeBuild, CodeDeploy, CodePipeline
* In place deployment, Blue/Green deployment

# Week 12

### Monday: Queen's Birthday (No class)

### Day 1 - Presentations:

* Maria: S3 Static Website Hosting
* Allan: Terraform
* Matthew K: Scraping with BeautifulSoup
* Matthew R: Elastic Beanstalk
* Michael J: Automation with python and awscli
* Jarryd: AWS Amplify
* Heaven: CloudWatch
* Eden: Creating a portfolio with React
* Tahseena: Setting up and using load balancers
* Sheldon: Using IoT TwinMaker
* Robert: EC2 autoscaling
* Nisheeth: Using DynamoDB
* Nick C: Using AWS Kendra 
* Asimina: Intro to TypeScript
* Wiremu: IP crawler that downloads certificates
* Joe Zhu: Using Pulumi to deploy a backend API server to AWS EC2
* Ben Browning: AWS Lambda
* Myat Lwin: Create Custom VPC with Public&Private Subnets
* John Simmons:  AWS Comprehend
* Alice Kokado: Boto3 Python SDK
* Xinpeng Yang: AWS Lightsail
* Kumar AWS EC2 Backup

### Day 2
* More Presentations
* Another Practice Test
* Meeting with [Sky](https://www.sky.co.nz/)

### Day 3
* Remaining Presentations
* Test
* [Anki](https://apps.ankiweb.net/) - Spaced-Repetition Flash Cards (see the Cloud Practitioner deck in this repo)
* [DigitalCloud.training - AWS Cloud Practitioner Cheat Sheets](https://digitalcloud.training/category/aws-cheat-sheets/aws-cloud-practitioner/)
* [AWS.PlainEnglish.io - Cloud Practitioner Study Notes](https://aws.plainenglish.io/aws-cloud-practitioner-study-notes-2021-64fa18b9121b)
* [Notes for Cloud Practitioner](https://gist.github.com/kkadete/ce7af949c5fef86fa9955ad4873d18da)
* [FreeCodeCamp - Cloud Practitioner 2020](https://www.youtube.com/watch?v=3hLmDS179YE) - Supplementary video on preparing for CloudPrac exam. Caution: Some things have changed since then.

### Day 4
* Revision
* Assignment help
* Congratulations!

# More AWS services to cover in Week 9-12:
* [x] EC2
* [x] IAM
* [x] Lambda
* [x] S3
* [x] Virtual Private Cloud (VPC), Subnets, Route tables, Internet Gateways
* [x] System Manager (Session Manager, Patch Manager, Compliance, Parameter - string and secrets)
* [x] CloudWatch Metrics (given by default, and also Custom Metrics like RAM and %Drive)
* [x] CloudWatch Alarms
* [x] Auto Scaling Group
* [x] EC2 Launch Template
* [x] Elastic Load Balancer
* [x] EBS + EC2 Instance Store (IOPS calculation)
* [x] CloudFront (how this relate to Load Balancer, S3, and APIGW)
* [x] Route 53
* [x] Elastic Beanstalk
* [x] StepFunction (more Lambda)
* [x] RDS/Aurora
* [x] ElastiCache
* [ ] RedShift
* [x] DMS
* [ ] EFS (NFS)
* [x] S3/Glacier
* [ ] Storage Gateway

# Advanced services to cover to cover in Week 9-12:
* [x] SNS
* [x] SQS
* [x] CloudWatch Logs
* [x] CloudTrail
* [ ] Organizations
* [x] Tagging
* [x] Billing
* [x] Code Commit, Code Build, Code Deploy
* [x] IaC, CloudFormation

# Projects ideas 

Intended for team of up to 3 people, lasting 4 weeks

|                                                                    Projects ideas | Difficulty   | Nature                                                | Suggested Week 1 milestone                                                                                                                                                                                                      | Suggested Week 2 milestone                                                                                                     | Suggested Week 3 milestone            | Suggested Week 4 milestone                                                                      |   |
|----------------------------------------------------------------------------------:|--------------|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|-------------------------------------------------------------------------------------------------|---|
|                                                        Real-time World Statistics | Medium       | Frontend development + Cloud Native Hosting           | Identify data source (eg. [Covid data](https://covidtracking.com/data/api)),  wide frame design for the visualization website, identify a place to host the website (eg. S3+Cloudfront), finalize the scope of work             | 40% of planned work                                                                                                            | 80% of planned work                   | 100% of planned work,  Team presentation + Demo, figure out future directions for this projects |   |
|                                            A fully functioning e-Commerce Website | Low - Medium | eCommerce platform management + Cloud Native Hosting  | Identify eCommerce platform (eg. [Magento on LightSails](https://aws.amazon.com/getting-started/hands-on/magento-on-aws/), or EC2), and products to sell, finalize the features of the eCommerce website                        | 40% of planned work                                                                                                            | 80% of planned work                   | 100% of planned work,  Team presentation + Demo, figure out future directions for this projects |   |
|                                               A Blogging (News aggregate) Website | Low - Medium | CMS platform management + Cloud Native Hosting        | CMS engine for the Blog/News website (WordPress, Gatsby...), wide frame design for the Blog/News website, identify a place to host the website (eg. S3+Cloudfront, or LightSail, or EC2), choose and finalize the scope of work | 40% of planned work                                                                                                            | 80% of planned work                   | 100% of planned work,  Team presentation + Demo, figure out future directions for this projects |   |
| [A Habit tracking app]( https://www.lifehack.org/668261/best-habit-tracking-apps) | Hard         | Backend + Frontend development + Cloud Native Hosting | Identify authentication provider (AWS Cognito or Google Firebase), wide frame design for the web application, design a cloud native architecture (eg. APIGW+Lambda+S3+CloudFront), choose and finalize the scope of work        | All the basic infrastructure components such as Authen provider, static web hosting infras, API gateway and backend components | Basic logins and half of the features | 100% of planned work,  Team presentation + Demo, figure out future directions for this projects |   |
|                                     A project management app (extension of Todos) | Hard         | Backend + Frontend development + Cloud Native Hosting | Identify authentication provider (AWS Cognito or Google Firebase), wide frame design for the web application, design a cloud native architecture (eg. APIGW+Lambda+S3+CloudFront), choose and finalize the scope of work        | All the basic infrastructure components such as Authen provider, static web hosting infras, API gateway and backend components | Basic logins and half of the features | 100% of planned work,  Team presentation + Demo, figure out future directions for this projects |   |
|                                                                                   |              |                                                       |                                                                                                                                                                                                                                 |                                                                                                                                |                                       |                                                                                                 |   |
|                                                                                   |              |                                                       |                                                                                                                                                                                                                                 |                                                                                                                                |                                       |                                                                                                 |   |
|                                                                                   |              |                                                       |                                                                                                                                                                                                                                 |                                                                                                                                |                                       |                                                                                                 |   |
|                                                                                   |              |                                                       |                                                                                                                                                                                                                                 |                                                                                                                                |                                       |                                                                                                 |   |
|                                                                                   |              |                                                       |                                                                                                                                                                                                                                 |                                                                                                                                |                                       |                                                                                                 |   |
|                                                                                   |              |                                                       |                                                                                                                                                                                                                                 |                                                                                                                                |                                       |                                                                                                 |   |
|                                                                                   |              |                                                       |                                                                                                                                                                                                                                 |                                                                                                                                |                                       |                                                                                                 |   |
