/api/bookings/
/api/registration

restaurant\static\img\api_output.png

Little Lemon Restaurant Website
This is a Django-based web application for the Little Lemon Restaurant, showcasing a modern and responsive design, dynamic menu display, table booking functionality, and a well-structured project setup. This project demonstrates core Django concepts, including models, views, templates, forms, static file management, and URL namespacing.
Features
Responsive Design: The website is designed to be fully responsive, providing an optimal viewing experience across various devices (desktop, tablet, mobile).

Homepage: A welcoming landing page with highlights and calls to action.

Dynamic Menu Page: Displays menu items fetched directly from the database.

Menu Item Detail Pages: Each menu item has its own dedicated page with more details.

Table Booking System: A form for customers to submit table reservations, stored in the database.

About Us Page: Provides information about the restaurant.
Apply database migrations:
This will create the necessary database tables for your models.

python manage.py makemigrations restaurant
python manage.py migrate

Create a superuser (for admin access):

python manage.py createsuperuser

Follow the prompts to set up your admin username, email, and password.

Collect static files (optional for development, but good practice):

python manage.py collectstatic

Run the development server:

python manage.py runserver

The website will be accessible at http://127.0.0.1:8000/.

Usage
Homepage: Access the site at http://127.0.0.1:8000/

Menu Page: View all menu items at http://127.0.0.1:8000/menu/

Menu Item Details: Click on any menu item on the menu page to see its details (e.g., http://127.0.0.1:8000/menu/1/ for item with ID 1).

Book a Table: Fill out the booking form at http://127.0.0.1:8000/book/

About Us: Learn more about the restaurant at http://127.0.0.1:8000/about/

Admin Panel: Log in to the Django administration interface at http://127.0.0.1:8000/admin/ using the superuser credentials you created. Here you can add/edit Menu items and Booking entries.

Future Improvements
User Authentication for Bookings: Link Booking records to authenticated User models.

API Endpoints (with DRF): Implement a RESTful API for Menu items and Bookings using Django REST Framework, with proper authentication and permissions (e.g., for managers).

Order Management System: Develop models and views for handling customer orders.

Interactive Booking Calendar: Enhance the booking form with a more interactive date picker.

Tests: Write unit and integration tests for models, views, and forms.

Technologies Used
Python 
Django 4.1.1 (or your specific version)
HTML5
CSS3 (Custom styling for an attractive UI)

/api/bookings/
/api/registration

restaurant\static\img\api_output.png