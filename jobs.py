#We're going to add and view job opportunities
from datetime import datetime
from database import the_talents

JOB_TYPES = ["Full-Time", "Part-Time", "Freelance", "Remote", "Hybrid"]
FIELDS = ["Graphic Design", "Photography", "UI/UX Design", "Illustration", "Video Production",
               "Animation", "Fine Art", "Fashion Design", "Web Design", "Music Production", "Writing", "Other"
               ]

def add_job_oppotunity():
    print("\n*** ADD JOB OPPORTUNITY ***")
    title = input("Job Title : ").strip()
    if not title:
        print("Job title can not be empty.")
        return
    
    company = input("Company : ").strip
    location = input("Location : ").strip

    print("\nJob Types: ")
    for i,t in enumerate(JOB_TYPES, 1):
        print(f" [{i}] {f}")
    jt = input("Pick anumber : ")
    job_type = JOB_TYPES[int(jt) - 1] if jt.isdigit() and 1 <= int(jt) <= len(JOB_TYPES) else "Not Specified"   
    print("\nCreative Fields: ")
    for i, f in enumerate(FIELDS, 1):
        print(f" [{i}] {f}")
    fi = input("Pick number : ").strip()
    field = FIELDS[int(fi) - 1] if fi.isdigit() and 1 <= int(fi) <= len(FIELDS) else"Other"


    salary = input("Salary: ")
    deadline = input("Deadline: ")
    description = input("Description: ")
    apply_link = input("Apply Link: ")

    conn = the_talents()
    conn.execute(
        "INSERT INTO jobs (title, company, location, job_type, field, salary, deadline, description, apply_link, date_added) VALUES (?,?,?,?,?,?,?,?,?)",
        (title, company, location, job_type, field, salary  )
    )   
    conn.commit()
    conn.close()
    print(f"\n '{title}' at '{company}' has been added!")

def view_job_opportunities():
    print("\n*** JOB OPPORTUNITIES ***")
    conn = the_talents()
    rows = conn.execute("SELECT * FROM jobs").fetchall
    conn.close()

    if not rows:
        print("No jobs yet. Use option [3] to add one.")
        return
    
    for r in rows:
        print(f"\n ID: {r[0]}")
        print(f" Title : {r[1]}")
        print(f" Company : {r[2]}")
        print(f" Location : {r[3]}")
        print(f" Type : {r[4]}")
        print(f" Field : {r[5]}")
        print(f" Salary : {r[6]}")
        print(f" Deadline : {r[7]}")
        print(f" Description : {r[8]}")
        print(f" Apply Link : {r[9]}")
        print(f" Date Added : {r[10]}")
        print(f"" + "-" * 40)