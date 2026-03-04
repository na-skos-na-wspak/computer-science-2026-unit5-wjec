import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv

def save_comp(comp_add, IsAdmin, serial_entry, problem_entry, cust_sel_entry, repairid_entry, is_scrap, is_ready, collection_entry="", full_computers_list=list()):
    # Gets all of the inputted fields
    serial = serial_entry.get()
    if serial == "":
        messagebox.showerror("Error", "There is no serial specified.")
        return

    problem = problem_entry.get()
    if problem == "":
        messagebox.showerror("Error", "There is no problem specified.")
        return

    cust_sel = cust_sel_entry.get()
    if cust_sel == "":
        messagebox.showerror("Error", "There is no customer specified.")
        return

    repairid = repairid_entry.get()
    if repairid == "":
        messagebox.showerror("Error", "There is no repairer selected.")
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
        messagebox.showerror("Error", "Date is not in DD/MM/YYYY.")
        return

    save_list = [serial, problem, cust_sel, repairid, is_s, is_r, collection_e]
    
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
    comp_add.destroy()
    main_menu(IsAdmin)

def save_staff(staff_add, IsAdmin, next_staffid, username_entry, password_entry, fname_entry, sname_entry, email_entry, phonenum_entry, dob_entry, is_admin, staff_list=list()):
    
    # Gets all of the inputted fields
    username = username_entry.get()
    if username == "":
        messagebox.showerror("Error", "There is no data within the username entry.")
        return

    password = password_entry.get()
    if password == "":
        messagebox.showerror("Error", "There is no data within the password entry.")
        return
    if len(password) <= 3:
        messagebox.showerror("Error", "Your password is too short.")
        return

    fname = fname_entry.get()
    if fname == "":
        messagebox.showerror("Error", "There is no data within the first name entry.")
        return
    i = any(char.isdigit() for char in username)
    if i:
        messagebox.showerror("Error", "There should be no numbers in the first name.")
        return

    sname = sname_entry.get()
    if sname == "":
        messagebox.showerror("Error", "There is no data within the second name entry.")
        return
    i = any(char.isdigit() for char in username)
    if i:
        messagebox.showerror("Error", "There should be no numbers in the first name.")
        return

    email = email_entry.get()
    if email == "":
        messagebox.showerror("Error", "There is no data within the email entry.")
        return
    if '@' not in email:
        messagebox.showerror("Error", "This is not a valid email address.")
        return

    phonenum = phonenum_entry.get()
    if phonenum == "":
        messagebox.showerror("Error", "There is no data within the phone number entry.")
        return
    try:
        i = int(phonenum)
    except:
        messagebox.showerror("Error", "There should not be any letters in the customer phone number.")
        return

    dob = dob_entry.get()
    if dob == "":
        messagebox.showerror("Error", "There is no data within the Date of Birth entry.")
        return
    from datetime import datetime
    format = "%d/%m/%Y"
    try:
        i = bool(datetime.strptime(dob, format))
    except:
        messagebox.showerror("Error", "Date is not in DD/MM/YYYY.")
        return

    is_a = is_admin.get()

    if next_staffid == "1":
        if is_a != 1:
            messagebox.showerror("Error", "Owner account has to be an admin.")
            return

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
    staff_add.destroy()
    main_menu(IsAdmin)

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
    staff_add.title('Add Staff')
    staff_add.resizable(width=False, height=False)

    # Reads from the staff file to check how many users there are already, to choose a new ID for the user being created
    current_staff_list = list(csv.reader(open("staff.csv")))
    
    if list_items != 0:
        next_staffid = staff_list[index][0]
    else:
        next_staffid = len(current_staff_list) + 1

    is_admin = tk.IntVar()
    
    # Inserts the buttons into the menu
    a_back_button = ttk.Button(staff_add, text = "Back", command = lambda: staff_back_button(IsAdmin, staff_add))
    a_back_button.grid(column = 3, row = 0, padx = 2, pady = 2, sticky = "E")

    save_button = ttk.Button(staff_add, text = "Save", command = lambda: save_staff(staff_add, IsAdmin, next_staffid, username_entry, password_entry, fname_entry, sname_entry, email_entry, phonenum_entry, dob_entry, is_admin, staff_list))
    save_button.grid(column = 3, row = 1, padx = 2, pady = 2, sticky = "E")
    
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
    is_admin_button.grid(column = 3, row = 5, padx = 2, pady = 2)

    staffid_label = ttk.Label(staff_add, text='Staff ID: ' + str(next_staffid))
    staffid_label.grid(column = 3, row = 6, padx = 2, pady = 2)

    if list_items != 0:
        username_entry.insert(0, staff_list[index][1])
        password_entry.insert(0,staff_list[index][2])
        fname_entry.insert(0, staff_list[index][3])
        sname_entry.insert(0, staff_list[index][4])
        email_entry.insert(0, staff_list[index][5])
        phonenum_entry.insert(0, staff_list[index][6])
        dob_entry.insert(0, staff_list[index][7])
        if staff_list[index][8] == "1":
           is_admin_button.invoke()

    staff_add.mainloop()

def cust_save(cust_add, custname_entry, custphone_entry, cust_sel_entry):
    # Gets all of the inputted fields
    custname = custname_entry.get()
    if custname == "":
        messagebox.showerror("Error", "There is no customer name.")
        return
    i = any(char.isdigit() for char in custname)
    if i:
        messagebox.showerror("Error", "There should be no numbers in the customers name.")
        return

    custphone = custphone_entry.get()
    if custphone == "":
        messagebox.showerror("Error", "There is no customer phone number.")
        return
    try:
        i = int(custphone)
    except:
        messagebox.showerror("Error", "There should not be any letters in the customer phone number.")
        return

    save_list = [custname, custphone]
    
    with open('customers.csv', 'a', newline='') as list:
        writer = csv.writer(list)
        writer.writerow(save_list)
    
    # Shows a messagebox once saved
    cust_sel_entry['values'] = [[custname, custphone]]
    messagebox.showinfo("Saved", "Given customer was saved.")
    cust_add.destroy()

def cust_add(cust_sel_entry):
    cust_add = tk.Tk()
    cust_add.title('Add new customer')
    cust_add.resizable(width=False, height=False)

    custname_label = ttk.Label(cust_add, text='Customer Name:', width = 15)
    custname_label.grid(column = 0, row = 1, padx = 2, pady = 2)
    custname_entry = ttk.Entry(cust_add)
    custname_entry.grid(column = 1, row = 1, padx = 2, pady = 2)

    custphone_label = ttk.Label(cust_add, text='Customer Phone:', width = 15)
    custphone_label.grid(column = 0, row = 2, padx = 2, pady = 2)
    custphone_entry = ttk.Entry(cust_add)
    custphone_entry.grid(column = 1, row = 2, padx = 2, pady = 2)

    save_button = ttk.Button(cust_add, text = "Save", command = lambda: cust_save(cust_add, custname_entry, custphone_entry, cust_sel_entry))
    save_button.grid(column = 1, row = 3, padx = 2, pady = 2, sticky = 'E')

    cust_add.mainloop()

def comp_add(IsAdmin, main_menu=0, list_items=0, listbox=0, computers_list=0, full_computers_list=0):
    if list_items != 0:
        try:
            index = listbox.curselection()[0]
        except:
            messagebox.showerror("Error", "You have not selected a computer.")
            return
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
    selrepairid = 0
    current_var = tk.StringVar()
    current_var2 = tk.StringVar()
    
    staff_list = list(csv.reader(open("staff.csv")))

    try:
        cust_list = list(csv.reader(open("customers.csv")))
    except:
        pass

    print(staff_list)

    condensed_list = [[0 for j in range(2)] for i in range(len(staff_list))]
    print(condensed_list)

    for i in range(len(staff_list)):
        #0 denotes the staff id
        #2 denotes the username of the person
        condensed_list[i][0] = staff_list[i][0]
        condensed_list[i][1] = staff_list[i][1]
    
    # Inserts the buttons into the program
    a_back_button = ttk.Button(comp_add, text = "Back", command = lambda: comp_back_button(IsAdmin, comp_add))
    a_back_button.grid(column = 3, row = 0, padx = 2, pady = 2, sticky = "E")

    save_button = ttk.Button(comp_add, text = "Save", command = lambda: save_comp(comp_add, IsAdmin, serial_entry, problem_entry, cust_sel_entry, repairid_entry, is_scrap, is_ready, collection_entry, full_computers_list))
    save_button.grid(column = 3, row = 1, padx = 2, pady = 2, sticky = "E")
    
    serial_label = ttk.Label(comp_add, text = 'Serial:', width = 15)
    serial_label.grid(column = 0, row = 0, padx = 2, pady = 2)
    serial_entry = ttk.Entry(comp_add)
    serial_entry.grid(column = 1, row = 0, padx = 2, pady = 2)

    problem_label = ttk.Label(comp_add, text = 'Problem:', width = 15)
    problem_label.grid(column = 0, row = 1, padx = 2, pady = 2)
    problem_entry = ttk.Entry(comp_add)
    problem_entry.grid(column = 1, row = 1, padx = 2, pady = 2)

#   custname_label = ttk.Label(comp_add, text='Customer Name:', width = 15)
#   custname_label.grid(column = 0, row = 3, padx = 2, pady = 2)
#   custname_entry = ttk.Entry(comp_add)
#   custname_entry.grid(column = 1, row = 3, padx = 2, pady = 2)

#   custphone_label = ttk.Label(comp_add, text='Customer Phone:', width = 15)
#   custphone_label.grid(column = 0, row = 4, padx = 2, pady = 2)
#   custphone_entry = ttk.Entry(comp_add)
#   custphone_entry.grid(column = 1, row = 4, padx = 2, pady = 2)

    add_new_cust = ttk.Button(comp_add, text = 'Add new customer', command = lambda: cust_add(cust_sel_entry), width = 20)
    add_new_cust.grid(column = 0, row = 3, padx = 2, pady = 2, columnspan = 2, sticky = 'E')
    cust_sel_label = ttk.Label(comp_add, text = 'Customer: ', width = 15)
    cust_sel_label.grid(column = 0, row = 4, padx = 2, pady = 2)
    cust_sel_entry = ttk.Combobox(comp_add, textvariable = current_var2, width = 19)
    cust_sel_entry.grid(column = 1, row = 4, padx = 2, pady = 2)
    
    repairid_label = ttk.Label(comp_add, text='Repairer ID:', width = 15)
    repairid_label.grid(column = 0, row = 5, padx = 2, pady = 2)
    repairid_entry = ttk.Combobox(comp_add, textvariable=current_var, width = 19)
    repairid_entry.grid(column = 1, row = 5, padx = 2, pady = 2)

    collection_label = ttk.Label(comp_add, text='Collection Date:', width = 15)
    collection_label.grid(column = 0, row = 6, padx = 2, pady = 2)
    collection_entry = ttk.Entry(comp_add)
    collection_entry.grid(column = 1, row = 6, padx = 2, pady = 2)
    
    # Creates a button if the current user is an admin
    if IsAdmin == 1:
        is_scrap_button = ttk.Checkbutton(comp_add, text='Is Scrap?', variable = is_scrap, onvalue = 1, offvalue = 0, width = 8)
        is_scrap_button.grid(column = 3, row = 5, padx = 2, pady = 2)

    is_ready_button = ttk.Checkbutton(comp_add, text='Ready?', variable = is_ready, onvalue = 1, offvalue = 0, width = 8)
    is_ready_button.grid(column = 3, row = 6, padx = 2, pady = 2)

    if list_items != 0:
        serial_entry.insert(0, computers_list[index][0])
        problem_entry.insert(0, computers_list[index][1])
        cust_sel_entry.insert(0,computers_list[index][2])
        repairid_entry.insert(0, computers_list[index][3])
        if computers_list[index][4] == "1":
           is_scrap_button.invoke()
        if computers_list[index][5] == '1':
           is_ready_button.invoke()
        collection_entry.insert(0, computers_list[index][6])

    repairid_entry['values'] = (condensed_list)
    try:
        cust_sel_entry['values'] = (cust_list)
    except:
        pass

    comp_add.mainloop()

def list_items(IsAdmin, main_menu, comp_r = "", comp_s = "", staff_list_b = ""):
    if staff_list_b == "":
        try:
            open('computers.csv', mode ='r')
        except:
            messagebox.showerror("Error", "There are no computers added yet.")
            return

    main_menu.destroy()
    menu_position = "list_items"

    list_items = tk.Tk()
    list_items.title('List of items')
    list_items.resizable(width=False, height=False)
    
    a_back_button = ttk.Button(list_items, text = "Back", command = lambda: list_back_button(IsAdmin, list_items))
    a_back_button.grid(column = 0, row = 0, padx=2, pady=2, sticky = "E")
    
    
    if staff_list_b == "":
        full_computers_list = list(csv.reader(open("computers.csv")))
        print(full_computers_list)
        computers_list = list(csv.reader(open("computers.csv")))

        poppable_values = []

        if comp_r == "1":
            print("Works Here")
            for i in range(len(computers_list)):
                print(computers_list[i][4])
                if computers_list[i][4] == "1":
                    poppable_values.append(i) 

        if comp_s == "1":
            print("Works Here")
            for i in range(len(computers_list)):
                print(computers_list[i][4])
                if computers_list[i][4] == "0":
                    poppable_values.append(i) 

        for i in sorted(poppable_values, reverse=True):
            del computers_list[i]


        condensed_list = [[0 for j in range(2)] for i in range(len(computers_list))]
        print(condensed_list)

        for i in range(len(computers_list)):
            #0 denotes the serial
            #2 denotes the name of the person who owns the computer
            condensed_list[i][0] = computers_list[i][0]
            condensed_list[i][1] = str(computers_list[i][2])

        list_variable = tk.Variable(value = condensed_list)
        do_what = 0

        listbox = tk.Listbox(list_items, listvariable=list_variable, width = 40)
        listbox.grid(column = 0, row = 1, padx = 8, pady = 2)
        itemselect = ttk.Button(list_items, text = "Select", command = lambda: comp_add(IsAdmin, main_menu, list_items, listbox, computers_list, full_computers_list))
        itemselect.grid(column = 0, row = 2, padx=2, pady=2, sticky = "W")
        delitem = ttk.Button(list_items, text = "Delete", command = lambda: delete_item(IsAdmin, list_items, listbox, full_computers_list, do_what))
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

        list_variable = tk.Variable(value = condensed_list)
        do_what = 1

        listbox = tk.Listbox(list_items, listvariable=list_variable, width = 40)
        listbox.grid(column = 0, row = 1, padx = 8, pady = 2)
        itemselect = ttk.Button(list_items, text = "Select", command = lambda: staff_add(IsAdmin, list_items, listbox, staff_list))
        itemselect.grid(column = 0, row = 2, padx = 2, pady = 2, sticky = "W")
        delitem = ttk.Button(list_items, text = "Delete", command = lambda: delete_item(IsAdmin, list_items, listbox, staff_list, do_what))
        delitem.grid(column = 0, row = 2, padx = 2, pady = 2, sticky = "E")

    list_items.mainloop()

def list_cust(IsAdmin, main_menu):
    try:
        open('staff.csv', mode ='r')
    except:
        messagebox.showerror("Error", "There are no customers added yet.")
        return

    main_menu.destroy()
    menu_position = "list_cust"

    list_items = tk.Tk()
    list_items.title('List of items')
    list_items.resizable(width=False, height=False)
    
    a_back_button = ttk.Button(list_items, text = "Back", command = lambda: list_back_button(IsAdmin, list_items))
    a_back_button.grid(column = 0, row = 0, padx=2, pady=2, sticky = "E")
    
    customers_list = list(csv.reader(open("customers.csv")))

    list_variable = tk.Variable(value = customers_list)

    listbox = tk.Listbox(list_items, listvariable=list_variable, width = 40)
    listbox.grid(column = 0, row = 1, padx = 8, pady = 2)
    delitem = ttk.Button(list_items, text = "Delete", command = lambda: delete_item(IsAdmin, list_items, listbox, customers_list, do_what = 2))
    delitem.grid(column = 0, row = 2, padx=2, pady=2, sticky = "E")


def delete_item(IsAdmin, list_items, listbox, selected_list_before, do_what):
    print(selected_list_before)
    index = listbox.curselection()[0]
    to_delete = selected_list_before[index][0]

    for i in range(len(selected_list_before)):
        if to_delete == selected_list_before[i][0]:
            index = i
    del selected_list_before[index]
        
    if do_what == 0:
        with open('computers.csv', 'w', newline='') as list:
            writer = csv.writer(list)
            writer.writerows(selected_list_before)

        messagebox.showinfo("Item Deleted", "The selected item in the list was deleted.")
        list_items.destroy()
        main_menu(IsAdmin)

    elif do_what == 1:
        if to_delete == "1":
            messagebox.showerror("Error", "You cannot delete the owner account.\nIf you mean to change any of its\ninfo, please edit it instead.")
        else:
            with open('staff.csv', 'w', newline='') as list:
                writer = csv.writer(list)
                writer.writerows(selected_list_before)

            messagebox.showinfo("Item Deleted", "The selected item in the list was deleted.")
            list_items.destroy()
            main_menu(IsAdmin)

    elif do_what == 2:
        with open('customers.csv', 'w', newline='') as list:
            writer = csv.writer(list)
            writer.writerows(selected_list_before)

        messagebox.showinfo("Item Deleted", "The selected item in the list was deleted.")
        list_items.destroy()
        main_menu(IsAdmin)

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
    button_logout.grid(row = 0, column = 0, padx = 4, pady = 2, sticky = "E")

    button_comp_add = ttk.Button(main_menu, text = "Add Computer (Repair/Scrap)", command = lambda: comp_add(IsAdmin, main_menu), width = 25)
    button_comp_add.grid(row = 1, column = 0, padx = 4, pady = 4, sticky = "W")

    button_list_bookings = ttk.Button(main_menu, text = "List Bookings", command = lambda: list_items(IsAdmin, main_menu, comp_r = "1"), width = 25)
    button_list_bookings.grid(row = 2, column = 0, padx = 4, pady = 2)

    customers_list = ttk.Button(main_menu, text = "List Customers", command = lambda: list_cust(IsAdmin, main_menu), width =25)
    customers_list.grid(row = 3, column = 0, padx = 4, pady = 2)

    # If the account is an admin, insert the real buttons into the program. If not, replace them with buttons displaying an error
    if IsAdmin == 1:
        button_staff_add = ttk.Button(main_menu, text = "Add Staff", command = lambda: staff_add(IsAdmin, main_menu), width = 25)
        button_staff_add.grid(row = 4, column = 0, padx = 4, pady = 2)

        button_list_bookings = ttk.Button(main_menu, text = "Scrap Listings", command = lambda: list_items(IsAdmin, main_menu, comp_s = "1"), width = 25)
        button_list_bookings.grid(row = 5, column = 0, padx = 4, pady = 2)

        button_list_staff = ttk.Button(main_menu, text = "Staff", command = lambda: list_items(IsAdmin, main_menu, staff_list_b = "1"), width = 25)
        button_list_staff.grid(row = 6, column = 0, padx = 4, pady = 2)
    else:
        button_staff_add = ttk.Button(main_menu, text = "Add Staff", command = lambda: messagebox.showerror("Authentication Failed", "You are not an admin."), width = 25)
        button_staff_add.grid(row = 4, column = 0, padx = 4, pady = 2)

        button_list_bookings = ttk.Button(main_menu, text = "Scrap Listings", command = lambda: messagebox.showerror("Authentication Failed", "You are not an admin."), width = 25)
        button_list_bookings.grid(row = 5, column = 0, padx = 4, pady = 2)

        button_list_staff = ttk.Button(main_menu, text = "Staff", command = lambda: messagebox.showerror("Authentication Failed", "You are not an admin."), width = 25)
        button_list_staff.grid(row = 6, column = 0, padx = 4, pady = 2)

    main_menu.mainloop()

def login():
    try:
        Staff_list = list(csv.reader(open("staff.csv")))

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
    except:
        no_staff()

def attempt_login(username, password, login_prompt):
    # Gets the inputted username and password
    TempUsername = str(username.get())
    TempPassword = str(password.get())
    # Sets TempPosition to check password associated with username later to a value 
    TempPosition = -1

    # Reads from staff.csv
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
    banner2_label = ttk.Label(no_staff, text='No staff file has been found.\nYou will be given the option\nto create one now.\n\nThis account will be for the admin/owner.\n\nPress the OK button to continue.', justify = "center")
    banner2_label.grid(column = 0, row = 1, padx = 8, pady = 2)

    staff_start_button = ttk.Button(no_staff, text='OK', command = lambda: (newuse(no_staff)))
    staff_start_button.grid(column = 0, row = 2, padx = 2, pady = 2)
    
    no_staff.mainloop()

def newuse(no_staff):
    no_staff.destroy()
    newuse = tk.Tk()
    newuse.resizable(False, False)
    newuse.title('Add a new owner.')
    
    # Inserts the buttons into the menu
    save_button = ttk.Button(newuse, text = "Save", command = lambda: newuse_staff(username_entry, password_entry, fname_entry, sname_entry, email_entry, phonenum_entry, dob_entry, newuse))
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

def newuse_staff(username_entry, password_entry, fname_entry, sname_entry, email_entry, phonenum_entry, dob_entry, newuse):
    fname = fname_entry.get()
    if fname == "":
        messagebox.showerror("Error", "There is no data within the first name entry.")
        return
    i = any(char.isdigit() for char in fname)
    if i:
        messagebox.showerror("Error", "There should be no numbers in the first name.")
        return

    sname = sname_entry.get()
    if sname == "":
        messagebox.showerror("Error", "There is no data within the second name entry.")
        return
    i = any(char.isdigit() for char in sname)
    if i:
        messagebox.showerror("Error", "There should be no numbers in the second name.")
        return

    username = username_entry.get()
    if username == "":
        messagebox.showerror("Error", "There is no data within the username entry.")
        return

    email = email_entry.get()
    if email == "":
        messagebox.showerror("Error", "There is no data within the email entry.")
        return
    if '@' not in email:
        messagebox.showerror("Error", "This is not a valid email address.")
        return

    phonenum = phonenum_entry.get()
    if phonenum == "":
        messagebox.showerror("Error", "There is no data within the phone number entry.")
        return
    try:
        i = int(phonenum)
    except:
        messagebox.showerror("Error", "There should not be any letters in the phone number.")
        return

    dob = dob_entry.get()
    if dob == "":
        messagebox.showerror("Error", "There is no data within the Date of Birth entry.")
        return
    from datetime import datetime
    format = "%d/%m/%Y"
    try:
        i = bool(datetime.strptime(dob, format))
    except:
        messagebox.showerror("Error", "Date is not in DD/MM/YYYY.")
        return

    password = password_entry.get()
    if password == "":
        messagebox.showerror("Error", "There is no data within the password entry.")
        return
    if len(password) <= 3:
        messagebox.showerror("Error", "Your password is too short.")
        return

    is_a = str(1)
    next_staffid = str(1)

    save_list = [next_staffid, username, password, fname, sname, email, phonenum, dob, is_a]

    with open('staff.csv', 'w', newline='') as list:
        writer = csv.writer(list)
        writer.writerow(save_list)

    # Shows a messagebox once saved
    messagebox.showinfo("Saved", "The owner has been saved.")

    newuse.destroy()
    login()


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
