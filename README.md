# 📜AMEA Archives Curator Application 

This repository contains a Django-based web application named **AMEA Archives Curator Application**. It is designed to facilitate the submission and validation of curations by curators, with oversight from a curator head. The application also includes a leaderboard ranking system to highlight the most active users based on the pertinence and acceptance of their curations. 🚀

## ✨ Features 
- Curator authentication and management.
- Submission and validation workflows for curations.
- Leaderboard ranking system to reward active curators.
- A relational database for storing and retrieving information efficiently.

## 📚Project Structure 
- **`manage.py`**: Entry point for project management commands.
- **`db.sqlite3`**: SQLite database for storing application data.
- **`Board/`**: Project settings and configurations.
- **`leader/`**: Django app for managing leaderboard and validation features.
- **`users/`**: Django app for curator authentication and management.

## 🔧Requirements

To run this project, ensure you have the following installed on your system:
- Python 3.8+
- Django 4.0+
- SQLite (comes bundled with Python)

## 🎨🔗Installation and Setup 

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TheAmeaArchives/Board.git
   cd amea-archives
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open a browser and navigate to `http://127.0.0.1:8000/`. 

## 🛠️Technologies Used
- **Django**: Backend web framework.
- **SQLite**: Lightweight database.
- **Python**: Core programming language.

## 🧨🔧Contributing 
If you want to contribute to this project:
- Fork the repository.
- Create a new branch for your feature/fix.
- Submit a pull request with detailed information about your changes.

## 🔒🌐License 
This project is licensed under the MIT License. See the LICENSE file for details.

--- 
Feel free to explore the code and suggest improvements! If you encounter any issues, please report them in the [Issues](https://github.com/TheAmeaArchives/Board.git) section. 🌐📜

