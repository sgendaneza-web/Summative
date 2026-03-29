"""
menu.py - Menu Display and Routing
Shows different menus for artists and Hirers.
"""
from portfolio import add_portfolio_project, view_my_portfolio, view_all_portfolios
from jobs import add_job_opportunity, view_job_opportunities
from application import apply_for_job, view_my_applications, view_all_applications

ARTIST_MENU = """
========================================
         MAESTRO VORTEX — ARTIST
========================================
  [1]  Add My Portfolio Project
  [2]  View My Portfolio
  [3]  View All Portfolios
  [4]  View Job Opportunities
  [5]  Apply for a Job
  [6]  View My Applications
  [7]  Exit
========================================"""

Hirer_MENU = """
========================================
         MAESTRO VORTEX — Hirer
========================================
  [1]  View All Portfolios
  [2]  Add Job Opportunity
  [3]  View Job Opportunities
  [4]  View All Applications
  [5]  Exit
========================================"""

def run_menu(user):
    role = user[4]  # 'artist' or 'hirer'

    while True:
        if role == "hirer":
            print(Hirer_MENU)
            choice = input("Enter choice: ").strip()
            if choice == "1":
                view_all_portfolios()
            elif choice == "2":
                add_job_opportunity(user)
            elif choice == "3":
                view_job_opportunities()
            elif choice == "4":
                view_all_applications()
            elif choice == "5":
                print("\n  Goodbye! Keep creating. 🌟\n")
                break
            else:
                print("  Invalid choice. Enter a number from 1 to 5.")

        else:  # artist
            print(ARTIST_MENU)
            choice = input("Enter choice: ").strip()
            if choice == "1":
                add_portfolio_project(user)
            elif choice == "2":
                view_my_portfolio(user)
            elif choice == "3":
                view_all_portfolios()
            elif choice == "4":
                view_job_opportunities()
            elif choice == "5":
                apply_for_job(user)
            elif choice == "6":
                view_my_applications(user)
            elif choice == "7":
                print("\n  Goodbye! Keep creating. \n")
                break
            else:
                print("  Invalid choice. Enter a number from 1 to 7.")