class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        print(id(self))
        # self.menu()

    def menu(self):
        print("Welcome to Chatbook!")
        print("1. Signin")
        print("2. Signup")
        print("3. Write a post")
        print("4. Send a message")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.signin()
        elif choice == '2':
            self.signup()
        elif choice == '3':
            pass #self.write_post()
        elif choice == '4':
            self.send_message()
        elif choice == '5':
            print("Exiting Chatbook. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
            self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(value):
        chatbook.__user_id = value

    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = email 
        self.password = password
        print("Signup successful! You can now login.")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" or self.password == "":
            print("Please signup first.")
        else:
            print("Signin to your account")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email == self.username and password == self.password:
                self.logged_in = True
                print("Signin successful!")
                print("\n")
                self.menu()
            else:
                print("Invalid credentials. Please try again.")
        print("\n")
        self.menu()

    def send_message(self,msg):
        pass
 

obj = chatbook() 
