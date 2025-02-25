# web_app
# Openverse Media Search Web Application

## Overview

This web application allows users to search for and browse open-license media using the Openverse API. The application features a user-friendly interface, robust user account management, secure user data handling, and advanced media search and filtering capabilities. It is designed with software engineering best practices, including modular architecture, automated testing, and containerization using Docker.

---

## Features

- **User Account Management**:
  - User registration and authentication
  - Ability to save, retrieve, and delete recent searches
  - Secure handling of user data

- **Media Search**:
  - Integration with Openverse API for searching and retrieving openly-licensed media
  - Advanced search and filtering capabilities (e.g., by type, license, and more)
  - Ability to display and play media (e.g., images, audio, video)

- **Software Engineering Best Practices**:
  - Modular and scalable architecture using object-oriented programming (OOP)
  - Containerization with Docker
  - Automated build and testing strategies
  - Clean, well-documented code

---

## Getting Started

These instructions will guide you on how to get your project running on your local machine.

### Prerequisites

Make sure you have the following installed:
- **Python 3.x** – Programming language
- **MySQL** – Database system for storing user data and search histories
- **Docker** – For containerization (optional for deployment)
- **Git** – To clone the repository

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rabin8-tech/web_app.git
   cd web_app
Create a virtual environment and install the required packages:

bash
python3 -m venv venv
# On Windows: venv\Scripts\activate
pip install -r requirements.txt
Set up your MySQL database and configure the database connection:

Create a database media_search and ensure your MySQL user has the correct privileges.
Configure your app.py or .env file to match your database credentials.
Set up Docker (Optional):

Run the following to build and run the app in a container:

docker-compose up --build
Running the Application

Start the Flask development server:

python app.py
Open your browser and visit http://127.0.0.1:5000/ to access the application.

Testing
To run tests for the application:
pytest


Architectural Design
1. User Authentication and Authorization:
The system implements JWT authentication for secure user management.
Users can register, log in, and manage their search history securely.
2. Database Architecture:
A MySQL database is used to store user credentials and recent search queries.
Tables include: users, search_history.
3. Openverse API Integration:
The application integrates with the Openverse API to fetch open-license media.
API endpoints: /search for querying media and displaying results.
4. UI/UX Design:
The web interface is designed to be responsive and easy to use, with features like advanced search filters and media playback.
Technologies Used
Flask – Web framework for Python
MySQL – Database
Requests – HTTP requests library for API integration
Docker – For containerization and deployment
GitHub Actions – Automated CI/CD pipeline (if applicable)
JWT – JSON Web Token for user authentication

Project Documentation
1. Introduction (Critical Reflection on Software Engineering Principles)
In this section, you’ll discuss the rationale for choosing Flask, MySQL, and other technologies. You'll also reflect on current trends in software engineering and explain how they influenced your choices.

2. Project Planning
This section contains the architectural diagrams, use of design patterns, project timeline, risk management, and other important planning elements.

3. Project Management and Development Process
This section includes details on how you managed the project through GitHub, how you developed features, and how you tracked progress with issues, milestones, and pull requests.

4. Testing, Building, and Containerization
This section documents the testing methodology, automated tests, Docker container setup, and how you ensured portability and scalability.

Contribution
If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. Please ensure that your code follows the project’s coding standards and includes tests for new features.

License
This project is licensed under the MIT License – see the LICENSE file for details.

Acknowledgements
Openverse – for providing the API to retrieve open-license media.
Flask – for being the backbone of the web application.
Additional Information
You can refer to the project report and video demonstration for more details on the design, development, testing, and deployment processes.

Project Report – [Link to PDF]
Video Demonstration – [Link to Video]
markdown

---






