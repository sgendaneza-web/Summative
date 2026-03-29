#This is for adding and viewing the portfolio projects
from datetime import datetime
from database import the_talents

CATEGORIES = ["Graphic Design", "Photography", "UI/UX Design", "Illustration", "Video Production",
               "Animation", "Fine Art", "Fashion Design", "Web Design", "Music Production", "Writing", "Other"
               ]

def add_portfolio_project(user):
    print("\n*** ADD PORTFOLIO PROJECT ***")
    title = input("Title : ").strip()
    if not title:
        print("Titl" \
        "Title cannot be empty")
        return

    print("\nCategories: ")
    for i, c in enumerate(CATEGORIES, 1):
        print(f" [{i}] {c}")
    cat = input("Pick number : ").strip()
    category = CATEGORIES[int(cat) - 1] if cat.isdigit() and 1 <= int(cat) <= len(CATEGORIES) else "Other"

    description = input("Description : ").strip()
    tools       = input("Tools used  : ").strip()
    url         = input("Project URL : ").strip() or "N/A"

    conn = the_talents()
    conn.execute(
        "INSERT INTO portfolio (user_id, title, category, tools, url, description, date_added) VALUES (?,?,?,?,?,?,?)",
        (user[0], title, category, tools, url, description, datetime.now().strftime("%Y-%m-%d %H:%M"))
    )                             
    conn.commit()
    conn.close()
    print(f"\n '{title}' added to your portfolio!")


def view_my_portfolio(user):
    print(f"\n*** MY PORTFOLIO — {user[1]} ***")
    conn = the_talents()
    rows = conn.execute(
        "SELECT * FROM portfolio WHERE user_id = ?", (user[0],)
    ).fetchall()
    conn.close()

    if not rows:
        print("  No projects yet. Use option [1] to add one.")
        return

    for r in rows:
        print(f"\n  {'─' * 40}")
        print(f"  ID          : {r[0]}")
        print(f"  Title       : {r[2]}")
        print(f"  Category    : {r[3]}")
        print(f"  Tools       : {r[4]}")
        print(f"  URL         : {r[5]}")
        print(f"  Description : {r[6]}")
        print(f"  Date Added  : {r[7]}")
        print(f"  {'─' * 40}")


def view_all_portfolios():
    print("\n*** ALL PORTFOLIOS ***")
    conn = the_talents()
    rows = conn.execute("""
        SELECT portfolio.*, users.name
        FROM portfolio
        JOIN users ON portfolio.user_id = users.id
        ORDER BY users.name
    """).fetchall()
    conn.close()

    if not rows:
        print("  No portfolios have been added yet.")
        return

    print(f"  Total Projects: {len(rows)}\n")
    for r in rows:
        print(f"  {'─' * 40}")
        print(f"  Artist      : {r[-1]}")
        print(f"  Title       : {r[2]}")
        print(f"  Category    : {r[3]}")
        print(f"  Tools       : {r[4]}")
        print(f"  URL         : {r[5]}")
        print(f"  Description : {r[6]}")
        print(f"  Date Added  : {r[7]}")
        print(f"  {'─' * 40}")