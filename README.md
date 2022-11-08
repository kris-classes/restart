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

# YouTube Channel Recommendations
* [freeCodeCamp.org](https://www.youtube.com/c/Freecodecamp)
* [Computerphile](https://www.youtube.com/user/Computerphile)
* [Socratica](https://www.youtube.com/c/Socratica)
* [Harvard CS50](https://www.youtube.com/c/cs50)
* [Adrian Cantrill](https://www.youtube.com/c/LearnCantrill)
* [Theo Browne](https://www.youtube.com/c/TheoBrowne1017)
* [David Bombal](https://www.youtube.com/c/DavidBombal)
* [Programming with Mosh](https://www.youtube.com/c/programmingwithmosh)
* [TechWorld with Nana](https://www.youtube.com/c/TechWorldwithNana)
* [The Coding Train](https://www.youtube.com/c/TheCodingTrain)
* [devaslife](https://www.youtube.com/c/devaslife)
* [Fireship](https://www.youtube.com/c/Fireship)
* [IppSec](https://www.youtube.com/c/ippsec)
* [NahamSec](https://www.youtube.com/c/Nahamsec)
* [JohnHammond](https://www.youtube.com/c/JohnHammond010)
* [BillBuchanan](https://www.youtube.com/c/BillBuchanan)
* [LiveOverflow](https://www.youtube.com/c/LiveOverflow)
* [MarcusHutchins](https://www.youtube.com/c/MalwareTechBlog)
* [STÖK](https://www.youtube.com/c/STOKfredrik)

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
* Networking Basics: IPv4, Ports, DNS (A and CNAME records)
* `dig`, `whois`, `nc`
* Supplementary: [Spreeder - Improving reading speed](https://www.spreeder.com/app.php), [KeyBR - Improving typing speed](https://www.keybr.com/), [Illegal Numbers](https://en.wikipedia.org/wiki/Illegal_number), [Regional Internet Registry](https://en.wikipedia.org/wiki/Regional_Internet_registry)


# Week 4
## Day 1
* Python modules, JSON basics
* Exceptions
* Python's `with` keyword (context manager concept)
* `fastapi` and `uvicorn` basics
* Basics of project scoping, requirements gathering, data modeling basics
* Supplementary: [Billion laughs attack](https://en.wikipedia.org/wiki/Billion_laughs_attack) - Bug with deserialization
* [Architecture of Open Source Applications (AOSA Books)](http://www.aosabook.org/)

## Day 2
* Python's `http.server` and `pydoc` modules
* Interfaces & interacting with [APIs](https://github.com/public-apis/public-apis)
* User Agents, robots.txt, `Host:` header
* Using Python decorators with `fastapi`
* Public vs Private IP addresses, Loopback Interface/Localhost, Port Scanning 

## Day 3
* TCP, UDP
* RFC's
* Wireless Networking & WiFi

## Day 4
* Network Topology
* OSI Model, TCP/IP Model
* Ethernet, [MAC Addresses](https://en.wikipedia.org/wiki/MAC_address), [MAC Spoofing](https://en.wikipedia.org/wiki/MAC_spoofing)
* Wireshark basics
* Hexadecimal basics

## Day 5
* Revision & More on Python Classes

# Week 5
## No class on Monday - Public Holiday

## Day 1
* Hashing Basics
* VirusTotal
* Brute-forcing & probabilities
* CRUD applications

## Day 2
* Cybersecurity: [ExploitDB](https://www.exploit-db.com/), [GHDB](https://www.exploit-db.com/google-hacking-database), [ATT&CK](https://attack.mitre.org/), [D3FEND](https://d3fend.mitre.org/about/), [OWASP Top 10](https://owasp.org/Top10/)
* Scraping

## Day 3
* Binary, Hexadecimal
* ASCII
* Hex editors & other instances where you encounter hex
* [TryHackMe.com](https://www.tryhackme.com)


## Day 4
* Blockchain technical details
* Reading other programming languages (Rust/Go) 


# Week 6

## Day 1
* Subnetting
* [Subnet Calculator 1](https://jodies.de/ipcalc)
* [Subnet Calculator 2](https://www.site24x7.com/tools/ipv4-subnetcalculator.html)

## Day 2
* More EC2, some VPC
* IaaS, PaaS, SaaS, etc
* More networking labs

## Day 3
* More EC2

## Day 4
* More Cryptography Basics
* IAM Basics
* EBS (Elastic Block Store) & File system basics

## Day 5
* RDS
* SQL Basics

# Week 7
## Day 1
* More RDS
* Docker
* Single-Page Application Basics
* Base64 Encoding
* Cookie vs JWT Basics

## Day 2
* More Docker
* [redis](https://redis.io/)

## Day 3
* More Docker

## Day 4
* [`awscli`](https://github.com/aws/aws-cli)
* [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* S3 (Simple Storage Service)
* [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)

## Day 5
* Revision

# Week 8

## Day 1
* [AWS SkillBuilder - Cloud Practitioner Essentials](https://explore.skillbuilder.aws/learn/course/external/view/elearning/134/aws-cloud-practitioner-essentials)
* [AWS SkillBuilder - Cloud Quest](https://explore.skillbuilder.aws/learn/course/external/view/elearning/11458/aws-cloud-quest-cloud-practitioner)
* [Faker](https://github.com/joke2k/faker/)
* ElastiCache w/ Redis
* [Redis-Py](https://redis-py.readthedocs.io/en/stable/)
* [SQLite Sample Database - Sakila Rental](https://github.com/krp/sakila-sqlite)
* [SQLite Browser](https://sqlitebrowser.org/)

## Day 2
* More SQL
* Industry Meeting
* [Python's sqlite3 Module](https://pymotw.com/3/sqlite3/index.html)

## Day 3
* Unit Testing with `pytest`
* Basics of Algorithms & Data Structures
* Working with SQLite databases with Python's `sqlite3` module.

## Day 4
* Learning platforms: [CodeWars](https://www.codewars.com) & [HackTheBox](https://www.hackthebox.com)
* More Databases (Labs 268-273)

## Day 5
* Certification Pathways
* Exam Vouchers
* Frontend & NodeJS


# Week 9

## No Monday Class - Labour Day

## Day 1
* Assignment Help
* System Design
* Troubleshooting/Debugging the Deployment Script Lab Challenge

## Day 2
* CloudFront & CDNs
* CAP Theorem basics
* [Agile](https://www.atlassian.com/agile)
* Application & Network Load Balancers
* Load Balancer Lab

## Day 3
* Scott Hanselman talk
* Domain name registration
* Elastic Load Balancing (ELB) & Load Balancer types
* Auto-Scaling Groups & Lab
* netcat (`nc`) basics
* Cost Estimation with the [Pricing Calculator](https://calculator.aws)

## Day 4
* docker compose
* [awesome-compose](https://github.com/docker/awesome-compose)
* Some [React](https://reactjs.org/) & [Next.js](https://nextjs.org/)Basics

### Supplementary
* [Cloudflare & nginx' Architectural issues](https://www.youtube.com/watch?v=QbOAHkaFU6w)
* [DevOps Exercises](https://github.com/bregman-arie/devops-exercises)
* [Latency Numbers that Programmers Should Know](https://colin-scott.github.io/personal_website/research/interactive_latency.html)
* [LinkedIn Skill Assessment Quizzes](https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/) - Only use to learn what you don't know.
* [Next.js Conference - Future of the Web / Edge computing](https://www.youtube.com/watch?v=HlXLVb3QCvQ)


# Week 10

## Day 1
* Lambda
* More SNS
* More S3

## Day 2
* More Lambda, S3 & SNS
* [LibHunt](https://www.libhunt.com/)
* [Thoughtworks Tech Radar](https://www.thoughtworks.com/radar)


## Day 3
* [Amazon Lex](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html)
* Code review of several Lambda blueprints
* [Python Revision & Datetime objects](https://www.pythoncheatsheet.org/)
* [SQS](https://aws.amazon.com/sqs/)

## Day 4

* ChatOps Basics (coding a simple Discord bot that uses boto3 and DynamoDB)
* DynamoDB Basics
* Preventing RSI / back pain / etc in tech jobs

## Day 5

* [S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/)
* More software licensing & software patents
* [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) (Basics)
* Python [typing](https://docs.python.org/3/library/typing.html) basics & [pydantic](https://pydantic-docs.helpmanual.io/)
* More DNS Record Types (AAAA, NS, MX, TXT) [Pic](https://en.wikipedia.org/wiki/List_of_DNS_record_types#/media/File:All_active_dns_record_types.png) 


# Week 11

## Day 1
* CloudFront
* CloudTrail & Athena

## Day 2
* Revision: Docker, Databases, Subnetting, Shell scripting, `hashlib`


# Cloud Practitioner Stuff (to be covered in more detail)

|                  Domain | Topic                             | Items                                | Note                                                                                                                                                                                           | Lab                                                                                                               | Covered |
|------------------------:|-----------------------------------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------|
|          Cloud Concepts | AWS Cloud value proposition       | Benefits                             | Most important:  o Security, o Reliability, o High Availability, o Elasticity, o Agility, o Pay-as-you go pricing, o Scalability, o Global Reach, o Economy of scale,                          |                                                                                                                   | covered |
|                         |                                   | Focus shift                          | Shifting technical resources to revenue-generating activities as opposed to managing infrastructure                                                                                            |                                                                                                                   | covered |
|                         | AWS Economics                     | What is total cost of ownership      | OpEx, CapEx, Operational Cost, Software Licencing of selft maintain infrastructure                                                                                                             |                                                                                                                   | covered |
|                         |                                   | How the cloud can help lowering cost | Right sizing and scale (Elasticity + Pay as you go), many automation available (Agility)                                                                                                       | See billing break down                                                                                            | covered |
|                         | Design principle for Architecture | Design principles                    | o Fail proof, o Decoupling,  o Make use of elasticity,  o Think parallel                                                                                                                       |                                                                                                                   |         |
| Security and Compliance | Shared responsiblity model        | Shared responsibility model          | o Customer responsibility (configuration, software security),  o AWS responsibility (hardware availability, accepted failure rate...)                                                          |                                                                                                                   | covered |
|                         |                                   | Security & Compliance concepts       | o Industry compliance (HIPPA, SOCs, PCIs), basically security standards,  o Encryption (at rest, in transit),  o Least privilege access and Identity Access Management                         | See an IAM policy                                                                                                 | covered |
|                         | Identity Access Management        | User & Identity management           | o Access keys & password, o MFA, o IAM Service (Group/User/Role/Policies)                                                                                                                      | Login to root account,  Tour of IAM                                                                               | covered |
|                         | Security Support                  | Network Security                     | o For later when finished Networking part                                                                                                                                                      |                                                                                                                   |         |
|             Technologgy | Deploy & Operate                  | Methods                              | o AWS Console, o APIs, o SDKs, o Cloudformation (create/delete/modify but not operate) o CDK/Pulumi/Terraform                                                                                  | Login to AWS console                                                                                              | covered |
|                         |                                   | Deployment model                     | o Cloud native, o Hybrid, o On-premises                                                                                                                                                        | Show an architecture design with Hybrid Connectivity                                                              |         |
|                         |                                   | Connectivity options                 | o VPN, o Direct Connect, o Public internet                                                                                                                                                     | Show an architecture design with Hybrid Connectivity                                                              |         |
|                         | Global infrastructure             | Concepts                             | o Regions, o AZs, o Edge Location                                                                                                                                                              |                                                                                                                   | covered |
|                         |                                   | Why use regions                      | o Disaster recovery/business continuity, o Low latency for end user o Data compliance                                                                                                          |                                                                                                                   | covered |
|                         |                                   | Edge Location benefits               | o Quick for download from CDN (CloudFront), o Quick for S3 Upload Accelerator, o AWS Global Accelerator (speed up connection)                                                                  |                                                                                                                   | covered |
|                         | Core Services                     | Compute family 1                     | o VM based compute EC2, o Container based compute ECS/EKS, o Serverless Lambda, o Load Balancer (L7 for HTTP, L4 for ENI), o Health Check Alarm, o Autoscaling group and how autoscaling works | Lambda function lab, EC2 lab, ASG lab tour                                                                        | covered |
|                         |                                   | Compute family 2                     | o Types of EC2 o Types of EC2 billing (Reserve, On-demand, Spot)                                                                                                                               | Visit pricing calculator                                                                                          | covered |
|                         |                                   | Storage family 1                     | o S3 o Glacier o Snowball o Storage Gateway                                                                                                                                                    | S3 Bucket host objects,  S3 Bucket versioning,  S3 Static website hosting, S3 Bucket policy, S3 Life cycle policy | covered |
|                         |                                   | Storage family 2                     | o EBS, o EFS                                                                                                                                                                                   | EC2 attach EBS, encrypt un-encrypted EBS drive                                                                    | covered |
|                         |                                   | Networking 1                         | o VPC, subnets, o Internet Gateway, o Security Group, NACL, o NAT gateway, Bastion Host o Revisit Load Balancer                                                                                | Create VPC with NAT gateway, Bastion Host lab                                                                     | covered |
|                         |                                   | Networking 2                         | o CloudFront o Route53 o API Gateway                                                                                                                                                           | S3 Static website hosting + CloudFront CDN                                                                        | covered |
|                         |                                   | Database                             | o RDS o Aurora o DynamoDB o RedShift (OLTP vs. OLTA)                                                                                                                                           | Aurora RDS Lab + Bastion Host to connect,  DynamoDB Lab                                                           | covered |
|                         |                                   | Integration                          | o SQS o SNS o StepFunctions                                                                                                                                                                    | Go see some working example of StepFunctions, play with SQS and SNS                                               | covered |
|                         |                                   | Management 1                         | o CloudWatch Logs (Lambda example), o CloudTrail, o CloudWatch Event/Eventbridge, o System Manager, o Parameter Store, o Config, o Secrets Manager                                             | See CloudWatch Logs, CloudTrail, and different services                                                           | covered |
|                         |                                   | Management 2                         | o Concept of IaC (Infrastructure as Code) o Cloudformation o Pulumi/Terraform                                                                                                                  | Pulumi/Terraform introduction                                                                                     | covered |
|                         | Support                           | Resource                             | o AWS Trusted Advisor o Support tier o Professional services                                                                                                                                   | Go see the AWS Console                                                                                            |         |
|                         | Billing                           | Bills                                | o Billing console o Billing alarm o Free quota o Services limits o Pricing calculator                                                                                                          | Go see some bills + DynamoDB vs. RDS cost study                                                                   |         |
|                         |                                   | Organization                         | o Organization Units, o Ways to structure OU, o Consolidated billing                                                                                                                           | Go see the AWS Console                                                                                            |         |

* What is IaaS/PaaS/SaaS? 
* Block storage, file storage and object storage
* CDN

# Demonstration topics

| By whom | Ideas                                        | Links                  | Difficulty   | Time estimated to prepare | Tools           | Notes                                                                                   |
|---------|----------------------------------------------|------------------------|--------------|---------------------------|-----------------|-----------------------------------------------------------------------------------------|
|Kawana         | Create and Manage a Nonrelational Database   | https://go.aws/3UGYd2M | Easy         | 1 hour max                | AWS DynamoDB    | Don't use Cloud9, just get Sandbox environment keys                                     |
|Raemon         | Extract video metadata                       | https://go.aws/3NNtw9L | Easy         | 1 hour max                | AWS Rekognition | Do this in AWS Console, add more context if you can                                     |
|Prerana         | Analyze text context and sentiment           | https://go.aws/3DTiuLG | Easy         | 1 hour max                | AWS Comprehend  | Do this in AWS Console, add more context if you can                                     |
|Will         | Translate between languages                  | https://go.aws/3teZrq1 | Very easy    | 1 hour max                | AWS Translate   | Do this in AWS Console, add more context if you can                                     |
|         | Demonstrate SNS Fanout to SQS architecture   | https://go.aws/3DUR5Zw | Intermediate | 1-2 hours                 | AWS SNS,SQS     | Do this in AWS Console, add more context if you can                                     |
|         | Use SQS in real application                  | https://go.aws/3TkTzpY | Intermediate | 2-3 hours                 | AWS SQS         | Additionally, you need to get Sandbox keys, and use boto3 to consume SQS queue messages |
| Ryan        | Demonstrate building application with Lambda | https://go.aws/3DOKznj | Intermediate | 1-2 hours                 | AWS Lambda      | Do this in AWS Console, demonstrate any kind of code that you write yourself            |
| Anuj        | Use Textract to scan text out of images      | https://go.aws/3tcN3qz | Very easy    | 1 hour max                | AWS Textract    | Do this in AWS Console, add more context if you can                                     |
| Stacey        | Detect and analyze faces                     | https://go.aws/3WPVnKK | Very easy    | 1 hour max                | AWS Rekognition | Do this in AWS Console, add more context if you can                                     |
|         | Filter messages using SNS Topic              | https://go.aws/3WLihml | Intermediate | 1-2 hours                 | AWS SNS         | Do this in AWS Console, add more context if you can                                     |
|   Benke      | Add audio transcript                         | https://go.aws/3Upb89G | Very easy    | 1 hour max                | AWS Transcribe  | Do this in AWS Console, add more context if you can                                     |
|      Marcelle   | Protect your S3 data                         | https://go.aws/3Tkm8Uo | Intermediate | 1-2 hours                 | AWS S3          | Do this in AWS Console, add more context if you can                                     |
|Gracie         | Using Docker volume                          | https://bit.ly/3DUUkAa | Intermediate | 1-2 hours                 | Docker          |                                                                                         |
|         | Getting started with Kubernetes              | https://bit.ly/3A0xo1z | Harder       | 2-4 hours                 | Kubernetes      |                                                                                         |

## Technical presentations:
* Your name: Topic/Service goes here
* Another name: Another topic/service goes here

# Concepts book - to be covered
## Others
* VMs vs. Containerization
* Globally Unique IDs
* Process vs. Thread
* Software deployment strategies
* Design secure APIs
* DB Caching
