#This is the main file that will run everything
from database import connect_db
from auth import start
from menu import run_menu

def main():
    connect_db()
    print("\n *********************************************")
    print("          Welcome to Maestro_Vortex            ")
    print("     Where Artists are greatly appreciated!    ")
    print("**********************************************\n")
    user = start()    
    run_menu(user) 
    

if __name__ == "__main__":
    main()    