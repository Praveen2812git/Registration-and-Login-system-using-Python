# Description
**Registration and Login system using Python:**  A simple registration and login system with python and SQLite.

# Workflow and logic
### Step 1
**Choose between Registration and Login:**

### Step 2
**Registration Condition:**
  - **User Name**
    - email/username should have "@" and followed by "." Eg - sherlock@gmail.com, nothing@yahoo.in
    - it should not be like this Eg:- @gmail.com
    - there should not be any "." immediate next to "@" Eg:- my@.in
    - it should not start with special characters and numbers Eg:- 123#@gmail.com
  
  - **Password** 
    - (5 < password length < 16)
    - must have minimum one special character
    - one digit
    - one uppercase
    - one lowercase character
    
### Step 3
**Once the username and password are validated, the data is stored in a file.**

### Step 4
**Login**
  - **User Name**
    - When the user chooses to Login, check whether his/her credentials exist in the file or not based on the user input.
    - If it doesn’t exist then ask them to go for Registration.
  
  - **Password**
    - If they have chosen forget password you should be able to retrieve their original password based on their username provided in the user input
     (only if their username matches with the data exists in the file).
    - If nothing matches in your file you should ask them to Register.
     (Since they don't have an account).
     
     
# File Management
- SQLite is used for file management.
- UserName and Password is stored in SQLite database in a seperate table when registering.
- When Logging In, the username and password is checked in database and condition mentioned above is work accordingly.
