You are an IT specialist working in a medium-sized company. 

Your manager wants to create a daily report that tracks the use of machines; 
specifically she wants to know which users are currently connected  to which machine.

In your company, there's a system that collects every event that happens on the machines on the network. 
- Among the many events collected, it records each time a user longs in or out of a computer.

With this information, we want to write a script that generates a report of which users are logged in to which machines at that time.

## Problem Statement
We need to process a list of Event objects using their attributes 
to generate a report that lists all users currently logged in to the machines.

## Input Format
```text
Event objects with attributes
* date: when the event happened; Format: YYYY-MM-DDTHH:MM:SS
* machine: name of the machine where the event occurred
* user: user involved
* type: event type [login | logout]
```

## Output Format
```text
lists all the machine names; for each machine, lists the users that are currently logged in

output format option 1: 
machine name1:
- user1
- user2
- user3
machine name2:
- user4
- user5

output format option 2:
machine name1: user1, user2, user3
machine name2: user4, user5
machine name3: user6, user7, user8
```
This information should be printed on the screen.


## Note
what matters is how well script solve the problem, not how good-looking the generated report is 