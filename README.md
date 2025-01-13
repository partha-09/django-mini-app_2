# django-mini-app_2

A simple Django project that implements a user registration system. The project collects user data (Full Name, Email, and Phone Number) through a form and stores it in an SQLite database. The stored data can then be displayed in a structured format on an inquiry page.

---

## Project Features

1. **User Registration Form**:
   - Collects Full Name, Email, and Phone Number.
   - Data validation and proper UI feedback for inputs.
   - Utilizes a responsive and styled HTML form for user-friendly interaction.

2. **Data Storage**:
   - Data is stored in an SQLite database using Django models.

3. **Data Display**:
   - Displays the stored data in a table format on the inquiry page.

4. **Admin Interface**:
   - Allows admin users to manage user data through the Django admin panel.

---

## 📸 Screenshots

### Registration Form
A clean and responsive form for user registration.
![Registration Form](https://github.com/partha-09/django-mini-app_2/blob/51147e7aea0cfedbf5e18eb5a8534dd1f2c7f248/input.jpg)

### Inquiry Page
A styled table that displays the registered user information.
![Inquiry Page](https://github.com/partha-09/django-mini-app_2/blob/51147e7aea0cfedbf5e18eb5a8534dd1f2c7f248/output.jpg)

---

## Tech Stack

- **Backend**: Django
- **Database**: SQLite
- **Frontend**: HTML5, CSS3 (Inline styling)
- **Python Version**: 3.x

---

## How to Run the Project

1. **Clone the Repository**:

   git clone https://github.com/partha-09/django-mini-app_2.git
2. **Navigate into the project directory**:
    cd django-mini-app_2
3. **Install Dependencies**: Make sure you have Python and Django installed. Use the following command to install Django:
    pip install django
4. **Apply Migrations**: Run the following commands to apply database migrations:
    python manage.py makemigrations
    python manage.py migrate
5. **Run the Development Server**: Start the Django development server:
    python manage.py runserver
6. **Visit** http://127.0.0.1:8000/reg/ to access the registration form.
---
## URLs and Functionalities
1. **Registration Form:** http://127.0.0.1:8000/reg/
    Collects user details and stores them in the database.
2. **Inquiry Page:** http://127.0.0.1:8000/info/
    Displays all registered users' details in a tabular format.
3. **Admin Panel:** http://127.0.0.1:8000/admin/
    Access to manage and view the database. Make sure to create a superuser:
    python manage.py createsuperuser
---
## Code Overview
1. **Models** (models.py):
Defines a model Information for storing user data:
    class Information(models.Model):
        fullName = models.CharField(max_length=222)
        emial = models.EmailField(max_length=222)
        phone = models.CharField(max_length=15)
2. **Views** (views.py):
    Handles form submission and displays data:

      Contact: Processes registration form submissions.
      Info: Displays stored user information.
3. **URLs** (urls.py):
      Defines URL patterns for registration and inquiry:
    urlpatterns = [
          path('admin/', admin.site.urls),
          path('reg/', views.Contact),
          path('info/', views.info),
        ]
4. **Templates:**
   Register.html: Registration form template.
    Inquiry.html: Table to display user data.

## MVT Architecture:

1. Model: Details model to store user names.
2. View: Logic to process form input and fetch database records.
3. Template: HTML files to render the user interface.



### 📬 Contact:

For any queries:

- **Name**: Siddappa Godi
- **Email**: [siddapp2godi@gmail.com](mailto:siddapp2godi@gmail.com)
- **Phone**: +91 6363504679
- **LinkedIn**: [https://www.linkedin.com/in/siddappagodi/](https://www.linkedin.com/in/siddappagodi/)


## ⭐ Contribute

I welcome contributions to improve this project! If you find this project helpful or see any areas for enhancement, feel free to:

- **Fork** this repository.
- **Submit a Pull Request** with improvements or new features.
- **Open an Issue** if you encounter any bugs or have suggestions for better functionality.

Your contributions are greatly appreciated and will help make this project even better. Don't hesitate to reach out for any queries or collaboration ideas!



