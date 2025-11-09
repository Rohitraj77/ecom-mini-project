## E-Commerce Mini Project

### Live Link  
https://rohitraj6362.pythonanywhere.com/

---

### Overview  
This is an E-Commerce web application developed using Django and Django REST Framework. It was built as part of a full-stack developer assignment. The project includes features like user authentication, product management, and order tracking. It also supports admin and user roles with different levels of access.

---

### Technologies Used  
- Django  
- Django REST Framework  
- SimpleJWT for authentication  
- SQLite3 database  
- PythonAnywhere for deployment  
- Git and GitHub for version control  

---

### Features  

**User Module**  
- User registration and login using JWT authentication  
- Profile management  
- Role-based access for user and admin  

**Product Module**  
- Admin can add, update, and delete products  
- Public users can view product lists and details  

**Order Module**  
- Users can place and view their own orders  
- Admin can view and update order status (Pending, Processing, Shipped, Delivered, Cancelled)  

**Admin Panel**  
- Admin dashboard for managing users, products, and orders  
  - URL: https://rohitraj6362.pythonanywhere.com/dj-admin/

---

### API Endpoints  

| Module | Endpoint | Method | Description |
|---------|-----------|--------|--------------|
| Auth | /api/auth/register/ | POST | Register a new user |
| Auth | /api/auth/token/ | POST | Get JWT tokens |
| Products | /api/products/ | GET | View product list |
| Products | /api/admin/products/ | GET, POST, PUT, DELETE | Manage products (Admin only) |
| Orders | /api/orders/ | GET, POST | Create or view orders |
| Orders | /api/admin/orders/ | GET, PUT | Manage orders (Admin only) |

---

### Installation Steps  

```bash
git clone https://github.com/Rohitraj77/ecom-mini-project.git
cd ecom-mini-project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

After running the server, open http://127.0.0.1:8000/ in the browser.

---

### Deployment Steps  

```bash
git clone https://github.com/Rohitraj77/ecom-mini-project.git
cd ecom-mini-project
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

Configured and deployed on PythonAnywhere.

---

### Developer  
**Name:** Rohit Raj  
**Role:** Full Stack Developer  
**Skills:** Python, Django, MySQL, HTML, CSS, JavaScript  
**GitHub:** https://github.com/Rohitraj77  

---

### Project Status  
Completed and successfully deployed on PythonAnywhere  
Deployed in November 2025  
