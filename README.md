                          PROJECT OVERVIEW

Maestro Vortex
A command line platform linking creative artists with employment.
Maestro Vortex is a Python application with a built-in SQLite database that is menu-driven and is designed to serve artists and hirers in the creative industry. Artists and hirers can post portfolios and apply and browse respectively.

Features
For Artists:

Create and manage personal portfolio projects.
Look at every portfolio on the site.
See available vacancies.
Make applications using a optional cover note.
Monitor the application status of applications
in progress.

For Hirers / Admins:

Advertise new positions in detail.
View all listed jobs
Visit the entire portfolio of artists.
See the applications that were submitted.


Project Structure
FilePurposemain.pyEntry point - Initialize the database and show menu databasemanager.pyAdd and remove entries to the database and all tables menu.pyDisplay and navigate menus depending on user role application.pyRegister and apply to jobs and follow up on application status portfolio.pyAdd and view projects in a portfolio jobs.pyAdd and view jobs application.pyApply and follow up on status of applications

Database Tables

users -artists and hirers who are registered by the stores.
portfolio — archives portfolio projects of artists.
jobs- stores employment advertisements posted by recruiters.
applications - job application and its statuses.


How to run the file

Requirement Python 3.x (no external dependencies required, built-in Python 3.x to use - sqlite3 and datetime)
bash# Clone the repository
git clone -GitHub: sgendaneza-web/Summative.git

# Run the app
python3 main.py

How to Use

Run main.py to launch the app
Big! Become an Artist or Hirer.
Click into and move your role-action menu.
Artists are able to develop their portfolio and apply to work, Hirers are able to advertise and look at the applications.


Authors
The construction is done by the ALU Peer Learning Project team of the Maestro Vortex.
