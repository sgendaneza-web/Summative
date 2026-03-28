#This is the main file that will run everything
from database import connect_db
from menu import run_menu

def main():
    connect_db()
    print("\n *********************************************")
    print("          Welcome to Maestro_Vortex            ")
    print("     Where Artists are greatly appreciated!    ")
    print("**********************************************\n")
    run_menu()

if __name__ == "__main__":
    main()    