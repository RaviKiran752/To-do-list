FastAPI Todo App

A simple Todo List web application built with FastAPI (Python backend) and vanilla HTML/CSS/JavaScript (frontend). Add, view, and delete tasks using a clean user interface.
🚀 Features

    View all todos

    Add new todos

    Delete existing todos

    Simple responsive UI

    RESTful API design

🛠️ Tech Stack

    Backend: FastAPI

    Frontend: HTML, CSS, JavaScript

    Data storage: In-memory Python list (no database)

📂 Project Structure

fastapi-todo-app/
│
├── main.py                  # FastAPI backend
├── templates/
│   └── index.html           # Main frontend HTML
├── static/
│   ├── script.js            # Frontend JavaScript
│   └── style.css (optional) # CSS (if separated)
└── README.md                # Project documentation

🧰 Requirements

    Python 3.8+

    fastapi

    uvicorn

📦 Installation

    Clone the repository:

git clone https://github.com/your-username/fastapi-todo-app.git
cd fastapi-todo-app

    Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install dependencies:

pip install fastapi uvicorn

▶️ Running the App

Start the development server with:

uvicorn main:api --reload

    Open your browser and go to: http://127.0.0.1:8000

🔧 API Endpoints
Method	Endpoint	Description
GET	/todos	Get all todos
GET	/todos/{id}	Get a single todo
POST	/todos	Create a new todo
PUT	/todos/{id}	Update an existing todo
DELETE	/todos/{id}	Delete a todo
🎨 UI Preview

    The interface includes:

        List of todos with delete buttons

        Form to add new todos

        Smooth styling with hover effects and layout improvements

📌 Notes

    This project uses in-memory storage. All todos are reset when the server restarts.

    For persistent storage, consider integrating a database (e.g., SQLite, PostgreSQL).

📜 License

MIT License