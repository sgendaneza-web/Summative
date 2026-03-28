#Displays the menu
from portfolio import add_portfolio_project, view_portfolio
from jobs import add_job_oppotunity, view_job_opportunities
from application import apply_for_job, view_application

print("===================================================================")
print("                   MAESTRO_VORTEX                                  ")
print("===================================================================")
print(" [1] Add Portfolio")
print(" [2] View Portfolio")
print(" [3] Add job opportunity")
print(" [4] View job opportunities")
print(" [5] Apply for a job")
print(" [6] View my applications")
print(" [7] Exit")
print("===================================================================")


ACTIONS = {
    "1": add_portfolio_project,
    "2": view_portfolio,
    "3": add_job_oppotunity,
    "4": view_job_opportunities,
    "5": apply_for_job,
    "6": view_application,
}

def run_menu():
    while True:
        choice = input("Enter choice: ").strip()
        if choice == "7":
            print("\nGoodbye! \n")
            break
        elif choice in ACTIONS:
            ACTIONS[choice]()
        else:
            print("Invalid choice!")  