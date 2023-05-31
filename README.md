# Exam Scheduling System

![Application Dashboard](/Dashboard1.png)

The **exam-schedular-system** repository contains the code for an Exam Scheduling Application that seamlessly integrates with Africa's Talking SMS APIs. This application facilitates exam registration for college students. The project is built using the Django framework, utilizing HTML templates, Bootstrap, and CSS for the frontend, and Python for the backend.

## Admin Dashboard

To manage courses, exams, students, teachers, and parents, the admin can log into the website and access the respective tabs within the dashboard.

## Running Africa's Talking Simulator

Follow the steps below to run the Africa's Talking simulator:

1. Create an account at Africa's Talking - [africa's talking!](https://africastalking.com/).
2. Navigate to the Africa's Talking sandbox and click 'Go To Sandbox App'.
3. Launch the simulator and enter the phone number of the student.
4. Repeat the same process to have two running simulators, and add the parent's phone number in the second simulator.
5. Proceed to register a student for an exam. You should receive a text message about the registration on the simulators.

## Quick Guide

Follow the steps below to set up and run the web app:

1. Clone the repository:
   ```shell
   git clone https://github.com/john-thuo1/exam-schedular-system
   ```

2. Change into the project directory:
   ```shell
   cd exam-schedular-system
   ```

3. Create a virtual environment:
   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - Windows:
     ```shell
     venv\Scripts\activate
     ```

5. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

6. Create the database:
   ```shell
   python manage.py makemigrations
   ```

7. Apply database changes:
   ```shell
   python manage.py migrate
   ```

8. Configure Africa's Talking SMS API and Africa's Talking API:
   Please refer to this link for detailed instructions: [Integrating Africa's Talking APIs into the Hospital Management System](https://medium.com/@johnthuo/part-2-integrating-africas-talking-apis-into-the-hospital-management-system-5e7a2cd16345)

9. Run the server:
   ```shell
   python manage.py runserver <port_number>
   ```
   For example:
   ```shell
   python manage.py runserver 3000
   ```

10. Access the site on your localhost:
    Follow the instructions provided on the home page to start using the site.
