# Virtual-Queue-Management-System
This is a streamlit deployment of a basic queue management system.
It has 2 pages:
  1. A Homepage where the queue as well as its statitics are displayed.
  2. An Operations page where all the operations of queue management system are done. It consists of 3 operations.
    a. Add Customer                :  Adding a customer to the queue.
    b. Cancel Customer Booking     :  Cancels a customer booking and deletes him from the queue.
    c. Update Customer Timing      :  Updates Customer's time if the customer is uncomfortable with that time.
    

## P.S: 
     
     1. The data for the operations are preloaded into the repository within an excel file.
     2. The Customers are given a time interval of 30 minutes betwwen each
     3. If a customer is deleted in between, the timings after the deleted customer will be reduced by 15 minutes.
     4. A customer timing is updated to between two customers if the timing between those customers is equal to or greater than 1 hour.
