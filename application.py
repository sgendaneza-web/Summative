#This applies to jobs and tracks application statuses
from datetime import datetime
from database import the_talents

def apply_for_job():
    print("\n *** APPLY FOR A JOB***")
    conn = the_talents()
    jobs = conn.execute("SELECT id, title, company, field FROM jobs").fetchall()

    if not jobs:
        print("No jobs available.")
        conn.close()
        return
    
    print("\n Available jobs: ")
    for i,j in enumerate(jobs, 1):
        print(f"[{i}] {j[1]} @ {j[2]} ({j[3]})")

    choice = input("\nSelect job number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(jobs)):
        print("Invalid selection.")
        conn.close
        return

    selected = jobs[int(choice) - 1] 
    job_id, job_title, company = selected[0], selected[1], selected[2]  

    exists = conn.execute(
        "SELECT id FROM applications WHERE job_id = ?", (job_id,)
    ).fetchone()
    if exists:
        print(f"\n You already applied for '{job_title}' at '{company}'.")
        conn.close()
        return
    
    cover_note = input("COver not (optional): ").strip()

    conn.execute(
        "INSERT INTO applications (job_id, job_title, company, cover_note, status, date_applied) VALUES (?,?,?,?,?,?)",
        (job_id, job_title, company, cover_note, "Submitted", datetime.now().strftimr("%Y-%m-%d %H:%M"))
    )
    conn.commit()
    conn.close()
    print(f"\n Application submitted for '{job_title}' at '{company}'!")

def view_application():
    print("\n *** MY APPLICATIONS ***")
    conn = the_talents()
    rows = conn.execute("SELECT * FROM application").fetchall()
    conn.close()

    if not rows:
        print("No applications yet. Use option [5] to apply")
        return
    
    STATUS_iCONS = {"Submitted", "In Review", "Accepted", "Rejected"}
    for r in rows:
        icon = STATUS_iCONS.get(r[5])
        print(f"\n ID : {r[0]}")
        print(f" Job : {r[2]}")
        print(f"Company : {r[3]}")
        print(f" Cover Note : {r[4]}")
        print(f" Status : {icon} {r[5]}")
        print(f" Date Applied : {r[6]}")
        print(f"" + "" * 40)