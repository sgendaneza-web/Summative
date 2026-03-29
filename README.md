Maestro Vortex 🎨
A command-line platform connecting creative artists with job opportunities.
Maestro Vortex is a menu-driven Python application with SQLite database integration, built for artists and hirers in the creative industry. Artists can showcase their portfolios and apply for jobs, while hirers can post opportunities and browse applicants.

Features
For Artists:

Add and view personal portfolio projects
Browse all portfolios on the platform
View available job opportunities
Apply for jobs with an optional cover note
Track the status of submitted applications

For Hirers / Admins:

Post new job opportunities with full details
View all listed jobs
Browse all artist portfolios
View all submitted applications


Project Structure
FilePurposemain.pyEntry point — initializes the database and launches the menudatabase.pyCreates and manages the SQLite database and all tablesmenu.pyHandles menu display and routing based on user roleauth.pyUser registration and login for artists and hirersportfolio.pyAdd and view portfolio projectsjobs.pyAdd and view job opportunitiesapplication.pyApply for jobs and track application statuses

Database Tables

users — stores registered artists and hirers
portfolio — stores portfolio projects linked to artists
jobs — stores job listings posted by hirers
applications — tracks job applications and their statuses


How to run the file

Requirements: Python 3.x (no external libraries needed — uses built-in sqlite3 and datetime)
bash# Clone the repository
git clone https://github.com/your-username/alu-higher_level_programming.git

# Navigate to the project folder
cd maestro-vortex

# Run the app
python3 main.py

How to Use

Run main.py to launch the app
Register as an Artist or Hirer
Log in and navigate your role-specific menu
Artists can build their portfolio and apply for jobs; Hirers can post listings and review applications


Authors
Built by the Maestro Vortex team as part of the ALU Peer Learning Project.
