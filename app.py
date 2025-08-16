# app.py
import streamlit as st
from student_grade_tracker import add_student, calculate_averages, get_unique_grades

st.title("🎓 Student Grader Tracker")

# Use session state to persist student data across UI interactions
if "students" not in st.session_state:
    st.session_state.students = {}

# Input fields
student_name = st.text_input("Enter student name:")
marks_input = st.text_input("Enter marks (comma separated):")

if st.button("Add Student"):
    if student_name and marks_input:
        marks = [int(x) for x in marks_input.split(",") if x.strip().isdigit()]
        st.session_state.students = add_student(st.session_state.students, student_name, marks)
        st.success(f"Added {student_name} ✅")

# Show averages
if st.button("Show Averages"):
    averages = calculate_averages(st.session_state.students)
    st.write("📊 **Averages:**")
    st.json(averages)

# Show unique grades
if st.button("Show Unique Grades"):
    unique = get_unique_grades(st.session_state.students)
    st.write("🎯 **Unique Grades:**")
    st.write(unique)
