# business_info
Sample code in PHP and MySQL for Business Customer Information System. 
These are working sample files in PHP, all written from scratch.  In the business_info folder is a sample MySQL database titled business_info which can be imported into MySQL 5.7 or later.  User Name is 'staffmember', and Password is 'Customer1'.  The first file to open is business_first_record.php.


Also the same sample database has been connected to Python 3.7 screens.  The primary file, BusinessCustomerInformationScreenMySQLPython37.py is the screen to run.  BusinessCustomer.py is the class file, and db_businesscustomer.py is the connecting file to the MySQL database.

NOTE:  Everything was tested using wampserver64, with localhost.  

HOW TO CREATE DATABASE:  the file business_info_db_creation.sql can be immediately imported in phpmyadmin as written.  To import only into a MySQL instance, copy and paste from the line "CREATE DATABASE IF NOT EXISTS...." all the way to the end.  The user name in all PHP and Python files is 'staffmember' and the password is 'Customer1'.  Please set up accordingly.

NOTE:  For the Python - MySQL connection, I used pymysql.  If you have not installed it, please go to your commmand prompt, type "pip install pymysql".  

Please feel free to render feedback/comments.  Thanks!
