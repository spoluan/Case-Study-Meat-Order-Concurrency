# Case Study: Meat Order Concurrency

## Description
This project is a Python-based simulation that implements concurrent processing in a meat ordering system. It uses threading and locking mechanisms to handle multiple orders simultaneously from multiple employees in a simulated meat shop environment.  

## Scenario
Imagine you own a meat processing plant that processes only three types of meat: beef, pork, and chicken. A lot of meat was purchased today, including 10 portions of beef, 7 portions of pork, and 5 portions of chicken. You have five employees: (A, B, C, D, E). Each employee processes meat at the same speed. Beef takes 1 second, pork takes 2 seconds, and chicken takes 3 seconds. Without interference, they can all handle the meat independently, and each person can only handle one piece of meat at a time. Each piece of meat can only be handled by one person, and people are not allowed to put the meat back after taking it.

The goal is to hand over all 10 portions of beef, 7 portions of pork, and 5 portions of chicken purchased this time to five employees. Each employee randomly picks up the meat, and the time of picking up the meat will be ignored. Only the processing time of the meat are considered.

## Features
- **Concurrency Handling**: Use Python threading to simulate concurrent order processing.
- **Lock Mechanisms**: Use locks for safe access to shared resources in a concurrent environment.
- **Real-Time Simulation**: Orders are processed dynamically, with the speed of processing influenced by the number of employees (more employees result in faster order processing, as each employee can handle one piece of meat at a time).
- **Order History Tracking**: Maintains a record of all employee orders.
- **Dynamic Adjustments**: The system can be configured with different numbers of employees and available meat portions.
- **Flexible Configuration**: The number of employees and available meat types can be easily adjusted to simulate different scenarios.
  
### Prerequisites
- Python

### The following is a sample output from the meat order processing simulation:

![Sample Figure](screenshots/Screenshot%202024-04-10%20135132.png)

![Sample Figure](screenshots/Screenshot%202024-04-10%20135211.png)


### Employee Records Summary

![Sample Figure](screenshots/Screenshot%202024-04-10%20135234.png)
