# #### Superheroes API  
This app is a superhero management backend built with Flask, created on 21/06/2025  
By Bismark Bett


## Description  
This Flask API allows you to manage a database of superheroes and their powers. You can view, update, and assign powers to heroes. An email is sent whenever a hero gets a new power.


## Features / User Stories  

**A User Can:**
- View all superheroes
- View details of a specific superhero including their powers
- View and update power descriptions
- Assign a power to a hero with a specific strength level

**The API Can:**
- Validate that power descriptions are at least 20 characters long
- Validate that hero power strength is one of 'Strong', 'Weak', or 'Average'
- Send an email to a configured address when a new hero power is created

### Known Bugs
The application works perfectly well, no bugs.

### Technologies Used
  Python
  Flask
  Flask SQLAlchemy
  Flask Migrate
  Flask Mail
  Postman
  SQLite
  
## Setup/Installation Requirements
1. **Fork and Clone this repo to your local machine**
   ``bash
  git clone git@github.com:Biss1996/superheroes.git
  cd superheroes
2. **Create a virtual environment and install dependencies**
``bash
       pipenv install
       pipenv shell
3. **Run migrations to create the database**
``bash
       flask db init
       flask db migrate -m "Initial migration"
       flask db upgrade
4. **Seed the database**
``bash
       python seed.py
5. **Run the development server**
``bash
        python app.py


## Support and contact details
Email: bismarckkip684@gmail.com

### MIT License
Copyright 2025 Bismark Bett
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

