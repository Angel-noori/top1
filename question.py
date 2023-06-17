Why we use form in web page? Write down the step-by-step answer that how we can store data from a form into a database.

Why we use form in web page
We use forms in web pages for several reasons:
•	Collect user input through text boxes, select menus, checkboxes, etc. 
•	Submit requests to the website like contact forms or search forms
•	Filter or sort data using form options
•	Collect user credentials for logins and registrations
•	Validate input fields before submitting
•	Transfer data to a database for permanent storage
In short, forms provide a structured interface for users to interact with websites by submitting information, requests and taking actions.

Write down the step-by-step answer that how we can store data from a form into a database 
The steps to store form data in a database are:
(1) Create an HTML form with input fields like text, radio buttons, checkboxes, etc.
(2) When the form is submitted, the data is sent to the server. We need a backend server (like in PHP, Python, etc.) to handle the form submission.
(3) In the backend, we can access the form data through request objects. For example, in PHP we can use.
(4) We then connect to the database (MySQL, PostgreSQL, etc.) using a library in the backend language. For example, in PHP we can use mysqli.
(5) We then insert the form data as a new record in the relevant database table using an INSERT query.
(6) Finally, we redirect the user to a success page to confirm the data was saved.

So, in short, an HTML form is used to get input from users, the data is sent to a backend server, where it is inserted into a database. The backend server then confirms success to the user.
