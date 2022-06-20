# Vending Machine Project
------------------------------------------------
### Starting Server
This program runs on Django web framework. In order to run this program use the make file '`make`' provided or from the home directory `python manage.py runserver` and navigate to `http://127.0.0.1:8000/` in your favorite browser. 

### Site Usage 
Once navigating to the homepage every user must create an account before purchasing sodas, accounts are credited with $100.00 upon signup. On the vending machine page users can purchase drink by using the keypad to enter the soda's key. 

### APIS

`/apis/adddrinkstock/DRINK_NAME_HERE/` **POST**
Allows admin to update the amount of stock for a certain drink. JSON table must include the amount and an admin key. Example: `{"amount": 500, "password": "secretpassword"}`

 `/apis/getallstock/` **GET**
Returns a JSON table with the current amount of stock for all drinks 

`/apis/getdrinkstock/DRINK_NAME_HERE/` **GET**
Returns the current amount of stock for a specified drink

`apis/changedrinkprice/DRINK_NAME_HERE/` **POST**
Allows admin to update price of a specific drink. JSON table must include the new price and an admin key. Example: `{"price": 500.25, "password": "secretpassword"}`
