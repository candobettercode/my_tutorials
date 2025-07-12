class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False
        self.menu()

    def menu(self):
        print("Welcome to Chatbook!")
        print("1. Signin")
        print("2. Signup")
        print("3. Write a post")
        print("4. Send a message")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            pass #self.login()
        elif choice == '2':
            pass #self.register()
        elif choice == '3':
            pass #self.write_post()
        elif choice == '4':
            pass #self.send_message()
        elif choice == '5':
            print("Exiting Chatbook. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
            self.menu()

obj = chatbook()
