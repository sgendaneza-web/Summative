#This is for adding and viewing the portfolio projects
from datetime import datetime
from database import the_talents

CATEGORIES = ["Graphic Design", "Photography", "UI/UX Design", "Illustration", "Video Production",
               "Animation", "Fine Art", "Fashion Design", "Web Design", "Music Production", "Writing", "Other"
               ]

def add_portfolio_project():
    print("\n*** ADD PORTFOLIO PROJECT ***")
    title = input("Title : ").strip()
    if not title:
        print("Title cannot be empty")
        return
    
    print("\nCategories: ")
    for i, c in enumerate(CATEGORIES, 1):
        print(f" [{i}] {c}")
    cat = input("Pick number : ").strip()
    category = CATEGORIES[int(cat) - 1] if cat.isdigit() and 1 <= int(cat) <= len(CATEGORIES) else "Other"

    description = input("Description : ").strip()
    tools = input("Tools used: ").strip()
    url = input("Project URL: ").strip()

    conn = the_talents()
    conn.execute(
        "INSERT INTO portfolio (title, category, tools, url, description, date_added) VALUES (?,?,?,?,?,?)",
        (title, category, tools, url, description, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )
    conn.commit()
    conn.close()
    print(f"\n '{title} added to your portfolio!")

def view_portfolio():
    print("\n *** MY PORTFOLIO ***")
    conn = the_talents()
    rows = conn.execute("SELECT * FROM portfolio").fetchall()
    conn.close()

    if not rows:
        print("No projects yet. Use option [1] to add one.")
        return
    
    for r in rows:
        print(f"\n ID : {r[0]}")
        print(f" Title : {r[1]}")
        print(f" Category : {r[2]}")
        print(f" Tools : {r[3]}")
        print(f" URL : {r[4]}")
        print(f" Descriptions : {r[5]}")
        print(f" Date Added : {r[6]}")
        print("" + "-" * 40)