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
   - The Presentation folder contains HTML files that constitute the user interface (UI) of the Task Management System.
   - These HTML files are utilized by the Django framework to render the application interface for users.

### 1. View Models
   - The View Models folder is responsible for managing the data flow between the user interface and the Services layer.
   - View Models handle incoming data from the UI, prepare and validate it, and then pass it to the Services layer for further processing.
  
### 2. UI
   - The UI folder serves as the primary location for the implementation of the application's business logic.
   - It acts as an intermediary layer, facilitating communication and interaction between the user interface, services, and data access layers.
   
### 5. Management
   - The Management folder encompasses all the components of the Task Management System.
   - It includes subfolders for DAL, Services, Bridge, Presentation, View Models, and UI.

## Usage

To use the Task Management System, follow these steps:

1. **Installation**:
   - Ensure you have Django installed. If not, install it using:
     ```
     pip install django
     ```

2. **Configuration**:
   - Configure your database settings in the Django project settings file.

3. **Database Setup**:
   - Run migrations to create the necessary database tables using:
     ```
     python manage.py migrate
     ```

4. **Running the Server**:
   - Start the Django development server using:
     ```
     python manage.py runserver
     ```

5. **Logging In**:
   - Once the server is running, log in with the following credentials:
     - **Username**: Admin
     - **Password**: admin#111

6. **Accessing the Application**:
   - Access the application through the provided URL and interact with the user interface to manage tasks.


## Follow
(https://www.instagram.com/sasidhar316?igsh=eHVhb2oycGFybXN6)





