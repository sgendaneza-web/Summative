#User Registration and Login (NEW FILE)
#Handles sign up and login for artists and Hirers.
from database import the_talents
 
def register():
    print("\n*** REGISTER ***")
    name     = input("Full Name : ").strip()
    email    = input("Email     : ").strip()
    password = input("Password  : ").strip()
 
    print("\nSelect your role:")
    print("  [1] Artist (Artist, Designer, Photographer, Freelancer)")
    print("  [2] Hirer / Admin")
    role_choice = input("Pick number : ").strip()
    role = "hirer" if role_choice == "2" else "artist"
 
    if not name or not email or not password:
        print("All fields are required.")
        return None
 
    conn = the_talents()
    existing = conn.execute(
        "SELECT id FROM users WHERE email = ?", (email,)
    ).fetchone()
 
    if existing:
        print("\nThis email is already registered. Please login instead.")
        conn.close()
        return None
 
    conn.execute(
        "INSERT INTO users (name, email, password, role) VALUES (?,?,?,?)",
        (name, email, password, role)
    )
    conn.commit()
 
    user = conn.execute(
        "SELECT * FROM users WHERE email = ?", (email,)
    ).fetchone()
    conn.close()
 
    print(f"\n  Welcome to Maestro Vortex, {name}! Account created successfully.")
    return user 
     
def login():
    print("\n*** LOGIN ***")
    email    = input("Email    : ").strip()
    password = input("Password : ").strip()
 
    conn = the_talents()
    user = conn.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?", (email, password)
    ).fetchone()
    conn.close()
 
    if not user:
        print("\n  Incorrect email or password. Please try again.")
        return None
 
    print(f"\n  Welcome back, {user[1]}!")
    return user

def start():
    """Show login or register options and return the logged in user."""
    while True:
        print("\n========================================")
        print("        MAESTRO VORTEX - ACCESS")
        print("========================================")
        print("  [1] Login")
        print("  [2] Register")
        print("  [3] Exit")
        print("========================================")
        choice = input("Enter choice: ").strip()
 
        if choice == "1":
            user = login()
            if user:
                return user
        elif choice == "2":
            user = register()
            if user:
                return user
        elif choice == "3":
            print("\n  Goodbye! 🌟\n")
            exit()
        else:
            print("  Invalid choice. Enter 1, 2 or 3.")

