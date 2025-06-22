Superheroes API Manager  

## Description  
This Flask API allows you to manage a database of superheroes and their powers. You can view, update, and assign powers to heroes. An email is sent whenever a hero gets a new power.
## Features / User Stories  

**A User Can:**
- View all episodes.
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

1. **Download or Clone**  
   Fork and Clone this repo:  
   `git@github.com:Biss1996/superheroes.git`

2. **Install Backend Requirements**  
   Open the project in VS Code → Terminal:
   ```bash
   pipenv install
   pipenv shell
3. **Configure Flask Environment**
In .flaskenv or terminal:

``bash
    export FLASK_APP=app:create_app
    export FLASK_ENV=development
    Run Migrations

``bash

    flask db init         
    flask db migrate -m "Initial"
    flask db upgrade
    Seed the Database
Ensure guests.csv is in the root folder, then:

``bash
    python seed.py

4. **Run the Application**

``bash
python app.py  #to run on port 5555


## Deployment
    This is a backend-only project. You can test the endpoints locally or via Postman using the provided collection.


## Support and contact details
    email :: bettkipkoech45@gmail.com

## License
Copyright 2025 BISMARK BETT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

