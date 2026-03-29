#This applies to jobs and tracks application statuses
from datetime import datetime
from database import the_talents

def apply_for_job(user):
    print("\n*** APPLY FOR A JOB ***")
    conn = the_talents()
    jobs = conn.execute("SELECT id, title, company, field FROM jobs").fetchall()
 
    if not jobs:
        print("  No jobs available yet.")
        conn.close()
        return
 
    print("\n  Available Jobs:")
    for i, j in enumerate(jobs, 1):
        print(f"  [{i}] {j[1]} @ {j[2]}  ({j[3]})")
 
    choice = input("\n  Select job number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(jobs)):
        print("  Invalid selection.")
        conn.close()
        return
 
    selected  = jobs[int(choice) - 1]
    job_id    = selected[0]
    job_title = selected[1]
    company   = selected[2]
 
    # Check for duplicate application by this user
    exists = conn.execute(
        "SELECT id FROM applications WHERE job_id = ? AND user_id = ?", (job_id, user[0])
    ).fetchone()
    if exists:
        print(f"\n  You already applied for '{job_title}' at '{company}'.")
        conn.close()
        return
 
    cover_note = input("  Cover note (optional): ").strip() or "None"
 
    conn.execute(
        "INSERT INTO applications (user_id, job_id, job_title, company, cover_note, status, date_applied) VALUES (?,?,?,?,?,?,?)",
        (user[0], job_id, job_title, company, cover_note, "Submitted", datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    conn.commit()
    conn.close()
    print(f"\n  Application submitted for '{job_title}' at '{company}'!")
 
 
def view_my_applications(user):
    """Artists see only their own applications."""
    print(f"\n*** MY APPLICATIONS — {user[1]} ***")
    conn = the_talents()
    rows = conn.execute(
        "SELECT * FROM applications WHERE user_id = ?", (user[0],)
    ).fetchall()
    conn.close()
 
    if not rows:
        print("  No applications yet. Use option [5] to apply.")
        return
 
    _display_applications(rows)
 
 
def view_all_applications():
    """Hirers see all applications from all users."""
    print("\n*** ALL APPLICATIONS ***")
    conn = the_talents()
    rows = conn.execute("""
        SELECT applications.*, users.name
        FROM applications
        JOIN users ON applications.user_id = users.id
        ORDER BY users.name
    """).fetchall()
    conn.close()
 
    if not rows:
        print("  No applications have been submitted yet.")
        return
 
    print(f"  Total Applications: {len(rows)}\n")
    STATUS_ICONS = {"Submitted": "📤", "In Review": "🔎", "Accepted": "✅", "Rejected": "❌"}
    for r in rows:
        icon = STATUS_ICONS.get(r[6], "📤")
        print(f"  {'─' * 40}")
        print(f"  Applicant    : {r[-1]}")
        print(f"  Job          : {r[3]}")
        print(f"  Company      : {r[4]}")
        print(f"  Cover Note   : {r[5]}")
        print(f"  Status       : {icon} {r[6]}")
        print(f"  Date Applied : {r[7]}")
    print(f"  {'─' * 40}")
 
 
def _display_applications(rows):
    STATUS_ICONS = {"Submitted": "📤", "In Review": "🔎", "Accepted": "✅", "Rejected": "❌"}
    for r in rows:
        icon = STATUS_ICONS.get(r[6], "📤")
        print(f"\n  {'─' * 40}")
        print(f"  Job          : {r[3]}")
        print(f"  Company      : {r[4]}")
        print(f"  Cover Note   : {r[5]}")
        print(f"  Status       : {icon} {r[6]}")
        print(f"  Date Applied : {r[7]}")
        print(f"  {'─' * 40}")