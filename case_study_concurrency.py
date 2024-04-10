# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:32:19 2024

@author: Sevendi Eldrige Rifki Poluan
"""

import threading
import time 
import random
import datetime   

class MeatOrderSystem(object):

    def __init__(self, meats={}, employees=[]): 
    
        self.meats = meats # A dictionary to keep track of meat types and their quantities
        self.employee_independent_lock = {} # A dictionary to manage locks for each employee
        self.employees = employees # Define a list of employees
        self.history = {} # A dictionary to record the history of orders
        self.semaphore = threading.Semaphore(0) # Track active threads 

    def choose_meat(self, employee): 
    
        # Check if there are any meats available
        if self.meats:
            
            # Select a random meat from the available options
            random_meat = list(self.meats.keys())[random.randint(0, len(self.meats.keys()) - 1)]
            
            # Record the time of the order
            order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            print(f"{employee}. Get {random_meat} at {order_time}. Remaining stock: {self.meats[random_meat] - 1}")
            
            # Decrease the quantity of the selected meat by 1
            self.meats[random_meat] -= 1
            
            # If the selected meat is out of stock, remove it from the list 
            if self.meats[random_meat] == 0:
                del self.meats[random_meat]
            
            # Return the selected meat 
            return random_meat, order_time
        else:
            # Return None if no meats are available
            return None, None 
        
    def process_order(self, employee, ordered_meat, order_time):
        
        # Create a unique lock for each employee
        if employee not in self.employee_independent_lock:
            self.employee_independent_lock[employee] = threading.Lock()   

        # Acquire the lock for the current employee
        self.employee_independent_lock[employee].acquire()
         
        # Record the time of the order
        processed_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        print(f"{employee}. {ordered_meat} proccessed at {processed_time}") 
   
        # Simulate processing time based on the type of meat
        if ordered_meat == 'beef':
            time.sleep(1)
        elif ordered_meat == 'pork':
            time.sleep(2)
        elif ordered_meat == 'chicken':
            time.sleep(3)

        # Record the time of the order
        finished_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        print(f"{employee}. Finished processing {ordered_meat} at {finished_time}")

        # Record the order in the history
        if employee not in self.history:
            self.history[employee] = [] 

        self.history[employee].append({
            "employee": employee,
            "order": ordered_meat,
            "order_time": order_time,
            "processed_time": processed_time,
            "finished_time": finished_time
        }) 
         
        # Release the lock after processing the order
        self.employee_independent_lock[employee].release()
          
    def process_order_independently(self, key, order_threads, semaphore):

        # Wait for all order threads to complete
        for order in order_threads:
            order.join()

        print(f"All orders for {key} are done")

        # Signal the semaphore once all orders are processed
        semaphore.release()
    
    def main(self):

        # Dictionary to manage threads for each employee    
        employee_threads = {}

        # Process orders from customers until the meats are out of stock
        while True:

            # Loop through each employee to determine their availability to handle meat orders and process them accordingly
            meat_to_order = 0
            for employee in self.employees:
                
                # Initialize a thread list for each employee if it doesn't exist
                if employee not in employee_threads:
                    employee_threads[employee] = []
                
                # Check if the employee is in serving mode. If so, they need to wait until they finish serving
                if employee in self.employee_independent_lock:
                    if self.employee_independent_lock[employee].locked(): 
                        continue 

                # Assume there is a meat order from a customer, and a meat is randomly chosen. 
                # Check the availability of the chosen meat in stock.
                meat_to_order, order_time = self.choose_meat(employee) 
                
                # Break the loop if meat is out of stock
                if meat_to_order is None: 
                    break
                
                # Create and start a thread for processing the order
                create_order = threading.Thread(target=self.process_order, args=(employee, meat_to_order, order_time, ))
                employee_threads[employee].append(create_order)
                create_order.start()

            # Exit the main loop if meat is out of stock
            if meat_to_order is None: 
                break 

        # Create threads to process orders independently for each employee 
        for key, orders in employee_threads.items():
            threading.Thread(target=self.process_order_independently, args=(key, orders, self.semaphore)).start()

        # Wait for all 'employee' threads to finish
        for _ in employee_threads:
            self.semaphore.acquire()

    def print_summary(self):     

        print("\n . \n" * 4)
        # Print a summary of all orders
        for employee, order_details in self.history.items(): 
            print(f"#### Employee {employee}")
            for order in order_details:
                print(f"Order time: {order['order_time']}: Processing time {order['order']} {order['processed_time']} to {order['finished_time']}")
            print("-" * 25, sep="\n")


if __name__=='__main__':
     
    meats = {
            "beef": 10, 
            "pork": 7, 
            "chicken": 5
        } # Define the meat availability.
    employees = ["A", "B", "C", "D", "E"] # Define a list of employees

    meatOrderSystem = MeatOrderSystem(meats=meats, employees=employees)
    meatOrderSystem.main()
    meatOrderSystem.print_summary()