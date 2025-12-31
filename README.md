Objective :-  
 
The primary purpose of this application is to design a  
customer-admin interface for a hotel-hotel blue waves, where 
customers can book rooms for staying or table reservations 
and hotel management team can perform their day to day 
activities. 
 
Types of portals :- 
 
We have 2 portals -user and admin.  
User UI 
Customers have the choice to book their room, table 
reservation and cancellation of room or table reservation. 
Customers after choosing one of the options, must enter their 
details without errors and can book or cancel their 
reservations. 
Customers have the option to contact the hotel. 
 
User defined functions:- 
 
User function: 
→ contains code to create and run user ui 
room_booking function: 
→ contains code to provide room reservation interface and    
stores data in mysql tables 
3 
 
Nested functions: 
• r_from_date function and choose_to_date function 
obtains stay duration from user 
• rbook 
→ finds out if chosen interval of days is available and stores 
data into mysql table, shows message box indicating 
error/unavailability otherwise 
 
table_booking function: 
→ contains code to provide room reservation interface and 
stores data in mysql tables 
 
Nested functions: 
• tslot1 function,tslot2 function,tslot3 function 
→ obtains timeslot from user and returns value to program 
• choose_to_date function 
→ obtains table reservation date from user 
• tbook 
→ finds out if chosen time slot is available and stores data 
into mysql table,shows message box indicating 
error/unavailability otherwise 
 
Cancellation function: 
→ contains code to provide interface for customers to cancel 
their reservation 
 
Nested functions: 
• cancel1 
4 
 
→ cancels room reservation after obtaining details from user 
by removing related logs from mysql table 
• cancel2 
→ cancels table reservation after obtaining details from user 
by removing related logs from mysql table 
 
Admin function: 
Interfaces for admin will be provided to check the availability 
of rooms, details of employees, details of customers,  book 
rooms,bill generation. 
 
SHOW: 
To verify the password given by the admin and to show the admin 
functions 
 
AVAILABILITY: 
To check the availability of room in the hotel and to book rooms 
accordingly 
 
DETAILS: 
Shows the details of customers who have booked a particular 
room 
 
FOODMENU: 
Admin can view or even change cost food items 
 
INFO: 
Admin can add,remove,view or even change particular employee 
details 
CHECKINNOW: 
5 
 
Admin can book rooms for customer in admin interface 
 
PAYMENT: 
To calculate the total bill for the stay 
 
CANCEL: 
To cancel the room/table booked 
 
LOG: 
Creates rooms and tables available for a particular month 
Deletes rooms and tables that were available for that month as per 
admins input  
 
FILES USED 
 
 
The portals are designed using python language(Python 3.7.0),  
tkinter  module and PIL module from its inbuilt library in a 
single .py file.
