# Almanac- To-Do-App
Almanac is a Django based To-Do-App  where you can add the tasks you have to do with task description and task priority level. Almanac will store your data forever unless you delete it. Almanac provides you with multiple features like sorting the tasks by their priority level and searching the task by its title. 

# How to setup on Windows
***1. Clone This Project:*** git clone https://github.com/SouravSehgal-3009/Almanac--To-Do-App   </br>
***2. Go to Project Directory:*** cd Desktop\AlmanacProj        (just example) </br>
***3. Create a Virtual Environment:*** python -m venv myproj        (I created a virtual environment myproj.)</br>
***4. Activate Virtual Environment:*** myproj\Scripts\activate.bat </br>
***5. Install Requirements Package:*** pip install -r requirements.txt </br>
***6. Migrate Database:*** python manage.py migrate </br>
***7. Create Super User:*** python manage.py createsuperuser (To make yourself django admin) </br>
***8. Finally Run The Project:*** python manage.py runserver (To run the project on server) </br>

# How to setup on Linux
***1. Clone This Project:*** git clone https://github.com/SouravSehgal-3009/Almanac--To-Do-App </br>
***2. Go to Project Directory:*** cd Desktop\AlmanacProj        (just example) </br>
***3. Create a Virtual Environment:*** python -m venv myproj        (I created a virtual environment myproj.) </br>
***4. Activate Virtual Environment:*** source myproj\Scripts\activate.bat </br>
***5. Install Requirements Package:*** pip install -r requirements.txt </br>
***6. Migrate Database:*** python manage.py migrate </br>
***7. Create Super User:*** python manage.py createsuperuser (To make yourself django admin) </br>
***8. Finally Run The Project:*** python manage.py runserver (To run the project on server) </br>
 
# Basic Features
● ***Add Task:*** You can add the task to do as task title along with task description and task priority level.

![Add Task](https://user-images.githubusercontent.com/60173032/117720845-c92d5b80-b1fc-11eb-94ce-9dac0e55fe7a.jpg)

● ***List All Tasks:*** All the tasks that you have added will be displayed. Two tasks will be shown on one page and you can navigate between the pages.

![List Tasks](https://user-images.githubusercontent.com/60173032/117721409-71dbbb00-b1fd-11eb-8009-b591107d5a9d.jpg)

● ***Sort by Priority level:*** You can list all the tasks you have been added will be displayed sorted by priority level of the task. Two tasks will be shown on one page and you can navigate between the pages.

![Sort By Priority Level](https://user-images.githubusercontent.com/60173032/117721799-eca4d600-b1fd-11eb-89bf-bf6d9337e6fe.jpg)

● ***Search by title:*** You can search any task in the task list by its title.

![Search](https://user-images.githubusercontent.com/60173032/117721894-0d6d2b80-b1fe-11eb-82ed-4cb304260b0d.jpg)

● ***Edit/Delete Task:*** You can delete an exiting task or make changes in an existing task as per your wish.

![EditDelete](https://user-images.githubusercontent.com/60173032/117722140-558c4e00-b1fe-11eb-8aae-25a62fdc523e.jpg)





