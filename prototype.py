import tkinter as tk
from tkinter import messagebox

def save_comp(serial_entry, problem_entry, custname_entry, custphone_entry, repairid_entry, is_scrap, is_ready, collection_entry="", full_computers_list=list(())):
    import csv

    # Gets all of the inputted fields
    serial = serial_entry.get()
    if serial == "":
        messagebox.showerror("Error", "There is no serial specified.")
        return
    problem = problem_entry.get()
    if problem == "":
        messagebox.showerror("Error", "There is no problem specified.")
        return
    custname = custname_entry.get()
    if custname == "":
        messagebox.showerror("Error", "There is no customer name specified.")
        return
    custphone = custphone_entry.get()
    if custphone == "":
        messagebox.showerror("Error", "There is no customer phone number specified.")
        return
    repairid = repairid_entry.get()
    if repairid == "":
        messagebox.showerror("Error", "There is no data within the repair id entry.")
        return
    is_s = is_scrap.get()
    is_r = is_ready.get()
    collection_e = collection_entry.get()
    if collection_e == "":
        messagebox.showerror("Error", "There is no data within the collection entry.")
        return

    save_list = [serial, problem, custname, custphone, repairid, is_s, is_r, collection_e]
    
    if full_computers_list != 0:
        for i in range(len(full_computers_list)):
            if serial == full_computers_list[i][0]:
                index = i
        del full_computers_list[index]
        full_computers_list.append(save_list)
        
        with open('computers.csv', 'w', newline='') as list:
            writer = csv.writer(list)
            writer.writerow(save_list)
    else:
        # Appends to the staff file
        with open('computers.csv', 'a', newline='') as list:
            writer = csv.writer(list)
            writer.writerow(full_computers_list)
    
    # Shows a messagebox once saved
    messagebox.showinfo("Saved", "Given computer was saved.")

def save_staff(next_staffid, username_entry, password_entry, fname_entry, sname_entry, email_entry, phonenum_entry, dob_entry, is_admin, staff_list=list()):
    import csv
    
    # Gets all of the inputted fields
    username = username_entry.get()
    if username == "":
        messagebox.showerror("Error", "There is no data within the username entry.")
        return
    password = password_entry.get()
    if password == "":
        messagebox.showerror("Error", "There is no data within the password entry.")
        return
    fname = fname_entry.get()
    if fname == "":
        messagebox.showerror("Error", "There is no data within the first name entry.")
        return
    sname = sname_entry.get()
    if sname == "":
        messagebox.showerror("Error", "There is no data within the second name entry.")
        return
    email = email_entry.get()
    if email == "":
        messagebox.showerror("Error", "There is no data within the email entry.")
        return
    phonenum = phonenum_entry.get()
    if phonenum == "":
        messagebox.showerror("Error", "There is no data within the phone number entry.")
        return
    dob = dob_entry.get()
    if dob == "":
        messagebox.showerror("Error", "There is no data within the Date of Birth entry.")
        return
    is_a = is_admin.get()

    save_list = [next_staffid, username, password, fname, sname, email, phonenum, dob, is_a]

    if staff_list != 0:
        poppable_values = []
        for i in range(len(staff_list)):
            if next_staffid == staff_list[i][0]:
                index = i
        poppable_values.append(index)
        del staff_list[index]
        staff_list.append(save_list)
        
        with open('staff.csv', 'w', newline='') as list:
            writer = csv.writer(list)
            writer.writerow(save_list)
    else:
        # Appends to the staff file
        with open('staff.csv', 'a', newline='') as list:
            writer = csv.writer(list)
            writer.writerow(save_list)

        # Shows a messagebox once saved
    messagebox.showinfo("Saved", "Given user was saved.")

def staff_add(IsAdmin, main_menu, list_items=0, listbox=0, staff_list=0):
    menu_position = "staff_add"
    if staff_list != 0:
        index = listbox.curselection()[0]
        list_items.destroy()
    else:
        main_menu.destroy()

    staff_add = tk.Tk()
    staff_add.title('Staff Modification')

    # Reads from the staff file to check how many users there are already, to choose a new ID for the user being created
    import csv
    current_staff_list = list(csv.reader(open("staff.csv")))
    
    if list_items != 0:
        next_staffid = staff_list[index][0]
    else:
        next_staffid = len(current_staff_list) + 1

    is_admin = tk.IntVar()
    
    # Inserts the buttons into the menu
    a_back_button = tk.Button(staff_add, text = "Back", command = lambda: staff_back_button(IsAdmin, staff_add))
    a_back_button.pack()

    save_button = tk.Button(staff_add, text = "Save", command = lambda: save_staff(next_staffid, username_entry, password_entry, fname_entry, sname_entry, email_entry, phonenum_entry, dob_entry, is_admin))
    save_button.pack()
    
    staffid_label = tk.Label(staff_add, text='Staff ID\n' + str(next_staffid))
    staffid_label.pack()

    username_label = tk.Label(staff_add, text='Username')
    username_label.pack()
    username_entry = tk.Entry(staff_add)
    username_entry.pack()

    password_label = tk.Label(staff_add, text='Password')
    password_label.pack()
    password_entry = tk.Entry(staff_add)
    password_entry.pack()

    fname_label = tk.Label(staff_add, text='First Name')
    fname_label.pack()
    fname_entry = tk.Entry(staff_add)
    fname_entry.pack()
    
    sname_label = tk.Label(staff_add, text='Second Name')
    sname_label.pack()
    sname_entry = tk.Entry(staff_add)
    sname_entry.pack()

    email_label = tk.Label(staff_add, text='Email')
    email_label.pack()
    email_entry = tk.Entry(staff_add)
    email_entry.pack()
    
    phonenum_label = tk.Label(staff_add, text='Phone Number')
    phonenum_label.pack()
    phonenum_entry = tk.Entry(staff_add)
    phonenum_entry.pack()

    dob_label = tk.Label(staff_add, text='Date Of Birth')
    dob_label.pack()
    dob_entry = tk.Entry(staff_add)
    dob_entry.pack()

    is_admin_button = tk.Checkbutton(staff_add, text='Is Admin?', variable = is_admin, onvalue = 1, offvalue = 0)
    is_admin_button.pack()

    if list_items != 0:
        username_entry.insert(0, staff_list[index][1])
        password_entry.insert(0,staff_list[index][2])
        fname_entry.insert(0, staff_list[index][3])
        sname_entry.insert(0, staff_list[index][4])
        email_entry.insert(0, staff_list[index][5])
        phonenum_entry.insert(0, staff_list[index][6])
        dob_entry.insert(0, staff_list[index][7])
        if staff_list[index][7] == "1":
           is_scrap_button.select()

    staff_add.mainloop()

def comp_add(IsAdmin, main_menu=0, list_items=0, listbox=0, computers_list=0, full_computers_list=0):
    if list_items != 0:
        index = listbox.curselection()[0]
        list_items.destroy()
    else:
        main_menu.destroy()

    comp_add = tk.Tk()

    if list_items != 0:
        comp_add.title('Modify Computer')
    else:
        comp_add.title('Add new Computer')

    menu_position = "comp_add"
    
    is_scrap = tk.IntVar()
    is_ready = tk.IntVar()
    
    # Inserts the buttons into the program
    a_back_button = tk.Button(comp_add, text = "Back", command = lambda: comp_back_button(IsAdmin, comp_add))
    a_back_button.pack()

    save_button = tk.Button(comp_add, text = "Save", command = lambda: save_comp(serial_entry, problem_entry, custname_entry, custphone_entry, repairid_entry, is_scrap, is_ready, collection_entry, full_computers_list))
    save_button.pack()
    
    serial_label = tk.Label(comp_add, text='Serial')
    serial_label.pack()
    serial_entry = tk.Entry(comp_add)
    serial_entry.pack()

    problem_label = tk.Label(comp_add, text='Problem')
    problem_label.pack()
    problem_entry = tk.Entry(comp_add)
    problem_entry.pack()

    custname_label = tk.Label(comp_add, text='Customer Name')
    custname_label.pack()
    custname_entry = tk.Entry(comp_add)
    custname_entry.pack()

    custphone_label = tk.Label(comp_add, text='Customer Phone')
    custphone_label.pack()
    custphone_entry = tk.Entry(comp_add)
    custphone_entry.pack()
    
    repairid_label = tk.Label(comp_add, text='Repairer ID')
    repairid_label.pack()
    repairid_entry = tk.Entry(comp_add)
    repairid_entry.pack()

    collection_label = tk.Label(comp_add, text='Collection Date')
    collection_label.pack()
    collection_entry = tk.Entry(comp_add)
    collection_entry.pack()
    
    # Creates a button if the current user is an admin
    if IsAdmin == 1:
        is_scrap_button = tk.Checkbutton(comp_add, text='Is Scrap?', variable = is_scrap, onvalue = 1, offvalue = 0)
        is_scrap_button.pack()

    is_ready_button = tk.Checkbutton(comp_add, text='Ready?', variable = is_ready, onvalue = 1, offvalue = 0)
    is_ready_button.pack()

    if list_items != 0:
        serial_entry.insert(0, computers_list[index][0])
        problem_entry.insert(0, computers_list[index][1])
        custname_entry.insert(0,computers_list[index][2])
        custphone_entry.insert(0, computers_list[index][3])
        repairid_entry.insert(0, computers_list[index][4])
        if computers_list[index][5] == "1":
           is_scrap_button.select()
        if computers_list[index][6] == '1':
           is_ready_button.select()
        collection_entry.insert(0, computers_list[index][7])

    comp_add.mainloop()

def list_items(IsAdmin, main_menu, comp_r = "", comp_s = "", staff_list_b = ""):
    main_menu.destroy()
    menu_position = "list_items"

    list_items = tk.Tk()
    list_items.title('List of items')
    
    a_back_button = tk.Button(list_items, text = "Back", command = lambda: list_back_button(IsAdmin, list_items))
    a_back_button.pack()
    
    import csv
    
    if staff_list_b == "":
        full_computers_list = list(csv.reader(open("computers.csv")))
        print(full_computers_list)
        computers_list = list(csv.reader(open("computers.csv")))


        poppable_values = []

        if comp_r == "1":
            print("Works Here")
            for i in range(len(computers_list)):
                print(computers_list[i][5])
                if computers_list[i][5] == "1":
                    poppable_values.append(i) 

        if comp_s == "1":
            print("Works Here")
            for i in range(len(computers_list)):
                print(computers_list[i][5])
                if computers_list[i][5] == "0":
                    poppable_values.append(i) 

        for i in sorted(poppable_values, reverse=True):
            del computers_list[i]


        condensed_list = [[0 for j in range(2)] for i in range(len(computers_list))]
        print(condensed_list)

        for i in range(len(computers_list)):
            #0 denotes the serial
            #2 denotes the name of the person who owns the computer
            condensed_list[i][0] = computers_list[i][0]
            condensed_list[i][1] = computers_list[i][2]

        list_variable = tk.Variable(value=condensed_list)

        listbox = tk.Listbox(list_items, listvariable=list_variable)
        listbox.pack(padx=10, pady=10, expand=True)
        itemselect = tk.Button(list_items, text = "Select", command = lambda: comp_add(IsAdmin, main_menu, list_items, listbox, computers_list, full_computers_list))
        itemselect.pack()
        delitem = tk.Button(list_items, text = "Delete", command = lambda: delete_item(IsAdmin, main_menu, list_items, listbox, full_computers_list))
        delitem.pack()
    
    else:
        staff_list = list(csv.reader(open("staff.csv")))
        print(staff_list)

        condensed_list = [[0 for j in range(2)] for i in range(len(staff_list))]
        print(condensed_list)

        for i in range(len(staff_list)):
            #0 denotes the staff id
            #2 denotes the name of the person
            condensed_list[i][0] = staff_list[i][0]
            condensed_list[i][1] = staff_list[i][1]

        list_variable = tk.Variable(value=condensed_list)

        listbox = tk.Listbox(list_items, listvariable=list_variable)
        listbox.pack(padx=10, pady=10, expand=True)
        itemselect = tk.Button(list_items, text = "Select", command = lambda: staff_add(IsAdmin, main_menu, list_items, listbox, staff_list))
        itemselect.pack()
        delitem = tk.Button(list_items, text = "Delete", command = lambda: delete_item(IsAdmin, main_menu, list_items, listbox, staff_list))
        delitem.pack()
    

    list_items.mainloop()

def delete_item(IsAdmin, main_menu, list_items, listbox, computers_list):
    index_value = -1
    
    serial = serial_entry.get()

    for i in range(7):
        if serial == computers_list[i][0]:
            index_value = i
            print(index_value)
    
    if index_value != -1:
        with open('computers.csv', 'w+', newline='') as list:
            writer = csv.writer(list)
            writer.strip(index_value)

# Destroys the main menu and returns to the login
def logout(main_menu):
    main_menu.destroy()
    login()

def main_menu(IsAdmin):
    print(IsAdmin)
    main_menu = tk.Tk()
    main_menu.title('Main Menu')
    main_menu.geometry('300x200')
    
    # Inserts the buttons into the menu
    button_logout = tk.Button(main_menu, text = "Logout", command = lambda: logout(main_menu))
    button_logout.pack()

    button_comp_add = tk.Button(main_menu, text = "Add Computer (Repair/Scrap)", command = lambda: comp_add(IsAdmin, main_menu))
    button_comp_add.pack()

    button_list_bookings = tk.Button(main_menu, text = "List Bookings", command = lambda: list_items(IsAdmin, main_menu, comp_r = "1"))
    button_list_bookings.pack()

    # If the account is an admin, insert the real buttons into the program. If not, replace them with buttons displaying an error
    if IsAdmin == 1:
        button_staff_add = tk.Button(main_menu, text = "Staff Modification", command = lambda: staff_add(IsAdmin, main_menu))
        button_staff_add.pack()

        button_list_bookings = tk.Button(main_menu, text = "Scrap Listings", command = lambda: list_items(IsAdmin, main_menu, comp_s = "1"))
        button_list_bookings.pack()

        button_list_staff = tk.Button(main_menu, text = "Staff", command = lambda: list_items(IsAdmin, main_menu, staff_list_b = "1"))
        button_list_staff.pack()
    else:
        button_staff_add = tk.Button(main_menu, text = "Staff Modification", command = lambda: messagebox.showerror("Authentication Failed", "You are not an admin."))
        button_staff_add.pack()

        button_list_bookings = tk.Button(main_menu, text = "Scrap Listings", command = lambda: messagebox.showerror("Authentication Failed", "You are not an admin."))
        button_list_bookings.pack()

        button_list_staff = tk.Button(main_menu, text = "Staff", command = lambda: messagebox.showerror("Authentication Failed", "You are not an admin."))
        button_list_staff.pack()

    main_menu.mainloop()

def login():
    login_prompt = tk.Tk()
    login_prompt.geometry('200x150')
    login_prompt.title('Login')

    try:
        import csv
        Staff_list = list(csv.reader(open("staff.csv")))
        if Staff_list == []:
            print("There is no staff")
    except:
        print("Loaded")

    
    # Creates the input boxes for Username and Passowrd
    username_label = tk.Label(login_prompt, text='Username:')
    username_label.pack()
    username = tk.Entry(login_prompt)
    username.pack()
    password_label = tk.Label(login_prompt, text='Password:')
    password_label.pack()
    password = tk.Entry(login_prompt, show="*")
    password.pack()
    
    # Creates the login button, which starts attempt_login()
    button_login = tk.Button(login_prompt, text = "Login", command = lambda: attempt_login(username, password, login_prompt))
    button_login.pack()
    
    login_prompt.mainloop()

def attempt_login(username, password, login_prompt):
    # Gets the inputted username and password
    TempUsername = str(username.get())
    TempPassword = str(password.get())
    # Sets TempPosition to check password associated with username later to a value 
    TempPosition = -1

    # Reads from staff.csv
    import csv
    Staff_list = list(csv.reader(open("staff.csv")))

    # Searches through the read file to see see whether usename matches any of the items
    for i in range(len(Staff_list)):
        if TempUsername == Staff_list[i][1]:
            TempPosition = i

    # If TempPassword equals the associated password with the found TempPosition, check whether the account is an admin
    if TempPassword == Staff_list[TempPosition][2]:
        if Staff_list[TempPosition][8] == "1":
            IsAdmin = 1
        else:
            IsAdmin = 0

        login_prompt.destroy()
        main_menu(IsAdmin)
        
    # Show an errorbox if not
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Defines the back buttons for all of the seperate menus
def comp_back_button(IsAdmin, comp_add):
        comp_add.destroy()
        main_menu(IsAdmin)

def staff_back_button(IsAdmin, staff_add):
        staff_add.destroy()
        main_menu(IsAdmin)

def list_back_button(IsAdmin, list_items):
        list_items.destroy()
        main_menu(IsAdmin)

login()
