# Simple Flask CRUD App for Course Evaluation

This app allows users to add, edit, and delete test/score entries, and calculates the final grade based on the course evaluation table.

## Features

## Setup
1. Install dependencies:
   ```sh
   pip install flask flask_sqlalchemy
   ```
2. Run the app:
   ```sh
   python app.py
   ```

## File Structure

## Course Evaluation Table
Update the weights in `app.py` as per the course evaluation table in the provided PDF.

## Session Prompts History

 1. Build a simple Flask CRUD app to collect and store test names and scores, then calculate and display the final grade using a course evaluation table.
 2. Set up a Python virtual environment for the project.
 3. Add a launch.json file for debugging the Flask app in VS Code.
 4. Resolve the "Working outside of application context" error for db.create_all().
 5. Change the grade item options to: Lab 1, Lab 2, Lab 3, Lab 4, Lab 5, Lab 6, Midterm, Final, Project.
 6. Update grade calculation weights to: Midterm 20%, Labs (total) 30%, Project 20%, Final 30%.
 7. Apply a modern CSS layout to match the provided design image.
 8. Document all session prompts in the README file.
