## Promptify

**Promptify** is a full-stack web application built using **Django**.  
It is designed to provide a platform for browsing, searching, and discovering prompts and photos in a clean, minimal UI. 
The website serves as a creative library where users can find high-quality prompts to generate unique images using any AI generative tool of their choice.



## Features

-  **Search with live suggestions** (by category, prompt, or keyword)  
-  **Responsive masonry-style photo grid** (different dimensions fit naturally)  
-  **Browse by categories**  
-  **About & Contact pages**  
-  **User-friendly interface**  
-  **Responsive design for all devices**  



## Technologies Used

- **Django** – Backend framework (Python)  
- **SQLite / PostgreSQL** – Database (depending on setup)  
- **Bootstrap 5** – UI components  
- **Custom CSS (Masonry Grid)** – Responsive photo layout  
- **JavaScript (AJAX)** – Live search suggestions  
- **HTML5 + Django Templates** – Frontend rendering  



## Getting Started

To run **Promptify** locally:

# 1. Clone the repository

    git clone https://github.com/your-username/promptify.git
    cd promptify

# 2. Create and activate a virtual environment

    python -m venv venv
   
  # Activate it
     venv\Scripts\activate      # On Windows
     source venv/bin/activate   # On Mac/Linux
      
# 3. Install dependencies

     pip install -r requirements.txt

# 4. Set up database

    python manage.py migrate

# 5. Create superuser (optional, for admin access)

     python manage.py createsuperuser


# 6. Run the development server

     python manage.py runserver
     Navigate to http://127.0.0.1:8000 in your browser 

## Project Structure

promptify/
│── gallery/            # Main Django app (views, models, templates)
│── static/             # Static files (CSS, JS, images)
│── templates/          # HTML templates
│── db.sqlite3          # Database (SQLite by default)
│── manage.py           # Django project manager


## Roadmap

✅ Basic photo browsing
✅ Categories & About page
✅ Masonry grid photo display
🔄 User authentication (Coming soon)
🔄 Upload prompts & photos (Coming soon)
🔄 Like / Save collections (Future feature)
