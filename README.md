# exam-schedular-system

![Application Dashboard](/Dashboard1.png)

# 

The repository contains code for an Exam Scheduling Application that interacts with Africa's Talking SMS APIs to allow for seamless Exam Registration For College Students. The project utilizes Django framework for both front(Uses html templates, Bootstrap and CSS) and Back-end.

To add Courses, Exams, Students, Teachers and Parents, the Admin will log into the website and move to the respective tabs within the dashboard.

# Running Africa's Talking Simulator
 - Create an account at Africa's Talking - [africa's talking!](https://africastalking.com/)
 - Navigate to the Africa's Talking sandbox and click 'Go To Sandbox App'
 - Within the page opened, Launch the simulator and enter the Phone Number of the student.
 - Do the same, in order to have 2 running simulators, and add the Parent's phone number in the second simulator.
 - Go ahead and register a student to an exam. You should see text message about it on the simulators.

  
# Quick Guide <br />

Below are the steps on how to get the web app up and running

- Clone it: <br />
    git clone https://github.com/john-thuo1/exam-schedular-system <br />

- Cd into it: <br />
    cd into the working directory <br />

- Create a virtual environment
    python3 -m venv venv <br />
     
- Activate venv: <br />
    Mac/Linux: source venv/bin/activate <br />
    Windows: venv\Scripts\activate <br />
    
- Install the requirements <br />
    pip install -r requirements.txt <br />
    
- Create DB <br />
    python manage.py makemigrations <br />
    
- Apply DB Changes <br />
    python manage.py migrate <br />
    
 
 
- Configure your Africa’s Talking S.M.S A.P.I. and Africa's Talking API: <br />
      Follow this link for more details : https://medium.com/@johnthuo/part-2-integrating-africas-talking-apis-into-the-hospital-management-system-5e7a2cd16345
      

- Run the server: <br />
   - python manage.py runserver Port Number<br />
   - python manage.py runserver 3000 <br />

- Navigate to your localhost site <br />
   Follow the instructions on the home page to start using the site
  
  



