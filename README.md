![Screenshot](screenshot.jpg)

# 📝 ByteBlog

A simple and extensible blog application built with Django.  
This project allows users to create, read, update, and delete blog posts. It also supports comments and categories.

## 📂 Features

- Create, edit, and delete blog posts
- Comment system
- Categories for organizing posts
- Responsive design
- Django Admin panel for managing content

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Django 5.0.1+
- Virtualenv (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mersad29/JanaShop.git
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin user.
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Open your browser and go to `http://127.0.0.1:8000/` 🌐

## ⚙️ Project Structure

\`\`\`
ByteBlog/
├── Account/         
├── Article/     
├── assets/       
├── ByteBlog/   
├── context_processors/      
├── Index/          
├── media/
├── staticfiles/
├── templates/           
├── manage.py
├── requirements.txt
└── README.md
\`\`\`

## 🛠️ Usage

- Visit /admin/ to manage posts, categories, and users.
- Posts can be categorized and commented on by Admin.


## 📧 Contact

Made by [Mersad29](https://github.com/Mersad29)
