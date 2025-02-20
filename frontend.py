#Aiden Fatta
#11/25/2024
#Frontend for the VITA Volunteer Management System

from tkinter import *
import backend as back
import emailSystem
import emailSystem as emSys

window = Tk()
window.title("VITA Volunteer Database")
window.minsize(width=600, height=600)

#Labels
lb1 = Label(window, text="Name")
lb1.grid(row=0, column=0, columnspan=1)

lb2 = Label(window, text="Job")
lb2.grid(row=1, column=0, columnspan=1)

lb3 = Label(window, text="Affiliation")
lb3.grid(row=2, column=0, columnspan=1)

lb4 = Label(window, text="Email")
lb4.grid(row=3, column=0, columnspan=1)

lb5 = Label(window, text="Phone Number")
lb5.grid(row=4, column=0, columnspan=1)

#Entryboxs
name_text = StringVar()
en1 = Entry(window, textvariable=name_text)
en1.grid(row=0, column=2)

job_text = StringVar()
en2 = Entry(window, textvariable=job_text)
en2.grid(row=1, column=2)

affiliation_text = StringVar()
en3 = Entry(window, textvariable=affiliation_text)
en3.grid(row=2, column=2)

email_text = StringVar()
en4 = Entry(window, textvariable=email_text)
en4.grid(row=3, column=2)

phone_text = StringVar()
en5 = Entry(window, textvariable=phone_text)
en5.grid(row=4, column=2)

#Listbox
list = Listbox(window, height=6, width=50)
list.grid(row=5, column=0, rowspan=6, columnspan=5)

#Gets item selected in listbox
def get_selected_row(event):
    global selected_tuple
    try:
        index=list.curselection()[0]
        selected_tuple = list.get(index)

        en1.delete(0, END)
        en1.insert(END, selected_tuple[1])
        en2.delete(0, END)
        en2.insert(END, selected_tuple[2])
        en3.delete(0, END)
        en3.insert(END, selected_tuple[3])
        en4.delete(0, END)
        en4.insert(END, selected_tuple[4])
        en5.delete(0, END)
        en5.insert(END, selected_tuple[5])
    except NameError:
        selected_tuple = None

list.bind('<<ListboxSelect>>', get_selected_row)

#Profile Window and Functions-------------------------------------------------------------------------------------------
def open_profile(account):
    profile = Tk()
    profile.title("Profile")
    profile.minsize(height=400, width=600)

    for rows in back.search_volunteer_by_id(account[0]):
        null, name, job, affiliation, email, phone = rows

    #Profile Labels
    plb1 = Label(profile, text="Name")
    plb1.grid(row=0, column=0, columnspan=1)

    plb2 = Label(profile, text="Job")
    plb2.grid(row=1, column=0, columnspan=1)

    plb3 = Label(profile, text="Affiliation")
    plb3.grid(row=2, column=0, columnspan=1)

    plb4 = Label(profile, text="Email")
    plb4.grid(row=3, column=0, columnspan=1)

    plb5 = Label(profile, text="Phone Number")
    plb5.grid(row=4, column=0, columnspan=1)

    #Profile Entryboxs
    p_name_text=StringVar()
    p_name_text.set(name)
    pen1 = Entry(profile, textvariable=p_name_text)
    pen1.delete(0, END)
    pen1.insert(END, name)
    pen1.grid(row=0, column=3)

    p_job_text = StringVar()
    p_job_text.set(job)
    pen2 = Entry(profile, textvariable=p_job_text)
    pen2.delete(0, END)
    pen2.insert(END, job)
    pen2.grid(row=1, column=3)

    p_affiliation_text = StringVar()
    p_affiliation_text.set(affiliation)
    pen3 = Entry(profile, textvariable=p_affiliation_text)
    pen3.delete(0, END)
    pen3.insert(END, affiliation)
    pen3.grid(row=2, column=3)

    p_email_text = StringVar()
    p_email_text.set(email)
    pen4 = Entry(profile, textvariable=p_email_text)
    pen4.delete(0, END)
    pen4.insert(END, email)
    pen4.grid(row=3, column=3)

    p_phone_text = StringVar()
    p_phone_text.set(phone)
    pen5 = Entry(profile, textvariable=p_phone_text)
    pen5.delete(0, END)
    pen5.insert(END, phone)
    pen5.grid(row=4, column=3)

    #Profile connecting functions
    def delete_command():
        back.delete_volunteer(account[0])
        view_command()

    def update_command():
        back.update_volunteer(account[0], pen1.get(), pen2.get(), pen3.get(),
                              pen4.get(), pen5.get())

    #Experience Window and Functions------------------------------------------------------------------------------------
    def open_experience_window(account):
        exp_window = Tk()
        exp_window.title(account[1] + "'s Experiences")
        exp_window.minsize(height=400, width=400)

        #Experience Labels
        elb1 = Label(exp_window, text="Title")
        elb1.grid(row=0, column=0)

        elb3 = Label(exp_window, text="Date Obtained")
        elb3.grid(row=1, column=0)

        elb4 = Label(exp_window, text="Expiration Date")
        elb4.grid(row=2, column=0)

        elb2 = Label(exp_window, text="Description")
        elb2.grid(row=3, column=0)

        #Experience Entryboxes
        title_text = StringVar()
        e_en1 = Entry(exp_window, textvariable=title_text)
        e_en1.grid(row=0, column=1)

        date_ob_text = StringVar()
        e_en2 = Entry(exp_window, textvariable=date_ob_text)
        e_en2.grid(row=1, column=1)

        ex_date_text = StringVar()
        e_en3 = Entry(exp_window, textvariable=ex_date_text)
        e_en3.grid(row=2, column=1)

        #Text Widget for Description
        desc_textbox = Text(exp_window, height=5, width=15)
        desc_textbox.grid(row=3, column=1)

        #Experience Listbox
        elist = Listbox(exp_window, height=6, width=50)
        elist.grid(row=6, column=0, rowspan=6, columnspan=5)

        #Get selected information from the experience list
        def get_selected_row_e(event):
            global e_selected_tuple
            try:
                e_index = elist.curselection()[0]
                e_selected_tuple = elist.get(e_index)

                e_en1.delete(0, END)
                e_en1.insert(END, e_selected_tuple[1])
                desc_textbox.delete(1.0, END)
                desc_textbox.insert(END, e_selected_tuple[2])
                e_en2.delete(0, END)
                e_en2.insert(END, e_selected_tuple[3])
                e_en3.delete(0, END)
                e_en3.insert(END, e_selected_tuple[4])
            except NameError:
                e_selected_tuple = None

        elist.bind('<<ListboxSelect>>', get_selected_row_e)

        #Connecting Functions
        def view_experience_command():
            elist.delete(0, END)
            for row in back.join_bridge(account[0]):
                elist.insert(END, row)

        def search_experience_command():
            elist.delete(0, END)
            for row in back.search_experiences(e_en1.get(), desc_textbox.get("1.0", "end-1c"), e_en2.get(), e_en3.get(), account[0]):
                elist.insert(END, row)

        def add_experience_command():
            back.insert_experience(e_en1.get(), desc_textbox.get("1.0", "end-1c"), e_en2.get(), e_en3.get(), account[0])
            elist.delete(0, END)
            elist.insert(END, (e_en1.get(), desc_textbox.get("1.0", "end-1c"), e_en2.get(), e_en3.get()))
            view_experience_command()

        def delete_experience_command():
            back.delete_experience(e_selected_tuple[0])
            view_experience_command()

        def update_experience_command():
            back.update_experience(account[0], e_selected_tuple[0], e_en1.get(), desc_textbox.get("1.0", "end-1c"), e_en2.get(), e_en3.get())
            view_experience_command()

        def notify_expiring_command(cert_name, expiration_date, user_email):
            emailSystem.send_Expiring_Email(cert_name, expiration_date, user_email)

        def notify_opporutiny_command(user_email):
            cert_naming_window = Tk()
            cert_naming_window.title("Name new opportunity")
            cert_naming_window.minsize(height=50, width=300)

            cert_text = StringVar()
            cen1 = Entry(cert_naming_window, textvariable=cert_text)
            cen1.grid(row=0, column=0)

            def send_opportunity_command():
                emSys.send_Opportunity_Email(cen1.get(), user_email)

            cbt1 = Button(cert_naming_window, text="Send", width=12, command=lambda: [send_opportunity_command(), cert_naming_window.destroy()])
            cbt1.grid(row=0, column=1)

            cbt2 = Button(cert_naming_window, text="Cancel", width=12, command=cert_naming_window.destroy)
            cbt2.grid(row=0, column=2)

        #Experience Buttons
        ebt1 = Button(exp_window, text="View All", width=12, command=view_experience_command)
        ebt1.grid(row=0, column=3)

        ebt2 = Button(exp_window, text="Search", width=12, command=search_experience_command)
        ebt2.grid(row=1, column=3)

        ebt3 = Button(exp_window, text="Add", width=12, command=add_experience_command)
        ebt3.grid(row=2, column=3)

        ebt4 = Button(exp_window, text="Update", width=12, command=update_experience_command)
        ebt4.grid(row=0, column=4)

        ebt5 = Button(exp_window, text="Delete", width=12, command=delete_experience_command)
        ebt5.grid(row=1, column=4)

        ebt6 = Button(exp_window, text="Close", width=12, command=exp_window.destroy)
        ebt6.grid(row=2, column=4)

        ebt7 = Button(exp_window, text="Expire Notification", width=22, command=lambda :notify_expiring_command(e_selected_tuple[1], e_selected_tuple[4], account[4]))
        ebt7.grid(row=12, column=1)

        ebt7 = Button(exp_window, text="New Opportunity Notification", width=22, command=lambda: notify_opporutiny_command(account[4]))
        ebt7.grid(row=12, column=3, columnspan=2)
    #-------------------------------------------------------------------------------------------------------------------
    #Profile Buttons
    pbt1 = Button(profile, text="Update", width=12, command=update_command)
    pbt1.grid(row=0, column=4)

    pbt2 = Button(profile, text="Edit Experience", width=12, command=lambda :open_experience_window(account))
    pbt2.grid(row=1, column=4)

    pbt4 = Button(profile, text="Delete", width=12, command=lambda: [delete_command(), profile.destroy()])
    pbt4.grid(row=2, column=4)

    pbt5 = Button(profile, text="Close", width=12, command=profile.destroy)
    pbt5.grid(row=3, column=4)

#-----------------------------------------------------------------------------------------------------------------------

#Backend Connecting Methods
def view_command():
    list.delete(0, END)
    for row in back.view_volunteer():
        list.insert(END, row)

def search_command():
    list.delete(0, END)
    for row in back.search_volunteer(name_text.get(), job_text.get(), affiliation_text.get(), email_text.get(), phone_text.get()):
        list.insert(END, row)

def add_command():
    back.insert_volunteer(name_text.get(), job_text.get(), affiliation_text.get(), email_text.get(), phone_text.get())
    list.delete(0, END)
    list.insert(END, (name_text.get(), job_text.get(), affiliation_text.get(), email_text.get(), phone_text.get()))

#Buttons
bt1 = Button(window, text="View All", width=12, command=view_command)
bt1.grid(row=0, column=3)

bt2 = Button(window, text="Search", width=12, command=search_command)
bt2.grid(row=1, column=3)

bt3 = Button(window, text="Add", width=12, command= lambda: [add_command(), search_command()])
bt3.grid(row=2, column=3)

bt4= Button(window, text="View Profile", width=12, command= lambda: open_profile(selected_tuple))
bt4.grid(row=3, column=3)

bt5 = Button(window, text="Close", width=12, command=window.destroy)
bt5.grid(row=4, column=3)

window.mainloop()
