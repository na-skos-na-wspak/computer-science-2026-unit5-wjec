import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def save_comp(serial_entry, problem_entry, custname_entry, custphone_entry, repairid_entry, is_scrap, is_ready, collection_entry="", full_computers_list=list()):
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
    i = any(char.isdigit() for char in custname)
    if i:
        messagebox.showerror("Error", "There should be no numbers in the customers name.")
        return

    custphone = custphone_entry.get()
    if custphone == "":
        messagebox.showerror("Error", "There is no customer phone number specified.")
        return
    try:
        i = int(custphone)
    except:
        messagebox.showerror("Error", "There should not be any letters in the customer phone number.")
        return

    repairid = repairid_entry.get()
    if repairid == "":
        messagebox.showerror("Error", "There is no data within the repairer id entry.")
        return
    try:
        i = int(repairid)
    except:
        messagebox.showerror("Error", "There should not be any letters in the repairers id.")
        return

    is_s = is_scrap.get()
    is_r = is_ready.get()
    collection_e = collection_entry.get()
    if collection_e == "":
        messagebox.showerror("Error", "There is no data within the collection entry.")
        return
    from datetime import datetime
    format = "%d/%m/%Y"
    try:
        i = bool(datetime.strptime(collection_e, format))
    except:
        messagebox.showerror("Error", "Date is not in DD/MM/YY.")
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
            writer.writerows(full_computers_list)

    else:
        # Appends to the staff file
        with open('computers.csv', 'a', newline='') as list:
            writer = csv.writer(list)
            writer.writerow(save_list)
    
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
        for i in range(len(staff_list)):
            if next_staffid == staff_list[i][0]:
                index = i
        del staff_list[index]
        staff_list.append(save_list)
        
        with open('staff.csv', 'w', newline='') as list:
            writer = csv.writer(list)
            writer.writerows(staff_list)

    else:
        # Appends to the staff file
        with open('staff.csv', 'a', newline='') as list:
            writer = csv.writer(list)
            writer.writerow(save_list)

    # Shows a messagebox once saved
    messagebox.showinfo("Saved", "Given user was saved.")

def staff_add(IsAdmin, main_menu, list_items=0, listbox=0, staff_list=0):
    menu_position = "staff_add"

    if no_staff != 1:
        if staff_list != 0:
            index = listbox.curselection()[0]
            list_items.destroy()
        else:
            main_menu.destroy()
    else:
        no_staff.destroy()


    staff_add = tk.Tk()
    staff_add.title('Staff Modification')
    staff_add.resizable(width=False, height=False)

    # Reads from the staff file to check how many users there are already, to choose a new ID for the user being created
    import csv
    current_staff_list = list(csv.reader(open("staff.csv")))
    
    if list_items != 0:
        next_staffid = staff_list[index][0]
    else:
        next_staffid = len(current_staff_list) + 1

    is_admin = tk.IntVar()
    
    # Inserts the buttons into the menu
    a_back_button = ttk.Button(staff_add, text = "Back", command = lambda: staff_back_button(IsAdmin, staff_add))
    a_back_button.grid(column = 4, row = 0, padx = 2, pady = 2, sticky = "E")

    save_button = ttk.Button(staff_add, text = "Save", command = lambda: save_staff(next_staffid, username_entry, password_entry, fname_entry, sname_entry, email_entry, phonenum_entry, dob_entry, is_admin, staff_list))
    save_button.grid(column = 3, row = 0, padx = 2, pady = 2, sticky = "E")
    
    fname_label = ttk.Label(staff_add, text='First Name:', width = 14)
    fname_label.grid(column = 0, row = 0, padx = 2, pady = 2)
    fname_entry = ttk.Entry(staff_add)
    fname_entry.grid(column = 1, row = 0, padx = 2, pady = 2)
    
    sname_label = ttk.Label(staff_add, text='Second Name:', width = 14)
    sname_label.grid(column = 0, row = 1, padx = 2, pady = 2)
    sname_entry = ttk.Entry(staff_add)
    sname_entry.grid(column = 1, row = 1, padx = 2, pady = 2)

    username_label = ttk.Label(staff_add, text='Username:', width = 14)
    username_label.grid(column = 0, row = 2, padx = 2, pady = 2)
    username_entry = ttk.Entry(staff_add)
    username_entry.grid(column = 1, row = 2, padx = 2, pady = 2)
    
    email_label = ttk.Label(staff_add, text='Email:', width = 14)
    email_label.grid(column = 0, row = 3, padx = 2, pady = 2)
    email_entry = ttk.Entry(staff_add)
    email_entry.grid(column = 1, row = 3, padx = 2, pady = 2)
    
    phonenum_label = ttk.Label(staff_add, text='Phone Number:', width = 14)
    phonenum_label.grid(column = 0, row = 4, padx = 2, pady = 2)
    phonenum_entry = ttk.Entry(staff_add)
    phonenum_entry.grid(column = 1, row = 4, padx = 2, pady = 2)

    dob_label = ttk.Label(staff_add, text='Date Of Birth:', width = 14)
    dob_label.grid(column = 0, row = 5, padx = 2, pady = 2)
    dob_entry = ttk.Entry(staff_add)
    dob_entry.grid(column = 1, row = 5, padx = 2, pady = 2)

    password_label = ttk.Label(staff_add, text='Password:', width = 14)
    password_label.grid(column = 0, row = 6, padx = 2, pady = 2)
    password_entry = ttk.Entry(staff_add)
    password_entry.grid(column = 1, row = 6, padx = 2, pady = 2)

    is_admin_button = ttk.Checkbutton(staff_add, text='Is Admin?', variable = is_admin, onvalue = 1, offvalue = 0, width = 8)
    is_admin_button.grid(column = 3, row = 5, columnspan = 2, padx = 2, pady = 2)

    staffid_label = ttk.Label(staff_add, text='Staff ID: ' + str(next_staffid))
    staffid_label.grid(column = 3, row = 6, columnspan = 2, padx = 2, pady = 2)

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
    
    comp_add.resizable(width=False, height=False)

    is_scrap = tk.IntVar()
    is_ready = tk.IntVar()
    
    # Inserts the buttons into the program
    a_back_button = ttk.Button(comp_add, text = "Back", command = lambda: comp_back_button(IsAdmin, comp_add))
    a_back_button.grid(column = 4, row = 0, padx = 2, pady = 2, sticky = "E")

    save_button = ttk.Button(comp_add, text = "Save", command = lambda: save_comp(serial_entry, problem_entry, custname_entry, custphone_entry, repairid_entry, is_scrap, is_ready, collection_entry, full_computers_list))
    save_button.grid(column = 3, row = 0, padx = 2, pady = 2, sticky = "E")
    
    serial_label = ttk.Label(comp_add, text='Serial:', width = 15)
    serial_label.grid(column = 0, row = 0, padx = 2, pady = 2)
    serial_entry = ttk.Entry(comp_add)
    serial_entry.grid(column = 1, row = 0, padx = 2, pady = 2)

    problem_label = ttk.Label(comp_add, text='Problem:', width = 15)
    problem_label.grid(column = 0, row = 1, padx = 2, pady = 2)
    problem_entry = ttk.Entry(comp_add)
    problem_entry.grid(column = 1, row = 1, padx = 2, pady = 2)

    custname_label = ttk.Label(comp_add, text='Customer Name:', width = 15)
    custname_label.grid(column = 0, row = 3, padx = 2, pady = 2)
    custname_entry = ttk.Entry(comp_add)
    custname_entry.grid(column = 1, row = 3, padx = 2, pady = 2)

    custphone_label = ttk.Label(comp_add, text='Customer Phone:', width = 15)
    custphone_label.grid(column = 0, row = 4, padx = 2, pady = 2)
    custphone_entry = ttk.Entry(comp_add)
    custphone_entry.grid(column = 1, row = 4, padx = 2, pady = 2)
    
    repairid_label = ttk.Label(comp_add, text='Repairer ID:', width = 15)
    repairid_label.grid(column = 0, row = 5, padx = 2, pady = 2)
    repairid_entry = ttk.Entry(comp_add)
    repairid_entry.grid(column = 1, row = 5, padx = 2, pady = 2)

    collection_label = ttk.Label(comp_add, text='Collection Date:', width = 15)
    collection_label.grid(column = 0, row = 6, padx = 2, pady = 2)
    collection_entry = ttk.Entry(comp_add)
    collection_entry.grid(column = 1, row = 6, padx = 2, pady = 2)
    
    # Creates a button if the current user is an admin
    if IsAdmin == 1:
        is_scrap_button = ttk.Checkbutton(comp_add, text='Is Scrap?', variable = is_scrap, onvalue = 1, offvalue = 0, width = 8)
        is_scrap_button.grid(column = 3, row = 5, columnspan = 2, padx = 2, pady = 2)

    is_ready_button = ttk.Checkbutton(comp_add, text='Ready?', variable = is_ready, onvalue = 1, offvalue = 0, width = 8)
    is_ready_button.grid(column = 3, row = 6, columnspan = 2, padx = 2, pady = 2)

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
    list_items.resizable(width=False, height=False)
    
    a_back_button = ttk.Button(list_items, text = "Back", command = lambda: list_back_button(IsAdmin, list_items))
    a_back_button.grid(column = 0, row = 0, padx=2, pady=2, sticky = "E")
    
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
        listbox.grid(column = 0, row = 1, padx=2, pady=2)
        itemselect = ttk.Button(list_items, text = "Select", command = lambda: comp_add(IsAdmin, main_menu, list_items, listbox, computers_list, full_computers_list))
        itemselect.grid(column = 0, row = 2, padx=2, pady=2, sticky = "W")
        delitem = ttk.Button(list_items, text = "Delete", command = lambda: delete_item(IsAdmin, main_menu, list_items, listbox, full_computers_list))
        delitem.grid(column = 0, row = 2, padx=2, pady=2, sticky = "E")
    
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
        listbox.grid(column = 0, row = 1, padx=2, pady=2)
        itemselect = ttk.Button(list_items, text = "Select", command = lambda: staff_add(IsAdmin, main_menu, list_items, listbox, staff_list))
        itemselect.grid(column = 0, row = 2, padx=2, pady=2, sticky = "W")
        delitem = ttk.Button(list_items, text = "Delete", command = lambda: delete_item(IsAdmin, main_menu, list_items, listbox, staff_list))
        delitem.grid(column = 0, row = 2, padx=2, pady=2, sticky = "E")

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
    main_menu.resizable(width=False, height=False)
    
    # Inserts the buttons into the menu
    button_logout = ttk.Button(main_menu, text = "Logout", command = lambda: logout(main_menu))
    button_logout.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "E")

    button_comp_add = ttk.Button(main_menu, text = "Add Computer (Repair/Scrap)", command = lambda: comp_add(IsAdmin, main_menu), width = 25)
    button_comp_add.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = "W")

    button_list_bookings = ttk.Button(main_menu, text = "List Bookings", command = lambda: list_items(IsAdmin, main_menu, comp_r = "1"), width = 25)
    button_list_bookings.grid(row = 2, column = 0, padx = 2, pady = 2)

    # If the account is an admin, insert the real buttons into the program. If not, replace them with buttons displaying an error
    if IsAdmin == 1:
        button_staff_add = ttk.Button(main_menu, text = "Staff Modification", command = lambda: staff_add(IsAdmin, main_menu), width = 25)
        button_staff_add.grid(row = 3, column = 0, padx = 2, pady = 2)

        button_list_bookings = ttk.Button(main_menu, text = "Scrap Listings", command = lambda: list_items(IsAdmin, main_menu, comp_s = "1"), width = 25)
        button_list_bookings.grid(row = 4, column = 0, padx = 2, pady = 2)

        button_list_staff = ttk.Button(main_menu, text = "Staff", command = lambda: list_items(IsAdmin, main_menu, staff_list_b = "1"), width = 25)
        button_list_staff.grid(row = 5, column = 0, padx = 2, pady = 2)
    else:
        button_staff_add = ttk.Button(main_menu, text = "Staff Modification", command = lambda: messagebox.showerror("Authentication Failed", "You are not an admin."), width = 25)
        button_staff_add.grid(row = 6, column = 0, padx = 2, pady = 2)

        button_list_bookings = ttk.Button(main_menu, text = "Scrap Listings", command = lambda: messagebox.showerror("Authentication Failed", "You are not an admin."), width = 25)
        button_list_bookings.grid(row = 7, column = 0, padx = 2, pady = 2)

        button_list_staff = ttk.Button(main_menu, text = "Staff", command = lambda: messagebox.showerror("Authentication Failed", "You are not an admin."), width = 25)
        button_list_staff.grid(row = 8, column = 0, padx = 2, pady = 2)

    main_menu.mainloop()

def login():
    try:
        import csv
        Staff_list = list(csv.reader(open("staff.csv")))
    except:
        no_staff()

    login_prompt = tk.Tk()
    login_prompt.geometry('250x140')
    login_prompt.resizable(False, False)
    login_prompt.title('Login')
    
    # Creates the input boxes for Username and Passowrd
    company_label = ttk.Label(login_prompt, text='PC4U Login', font=("Helvetica", 20))
    company_label.grid(column = 0, row = 0, padx = 2, pady = 4, columnspan = 2)
    username_label = ttk.Label(login_prompt, text='Username:', width = 9)
    username_label.grid(column = 0, row = 1, sticky = "W", padx = 2, pady = 2)
    username = ttk.Entry(login_prompt)
    username.grid(column = 1, row = 1, sticky = "W", padx = 2, pady = 2)
    password_label = ttk.Label(login_prompt, text='Password:', width = 9)
    password_label.grid(column = 0, row = 2, sticky = "W", padx = 2, pady = 2)
    password = ttk.Entry(login_prompt, show="*")
    password.grid(column = 1, row = 2, sticky = "W", padx = 2, pady = 2)
    
    # Creates the login button, which starts attempt_login()
    button_login = ttk.Button(login_prompt, text = "Login", command = lambda: attempt_login(username, password, login_prompt))
    button_login.grid(column = 0, row = 3, padx = 2, pady = 2, columnspan = 2)
    
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

def no_staff():
    no_staff = tk.Tk()
    no_staff.resizable(False, False)
    no_staff.title('Error')
    
    banner_label = ttk.Label(no_staff, text='Halt!', font=("Helvetica", 20))
    banner_label.grid(column = 0, row = 0, padx = 2, pady = 4)
    banner2_label = ttk.Label(no_staff, text='No staff file has been found.\nYou will be given the option\nto create one now.\n\nThis account will be for the admin/owner.\n\nPress the OK button to continue.')
    banner2_label.grid(column = 0, row = 1, padx = 2, pady = 2)

    staff_start_button = ttk.Button(no_staff, text='OK', command = lambda: (newuse(no_staff)))
    staff_start_button.grid(column = 0, row = 2, padx = 2, pady = 2)
    
    no_staff.mainloop()

def newuse(no_staff):
    no_staff.destroy()
    newuse = tk.Tk()
    newuse.resizable(False, False)
    newuse.title('Add a new owner.')
    
    # Inserts the buttons into the menu
    save_button = ttk.Button(newuse, text = "Save", command = lambda: newuse_staff(username_entry, password_entry, fname_entry, sname_entry, email_entry, phonenum_entry, dob_entry))
    save_button.grid(column = 3, row = 0, padx = 2, pady = 2, sticky = "E")
    
    fname_label = ttk.Label(newuse, text='First Name:', width = 14)
    fname_label.grid(column = 0, row = 0, padx = 2, pady = 2)
    fname_entry = ttk.Entry(newuse)
    fname_entry.grid(column = 1, row = 0, padx = 2, pady = 2)
    
    sname_label = ttk.Label(newuse, text='Second Name:', width = 14)
    sname_label.grid(column = 0, row = 1, padx = 2, pady = 2)
    sname_entry = ttk.Entry(newuse)
    sname_entry.grid(column = 1, row = 1, padx = 2, pady = 2)

    username_label = ttk.Label(newuse, text='Username:', width = 14)
    username_label.grid(column = 0, row = 2, padx = 2, pady = 2)
    username_entry = ttk.Entry(newuse)
    username_entry.grid(column = 1, row = 2, padx = 2, pady = 2)
    
    email_label = ttk.Label(newuse, text='Email:', width = 14)
    email_label.grid(column = 0, row = 3, padx = 2, pady = 2)
    email_entry = ttk.Entry(newuse)
    email_entry.grid(column = 1, row = 3, padx = 2, pady = 2)
    
    phonenum_label = ttk.Label(newuse, text='Phone Number:', width = 14)
    phonenum_label.grid(column = 0, row = 4, padx = 2, pady = 2)
    phonenum_entry = ttk.Entry(newuse)
    phonenum_entry.grid(column = 1, row = 4, padx = 2, pady = 2)

    dob_label = ttk.Label(newuse, text='Date Of Birth:', width = 14)
    dob_label.grid(column = 0, row = 5, padx = 2, pady = 2)
    dob_entry = ttk.Entry(newuse)
    dob_entry.grid(column = 1, row = 5, padx = 2, pady = 2)

    password_label = ttk.Label(newuse, text='Password:', width = 14)
    password_label.grid(column = 0, row = 6, padx = 2, pady = 2)
    password_entry = ttk.Entry(newuse)
    password_entry.grid(column = 1, row = 6, padx = 2, pady = 2)

    newuse.mainloop()

def newuse_staff(username_entry, password_entry, fname_entry, sname_entry, email_entry, phonenum_entry, dob_entry):
    import csv
    
    # Gets all of the inputted fields
    next_staffid = str(1)
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
    is_a = str(1)

    save_list = [next_staffid, username, password, fname, sname, email, phonenum, dob, is_a]

    with open('staff.csv', 'w', newline='') as list:
        writer = csv.writer(list)
        writer.writerows(save_list)

    # Shows a messagebox once saved
    messagebox.showinfo("Saved", "The owner has been saved.")

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
