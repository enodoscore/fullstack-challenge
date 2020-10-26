# Enodo Fullstack Engineering Challenge

## Description


Front-end and backend to allow users to search, select, or unselect properties from the DB.

## Features

- Frontend with Element.js and Vue.js
- Create DB from data in excel file using Sqlite
- Python Flask API to interact with database
- Element-ui autocomplete displaying the properties from the DB through the API.
  - On Selection of search result, save as "Selected" to DB.
- Table Showing selected properties:
  - Column 1: Full Address
  - Column 2: Class Description
  - Column 3: Delete button
- Include a delete button to unselect property from DB.
- Add a test to your implementation.
- This README

## Runbook

Assumes git, npm, python 3.6+ installed. 

1. Clone project
2. cd to project dir
3. pip install -r api/requirements.txt
4. ./start_app.sh
5. In browser, navigate to localhost:8080 and check it out.
