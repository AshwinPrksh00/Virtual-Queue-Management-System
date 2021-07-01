# Virtual-Queue-Management-System
This is a streamlit deployment of a basic queue management system.

It has 2 pages:
  1. A Homepage where the queue as well as its statitics are displayed.
  2. An Operations page where all the operations of queue management system are done. It consists of 3 operations.<br>
    a. Add Customer                :  Adding a customer to the queue.<br>
    b. Cancel Customer Booking     :  Cancels a customer booking and deletes him from the queue.<br>
    c. Update Customer Timing      :  Updates Customer's time if the customer is uncomfortable with that time.
    
## Deployment
To see results, click here: <a href="https://share.streamlit.io/ashwinprksh00/virtual-queue-management-system/main/vqms_script.py">VQMS</a>



## Note
 1. The data for the operations are preloaded into the repository within an excel file.<br>
 2. The Customers are given a time interval of 30 minutes betwwen each.<br>
 3. If a customer is deleted in between, the timings after the deleted customer will be reduced by 15 minutes.<br>
 4. A customer timing is updated to between two customers if the timing between those customers is equal to or greater than 1 hour.

## Update 1.0
-Fixed the error of updating customer timing to end of queue.
