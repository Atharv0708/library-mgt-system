# 📚 Smart Library Management System

A modern, automated, and web-based Library Management System developed using Python and the Django Framework. It simplifies book issuing, inventory tracking, and role-based access control for students and library staff.

## 🚀 Key Features
* **Role-Based Access Control (RBAC):** Separate dashboards and permissions for Admin, Library Staff, and Students.
* **Smart Analytics Dashboard:** Real-time statistics of total books, issued books, pending requests, and user count.
* **Online Book Requests:** Students can check real-time book availability and request books online.
* **Modern UI:** Clean, responsive, and intuitive interface built with Bootstrap and Django Jazzmin theme.

## 🛠️ Technology Stack
* **Backend:** Python, Django Framework
* **Database:** SQLite (Default)
* **Frontend:** HTML, CSS, Bootstrap, FontAwesome
* **Admin Theme:** Django Jazzmin

## ⚙️ How to Run the Project on Your Machine

Follow these simple steps to run this project on your local system:

**1. Clone the repository:**
`git clone https://github.com/your-username/smart-library-mgt-system.git`
`cd smart-library-mgt-system`

**2. Create and activate a Virtual Environment:**
`python -m venv env`
`env\Scripts\activate`  *(For Windows)*
`source env/bin/activate` *(For Mac/Linux)*

**3. Install required dependencies:**
`pip install -r requirements.txt`

**4. Apply Migrations (If required):**
`python manage.py makemigrations`
`python manage.py migrate`

**5. Run the Local Development Server:**
`python manage.py runserver`

**6. Access the Application:**
* Student Portal / Home: `http://127.0.0.1:8000/`
* Admin / Staff Dashboard: `http://127.0.0.1:8000/admin/`

## 🔐 Default Login Credentials
*(Note: Since this is a test project, the SQLite database is included with predefined users).*
* **Superadmin:** Username: `admin` | Password: `1234)`
* **Librarian/Staff:** Username: `staff_abhijeet` | Password: `Abhi@1624`