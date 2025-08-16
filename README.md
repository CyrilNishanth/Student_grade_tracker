Student Grader Tracker

A simple Streamlit web app to manage students, their subject marks, calculate averages, and view unique grades — all in one place!
Currently, the app stores student data in memory while the session is active (no external database needed).

🚀 Features

Add multiple students with their subject marks.

Calculate the average marks for each student.

Show all unique grades entered across students.

Simple, clean UI with interactive buttons.

🛠️ Installation

Clone this repository:

git clone https://github.com/your-username/student-grader-tracker.git
cd student-grader-tracker


(Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

▶️ Usage

Run the Streamlit app:

streamlit run app.py


Then open the link shown in your terminal (usually http://localhost:8501) in your browser.

📌 Notes

Data is stored temporarily in memory during the app session.

If you refresh or restart the app, student data will reset.

For permanent storage, future versions may include JSON/CSV/database integration.

🤝 Contributing

Fork the repo.

Create a new branch:

git checkout -b feature-branch


Commit your changes:

git commit -m "Added new feature"


Push to your branch:

git push origin feature-branch


Open a Pull Request 🚀



✍️ Author: [Cyril Nishanth]
