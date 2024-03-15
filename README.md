# Task Management System

Welcome to the Task Management System!

This project is organized into several folders, each serving a specific purpose in the overall 3-Tier architecture of the application.

## Folder Structure

### 1. DAL (Data Access Layer)
   - This folder contains Django models and repositories responsible for interacting with the database.
   - The Entities files define the structure of the data stored in the database.
   - The repositories provide methods for querying and manipulating data in the database.

### 2. Services
   - The Services folder holds Service Models, which contain business logic related to task management.
   - These models interact with the DAL layer to perform CRUD (Create, Read, Update, Delete) operations on tasks.
   - This folder contains files that bridge the communication between the DAL and Services layers.
   - It ensures smooth data flow between the database and the business logic layer.

### 4. Presentation 
   - The Presentation folder holds **HTML** files for the user interface (UI) of the Task Management System.
   - These HTML files are rendered by the Django framework to display the application to users.

   ### 1. View Models
        - View Models are responsible for handling data received from the UI and passing it to the Services layer.
        - They prepare and validate data before sending it to the business logic layer for processing.
     
   ### 2. UI
        - The UI folder contains the main business logic of the application.
        - It coordinates the interaction between the user interface, services, and data access layers.
     
   
### 7. Management
   - The Management folder encompasses all the components of the Task Management System.
   - It includes subfolders for DAL, Services, Bridge, Presentation, View Models, and UI.

## Usage
To use the Task Management System, follow these steps:

**Management** is the application name in the **Django project**

## Login using
     **Username : Admin**
     **Password : admin#111**

1. Ensure you have Django installed. If not, install it using `pip install django`.
2. Configure your database settings in the Django project settings file.
3. Run migrations to create the necessary database tables using `python manage.py migrate`.
4. Start the Django development server using `python manage.py runserver`.
5. Access the application through the provided URL and interact with the user interface to manage tasks.

## Follow
(https://www.instagram.com/sasidhar316?igsh=eHVhb2oycGFybXN6)


If you would like to contribute to the Task Management System project, please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and ensure they pass all tests.
- Submit a pull request, clearly describing the changes you've made.



