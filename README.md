# AssignmentWoltBackend
Assignment Wolt Software Engineer Internship

### Which function realized:
Calculation of Delivery Fee: <br>
'GET' 'localhost:8000/api/' with body: {"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}<br><br>
Returns {"delivery_fee": 710}<br><br>
![image](https://user-images.githubusercontent.com/78027392/215882425-e0e5a388-4b7f-4c7f-8b2a-a15d219eae16.png)


### Written different test cases, which are considered different delivery fee. [/api/tests/test_logic]

### Built With
* [Python]
* [Django]
* [Docker]<br>

### First way to run project (Using docker): <br>
--> Open path to project in Terminal/CMD (Check that DockerFile and Docker Compose located in this folder) <br>
--> For first time run of project write "docker-compose up --build" <br>
After that, you can fully use the project <br>
The next time you can run the project with the same path and single command "docker-compose up" <br>
<br><br>
### Second way to run project (Requires pip installed)
How to run project on Windows:
--> pip install virtualenv <br>
--> virtualenv *venv_name* <br>
--> .\*venv_name*\Scripts\activate <br>
--> pip install -r requirements.txt <br>
--> python manage.py test <br>
--> python manage.py runserver <br>

How to run project on Mac OS:
--> pip install virtualenv <br>
--> virtualenv *venv_name* <br>
--> source *venv_name*/bin/activate <br>
--> pip install -r requirements.txt <br>
(If some bug exist with postgres or psycopg2 write: "brew install postgresql" and try again)
<br>
--> python manage.py test <br>
--> python manage.py runserver <br>

### How to use it
You can use Postman with parameters which described above <br>
OR you can request from terminal by curl <br>
Example: <br>
   curl -X GET http://localhost:8000/api/ <br>
   -H "Content-Type: application/json" <br>
   -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2021-10-12T13:00:00Z"}' <br>

