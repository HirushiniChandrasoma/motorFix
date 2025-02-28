# 🚗 MotorFix - Car Parts Management System

MotorFix is a **Django-based** web application that allows users to **add, update, delete, and view** car parts. It includes **user authentication**, image uploads, and a responsive UI.

 

---

## 📸 Screenshots

### Home Page
![Home Page](screenshots/carpartsinventory.png)

### Add Car Part Page
![Add Car Part](screenshots/adddetails.png)

### Login Page
![Login Page](screenshots/login.png)

### Register Page
![Register Page](screenshots/register.png)

### delete Page
![delete Page](screenshots/delete.png)

### update Page
![update Page](screenshots/updatedetails.png)

---

## 📌 Features

✅ **User Authentication** - Signup, Login  
✅ **Add, Update, Delete Car Parts** - Manage inventory easily  
✅ **Image Upload Support** - Upload images for each car part  
✅ **Django-Based Backend** - Secure and scalable  
✅ **user-Friendly UI** - simple and easy use  

---

## 🛠 Installation

1️⃣ **Clone the Repository**
```sh
git clone https://github.com/HirushiniChandrasoma/motorFix.git
cd MotorFix

---

2️⃣ Create a Virtual Environment (Optional but recommended)
python -m venv venv
venv\Scripts\activate  # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the Server
python manage.py runserver     

Visit http://127.0.0.1:8000/ to access the application.