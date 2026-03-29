#We're going to add and view job opportunities
from datetime import datetime
from database import the_talents

JOB_TYPES = ["Full-Time", "Part-Time", "Freelance", "Internship", "Remote", "Hybrid"]
FIELDS     = [
    "Graphic Design", "Photography", "Video Production", "UI/UX Design",
    "Illustration", "Animation", "Fashion Design", "Web Design",
    "Fine Arts", "Music Production", "Artist Writing", "Other"
]
 
def add_job_opportunity(user):
    print("\n*** ADD JOB OPPORTUNITY ***")
    title = input("Job Title   : ").strip()
    if not title:
        print("Job title cannot be empty.")
        return
 
    company  = input("Company     : ").strip() or "Unknown"
    location = input("Location    : ").strip() or "Not Specified"
 
    print("\nJob Types:")
    for i, t in enumerate(JOB_TYPES, 1):
        print(f"  [{i}] {t}")
    jt       = input("Pick number : ").strip()
    job_type = JOB_TYPES[int(jt) - 1] if jt.isdigit() and 1 <= int(jt) <= len(JOB_TYPES) else "Not Specified"
 
    print("\nArtist Fields:")
    for i, f in enumerate(FIELDS, 1):
        print(f"  [{i}] {f}")
    fi    = input("Pick number : ").strip()
    field = FIELDS[int(fi) - 1] if fi.isdigit() and 1 <= int(fi) <= len(FIELDS) else "Other"
 
    salary      = input("Salary      : ").strip() or "Not Disclosed"
    deadline    = input("Deadline    : ").strip() or "Not Specified"
    description = input("Description : ").strip()
    apply_link  = input("Apply Link  : ").strip() or "N/A"
 
    conn = the_talents()
    conn.execute(
        "INSERT INTO jobs (user_id, title, company, location, job_type, field, salary, deadline, description, apply_link, date_added) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (user[0], title, company, location, job_type, field, salary, deadline, description, apply_link, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    conn.commit()
    conn.close()
    print(f"\n  '{title}' at '{company}' has been added!")
 
 
def view_job_opportunities():
    print("\n*** JOB OPPORTUNITIES ***")
    conn = the_talents()
    rows = conn.execute("SELECT * FROM jobs").fetchall()
    conn.close()
 
    if not rows:
        print("  No jobs yet.")
        return
 
    for r in rows:
        print(f"\n  {'─' * 40}")
        print(f"  ID          : {r[0]}")
        print(f"  Title       : {r[2]}")
        print(f"  Company     : {r[3]}")
        print(f"  Location    : {r[4]}")
        print(f"  Type        : {r[5]}")
        print(f"  Field       : {r[6]}")
        print(f"  Salary      : {r[7]}")
        print(f"  Deadline    : {r[8]}")
        print(f"  Description : {r[9]}")
        print(f"  Apply Link  : {r[10]}")
        print(f"  Date Added  : {r[11]}")
        print(f"  {'─' * 40}")