Django Address to Satellite Map
# Project Description

This is a Django web application that:

Accepts a user-entered address

Converts the address into latitude and longitude using Google Geocoding API

Displays the location on an interactive satellite (hybrid) map using Google Maps JavaScript API

This project demonstrates full backend–frontend integration using real-world APIs.

# How It Works
User enters address
        ↓
Django view receives POST request
        ↓
Google Geocoding API converts address → latitude & longitude
        ↓
Coordinates sent to template
        ↓
Google Maps JavaScript API renders satellite map
        ↓
Marker placed on exact location

# Project Structure
mapproject/
│
├── manage.py
├── requirements.txt
├── vercel.json
│
├── maps/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── index.html
│
└── mapproject/
    ├── settings.py
    ├── urls.py
    └── wsgi.py

# Environment Variables
GOOGLE_API_KEY=your_google_api_key_here

# Running Locally
 Navigate to project folder
    cd mapproject
 Create virtual environment
    python -m venv venv
    venv\Scripts\activate
 Run server
    python manage.py runserver

  
