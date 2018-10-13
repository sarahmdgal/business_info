##!/usr/bin/python3
import tkinter as tk
from tkinter import *
import tkinter as ttk
import os
from BusinessCustomer import Clientinfo
import pymysql

master = tk.Tk()
master.geometry("10000x800+0+0")
master.title("Business Customer Information Screen (Python 3.7 and MySQL 5.7)")
master.configure(background='#ff8c8c')
small_font = ('Verdana',10)


def add_new_customer():
    global PersonID
    global salut
    global firstname
    global mid_init
    global lastname
    global suffix
    global title
    global company_name
    global department
    global address1
    global address2
    global suite_no
    global city
    global state
    global postal_code
    global zip_code
    global mobile_phone
    global office_phone
    global fax_phone
    global home_phone
    global office_email
    global home_email
    global gender
    global age
    global notes

    

##    Label(master, text="Person ID:").grid(row=1, column=0, sticky=E)
##    PersonID = Entry(master, width=5, font=small_font)
##    PersonID.grid(row=1, column=1, sticky=W)

    Label(master, text="Salutation:").grid(row=1, column=0, sticky=E)
    salut = Entry(master, width=5, font=small_font)
    salut.grid(row=1, column=1, sticky=W)
    
    Label(master, text="First Name:").grid(row=1, column=2, sticky=E)
    firstname = Entry(master, width=25, font=small_font)
    firstname.grid(row=1, column=3, sticky=W)

    Label(master, text="Mid Init:").grid(row=1, column=4, sticky=E)
    mid_init = Entry(master, width=5, font=small_font)
    mid_init.grid(row=1, column=5, sticky=W)

    Label(master, text="Last Name:").grid(row=1, column=6, sticky=E)
    lastname = Entry(master, width=15, font=small_font)
    lastname.grid(row=1, column=7, sticky=W)

  
    Label(master, text="Suffix:").grid(row=1, column=8, sticky=E)
    suffix = Entry(master, width=5, font=small_font)
    suffix.grid(row=1, column=9, sticky=W)

    
    Label(master, text="Title:").grid(row=2, column=0, sticky=E)
    title = Entry(master, width=30, font=small_font)
    title.grid(row=2, column=1, sticky=W)

    
    Label(master, text="Company Name:").grid(row=3, column=0, sticky=E)
    company_name = Entry(master, width=30, font=small_font)
    company_name.grid(row=3, column=1, sticky=W)

   
    Label(master, text="Department:").grid(row=3, column=2, sticky=E)
    department = Entry(master, width=25, font=small_font)
    department.grid(row=3, column=3, sticky=W)

    
    Label(master, text="Address1:").grid(row=4, column=0, sticky=E)
    address1 = Entry(master, width=30, font=small_font)
    address1.grid(row=4, column=1, sticky=W)

    
    Label(master, text="Address2:").grid(row=4, column=2, sticky=E)
    address2 = Entry(master, width=30, font=small_font)
    address2.grid(row=4, column=3, sticky=W)
    
    Label(master, text="Suite No:").grid(row=4, column=4, sticky=E)
    suite_no = Entry(master, width=15, font=small_font)
    suite_no.grid(row=4, column=5, sticky=W)

    
    Label(master, text="City:").grid(row=5, column=0, sticky=E)
    city = Entry(master, width=25, font=small_font)
    city.grid(row=5, column=1, sticky=W)

    
    Label(master, text="State:").grid(row=5, column=2, sticky=E)
    state = Entry(master, width=5, font=small_font)
    state.grid(row=5, column=3, sticky=W)

    
    Label(master, text="Postal Code:").grid(row=5, column=4, sticky=E)
    postal_code = Entry(master, width=15, font=small_font)
    postal_code.grid(row=5, column=5, sticky=W)

    
    Label(master, text="Zip Code:").grid(row=5, column=6, sticky=E)
    zip_code = Entry(master, width=15, font=small_font)
    zip_code.grid(row=5, column=7, sticky=W)

   
    Label(master, text="Mobile Phone:").grid(row=6, column=0, sticky=E)
    mobile_phone = Entry(master, width=15, font=small_font)
    mobile_phone.grid(row=6, column=1, sticky=W)
    
    Label(master, text="Office Phone:").grid(row=6, column=2, sticky=E)
    office_phone = Entry(master, width=15, font=small_font)
    office_phone.grid(row=6, column=3, sticky=W)
    
    Label(master, text="Home Phone:").grid(row=6, column=4, sticky=E)
    home_phone = Entry(master, width=15, font=small_font)
    home_phone.grid(row=6, column=5, sticky=W)

    Label(master, text="Fax Phone:").grid(row=6, column=6, sticky=E)
    fax_phone = Entry(master, width=15, font=small_font)
    fax_phone.grid(row=6, column=7, sticky=W)
    
    Label(master, text="Office Email:").grid(row=7, column=0, sticky=E)
    office_email = Entry(master, width=30, font=small_font)
    office_email.grid(row=7, column=1, sticky=W)

    
    Label(master, text="Home Email:").grid(row=7, column=2, sticky=E)
    home_email = Entry(master, width=30, font=small_font)
    home_email.grid(row=7, column=3, sticky=W)

    
    Label(master, text="Gender:").grid(row=8, column=0, sticky=E)
    gender = Entry(master, width=7, font=small_font)
    gender.grid(row=8, column=1, sticky=W)

    
    Label(master, text="Age:").grid(row=8, column=2, sticky=E)
    age = Entry(master, width=5, font=small_font)
    age.grid(row=8, column=3, sticky=W)

    
    Label(master, text="Notes:").grid(row=9, column=0, sticky=E)
    notes = Entry(master, width=30, font=small_font)
    notes.grid(row=9, column=1, sticky=W)
    
##    PersonID.delete(0, END)
    salut.delete(0,END)
    firstname.delete(0,END)
    mid_init.delete(0,END)
    lastname.delete(0,END)
    suffix.delete(0,END)
    title.delete(0,END)
    company_name.delete(0,END)
    department.delete(0,END)
    address1.delete(0,END)
    address2.delete(0,END)
    suite_no.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    postal_code.delete(0,END)
    zip_code.delete(0,END)
    mobile_phone.delete(0,END)
    office_phone.delete(0,END)
    home_phone.delete(0,END)
    fax_phone.delete(0,END)
    office_email.delete(0,END)
    home_email.delete(0,END)
    gender.delete(0,END)
    age.delete(0,END)
    notes.delete(0,END)

    
def insert_data():
    salut1 = salut.get()
    firstname1 = firstname.get()
    mid_init1 = mid_init.get()    
    lastname1 = lastname.get()    
    suffix1 = suffix.get()    
    title1 = title.get()    
    company_name1 = company_name.get()    
    department1 = department.get()    
    address11 = address1.get()    
    address21 = address2.get()    
    suite_no1 = suite_no.get()    
    city1 = city.get()    
    state1 = state.get()    
    postal_code1 = postal_code.get()
    zip_code1 = zip_code.get()
    mobile_phone1 = mobile_phone.get()    
    office_phone1 = office_phone.get()
    home_phone1 = home_phone.get()
    fax_phone1 = fax_phone.get()
    office_email1 = office_email.get()    
    home_email1 = home_email.get()    
    gender1 = gender.get()    
    age1 = age.get()    
    notes1 = notes.get()    
 
    print(salut1, firstname1, mid_init1, lastname1, suffix1, title1, company_name1, 
                 department1, address11, address21, suite_no1, city1, state1, postal_code1, zip_code1, mobile_phone1, office_phone1,
                 home_phone1, fax_phone1, office_email1, home_email1, gender1, age1, notes1)



    conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
    with conn:
       c = conn.cursor()
       sql =  """
              INSERT INTO clientinfo(salut, firstname, mid_init, lastname, suffix, title, company_name,  
                 department, address1, address2, suite_no, city, state, postal_code, zip_code, mobile_phone,  
                 office_phone, home_phone, fax_phone, office_email, home_email, gender, age, notes)   
                 VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)   
              """
       c.execute(sql, (salut1, firstname1, mid_init1, lastname1, suffix1, title1, company_name1, department1,
                       address11, address21, suite_no1, city1, state1, postal_code1, zip_code1, mobile_phone1,
                       office_phone1, home_phone1, fax_phone1, office_email1, home_email1, gender1, age1, notes1))


    conn.commit()   
    conn.close()
    get_customer_record()
    
def update_record():
    PersonID1 = int(PersonID.get())
    print(PersonID)
    salut1 = salut.get()
    firstname1 = firstname.get()
    mid_init1 = mid_init.get()    
    lastname1 = lastname.get()    
    suffix1 = suffix.get()    
    title1 = title.get()    
    company_name1 = company_name.get()    
    department1 = department.get()    
    address11 = address1.get()    
    address21 = address2.get()    
    suite_no1 = suite_no.get()    
    city1 = city.get()    
    state1 = state.get()    
    postal_code1 = postal_code.get()
    zip_code1 = zip_code.get()
    mobile_phone1 = mobile_phone.get()    
    office_phone1 = office_phone.get()    
    home_phone1 = home_phone.get()
    fax_phone1 = fax_phone.get()
    office_email1 = office_email.get()    
    home_email1 = home_email.get()    
    gender1 = gender.get()    
    age1 = age.get()    
    notes1 = notes.get()    
 
    conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
    with conn:
       c = conn.cursor()
    c.execute('UPDATE clientinfo SET salut = %s,  firstname = %s,  mid_init = %s,  lastname = %s,  suffix = %s,  title = %s,  company_name = %s,  ' 
             'department = %s,  address1 = %s,  address2 = %s,  suite_no = %s,  city = %s,  state = %s,  postal_code = %s,  zip_code = %s,  mobile_phone = %s,  ' 
             'office_phone = %s,  home_phone = %s,  fax_phone = %s, office_email = %s,  home_email = %s,  gender = %s,  age = %s,  notes  = %s WHERE PersonID = %s', (salut1, firstname1, mid_init1, lastname1, 
              suffix1, title1, company_name1, department1, address11, address21, suite_no1, city1, state1, postal_code1, zip_code1, 
              mobile_phone1, office_phone1, home_phone1, fax_phone1, office_email1, home_email1, gender1, age1, notes1, PersonID1)) 

    conn.commit()
    conn.close()

    salut.delete(0,END)
    firstname.delete(0,END)
    mid_init.delete(0,END)
    lastname.delete(0,END)
    suffix.delete(0,END)
    title.delete(0,END)
    company_name.delete(0,END)
    department.delete(0,END)
    address1.delete(0,END)
    address2.delete(0,END)
    suite_no.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    postal_code.delete(0,END)
    zip_code.delete(0,END)
    mobile_phone.delete(0,END)
    office_phone.delete(0,END)
    home_phone.delete(0,END)
    fax_phone.delete(0,END)
    office_email.delete(0,END)
    home_email.delete(0,END)
    gender.delete(0,END)
    age.delete(0,END)
    notes.delete(0,END)
    get_first_record()
    
def get_customer_record():
    global PersonID
    global salut
    global firstname
    global mid_init
    global lastname
    global suffix
    global title
    global company_name
    global department
    global address1
    global address2
    global suite_no
    global city
    global state
    global postal_code
    global zip_code
    global mobile_phone
    global office_phone
    global home_phone
    global fax_phone
    global office_email
    global home_email
    global gender
    global age
    global notes
    global rowid
    global fname
    global lname


    conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM clientinfo WHERE PersonID = 1;")        
        list_load = c.fetchall()
    conn.commit() 
    for row in list_load:
        PersonID=row[0]
        salut=row[1]
        firstname=row[2]
        mid_init=row[3]
        lastname=row[4]
        suffix=row[5]
        title=row[6]
        company_name=row[7]
        department=row[8]
        address1=row[9]
        address2=row[10]
        suite_no=row[11]
        city=row[12]
        state=row[13]
        postal_code=row[14]
        zip_code=row[15]
        mobile_phone=row[16]
        office_phone=row[17]
        home_phone=row[18]
        fax_phone=row[19]
        office_email=row[20]
        home_email=row[21]
        gender=row[22]
        age=row[23]
        notes=row[24]

    Label(master, text="Person ID:").grid(row=0, column=0, sticky=E)
    PersonID = Entry(master, width=5, font=small_font)
    PersonID.grid(row=0, column=1, sticky=W)    

    Label(master, text="Salutation:").grid(row=1, column=0, sticky=E)
    salut = Entry(master, width=5, font=small_font)
    salut.grid(row=1, column=1, sticky=W)
    
    Label(master, text="First Name:").grid(row=1, column=2, sticky=E)
    firstname = Entry(master, width=25, font=small_font)
    firstname.grid(row=1, column=3, sticky=W)

    Label(master, text="Mid Init:").grid(row=1, column=4, sticky=E)
    mid_init = Entry(master, width=5, font=small_font)
    mid_init.grid(row=1, column=5, sticky=W)

    Label(master, text="Last Name:").grid(row=1, column=6, sticky=E)
    lastname = Entry(master, width=15, font=small_font)
    lastname.grid(row=1, column=7, sticky=W)

  
    Label(master, text="Suffix:").grid(row=1, column=8, sticky=E)
    suffix = Entry(master, width=5, font=small_font)
    suffix.grid(row=1, column=9, sticky=W)

    
    Label(master, text="Title:").grid(row=2, column=0, sticky=E)
    title = Entry(master, width=30, font=small_font)
    title.grid(row=2, column=1, sticky=W)

    
    Label(master, text="Company Name:").grid(row=3, column=0, sticky=E)
    company_name = Entry(master, width=30, font=small_font)
    company_name.grid(row=3, column=1, sticky=W)

   
    Label(master, text="Department:").grid(row=3, column=2, sticky=E)
    department = Entry(master, width=25, font=small_font)
    department.grid(row=3, column=3, sticky=W)

    
    Label(master, text="Address1:").grid(row=4, column=0, sticky=E)
    address1 = Entry(master, width=30, font=small_font)
    address1.grid(row=4, column=1, sticky=W)

    
    Label(master, text="Address2:").grid(row=4, column=2, sticky=E)
    address2 = Entry(master, width=30, font=small_font)
    address2.grid(row=4, column=3, sticky=W)
    
    Label(master, text="Suite No:").grid(row=4, column=4, sticky=E)
    suite_no = Entry(master, width=15, font=small_font)
    suite_no.grid(row=4, column=5, sticky=W)

    
    Label(master, text="City:").grid(row=5, column=0, sticky=E)
    city = Entry(master, width=25, font=small_font)
    city.grid(row=5, column=1, sticky=W)

    
    Label(master, text="State:").grid(row=5, column=2, sticky=E)
    state = Entry(master, width=5, font=small_font)
    state.grid(row=5, column=3, sticky=W)

    
    Label(master, text="Postal Code:").grid(row=5, column=4, sticky=E)
    postal_code = Entry(master, width=15, font=small_font)
    postal_code.grid(row=5, column=5, sticky=W)

    
    Label(master, text="Zip Code:").grid(row=5, column=6, sticky=E)
    zip_code = Entry(master, width=15, font=small_font)
    zip_code.grid(row=5, column=7, sticky=W)

   
    Label(master, text="Mobile Phone:").grid(row=6, column=0, sticky=E)
    mobile_phone = Entry(master, width=15, font=small_font)
    mobile_phone.grid(row=6, column=1, sticky=W)
    
    Label(master, text="Office Phone:").grid(row=6, column=2, sticky=E)
    office_phone = Entry(master, width=15, font=small_font)
    office_phone.grid(row=6, column=3, sticky=W)
    
    Label(master, text="Home Phone:").grid(row=6, column=4, sticky=E)
    home_phone = Entry(master, width=15, font=small_font)
    home_phone.grid(row=6, column=5, sticky=W)

    Label(master, text="Fax Phone:").grid(row=6, column=6, sticky=E)
    fax_phone = Entry(master, width=15, font=small_font)
    fax_phone.grid(row=6, column=7, sticky=W)

    
    Label(master, text="Office Email:").grid(row=7, column=0, sticky=E)
    office_email = Entry(master, width=30, font=small_font)
    office_email.grid(row=7, column=1, sticky=W)

    
    Label(master, text="Home Email:").grid(row=7, column=2, sticky=E)
    home_email = Entry(master, width=30, font=small_font)
    home_email.grid(row=7, column=3, sticky=W)

    
    Label(master, text="Gender:").grid(row=8, column=0, sticky=E)
    gender = Entry(master, width=7, font=small_font)
    gender.grid(row=8, column=1, sticky=W)

    
    Label(master, text="Age:").grid(row=8, column=2, sticky=E)
    age = Entry(master, width=5, font=small_font)
    age.grid(row=8, column=3, sticky=W)

    
    Label(master, text="Notes:").grid(row=9, column=0, sticky=E)
    notes = Entry(master, width=30, font=small_font)
    notes.grid(row=9, column=1, sticky=W)

    PersonID.insert(END, row[0])
    salut.insert(END, row[1])
    firstname.insert(END, row[2])
    mid_init.insert(END, row[3])
    lastname.insert(END, row[4])
    suffix.insert(END, row[5])
    title.insert(END, row[6])
    company_name.insert(END, row[7])
    department.insert(END, row[8])
    address1.insert(END, row[9])
    address2.insert(END, row[10])
    suite_no.insert(END, row[11])
    city.insert(END, row[12])
    state.insert(END, row[13])
    postal_code.insert(END, row[14])
    zip_code.insert(END, row[15])
    mobile_phone.insert(END, row[16])
    office_phone.insert(END, row[17])
    home_phone.insert(END, row[18])
    fax_phone.insert(END, row[19])
    office_email.insert(END, row[20])
    home_email.insert(END, row[21])
    gender.insert(END, row[22])
    age.insert(END, row[23])
    notes.insert(END, row[24])


##def clear_fields():
##   PersonID.delete(0, END)
##   salut.delete(0,END)
##   firstname.delete(0,END)
##   mid_init.delete(0,END)
##   lastname.delete(0,END)
##   suffix.delete(0,END)
##   title.delete(0,END)
##   company_name.delete(0,END)
##   department.delete(0,END)
##   address1.delete(0,END)
##   address2.delete(0,END)
##   suite_no.delete(0,END)
##   city.delete(0,END)
##   state.delete(0,END)
##   postal_code.delete(0,END)
##   zip_code.delete(0,END)
##   mobile_phone.delete(0,END)
##   office_phone.delete(0,END)
##   home_phone.delete(0,END)
##   office_email.delete(0,END)
##   home_email.delete(0,END)
##   gender.delete(0,END)
##   age.delete(0,END)
##   notes.delete(0,END)

def get_next_record():
    global PersonID
    global salut
    global firstname
    global mid_init
    global lastname
    global suffix
    global title
    global company_name
    global department
    global address1
    global address2
    global suite_no
    global city
    global state
    global postal_code
    global zip_code
    global mobile_phone
    global office_phone
    global home_phone
    global fax_phone
    global office_email
    global home_email
    global gender
    global age
    global notes
    
    

    next_PersonID = int(PersonID.get()) + 1
   
    PersonID.delete(0, END)
    salut.delete(0,END)
    firstname.delete(0,END)
    mid_init.delete(0,END)
    lastname.delete(0,END)
    suffix.delete(0,END)
    title.delete(0,END)
    company_name.delete(0,END)
    department.delete(0,END)
    address1.delete(0,END)
    address2.delete(0,END)
    suite_no.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    postal_code.delete(0,END)
    zip_code.delete(0,END)
    mobile_phone.delete(0,END)
    office_phone.delete(0,END)
    home_phone.delete(0,END)
    fax_phone.delete(0,END)
    office_email.delete(0,END)
    home_email.delete(0,END)
    gender.delete(0,END)
    age.delete(0,END)
    notes.delete(0,END)
    
    conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
    with conn:
        c = conn.cursor()
        c.execute( "SELECT * FROM clientinfo WHERE PersonID LIKE %s", [next_PersonID] )
        list_load = c.fetchall()


    # prepare a cursor object using cursor() method
    c = conn.cursor()

    for row in list_load:
        PersonID=row[0]
        salut=row[1]
        firstname=row[2]
        mid_init=row[3]
        lastname=row[4]
        suffix=row[5]
        title=row[6]
        company_name=row[7]
        department=row[8]
        address1=row[9]
        address2=row[10]
        suite_no=row[11]
        city=row[12]
        state=row[13]
        postal_code=row[14]
        zip_code=row[15]
        mobile_phone=row[16]
        office_phone=row[17]
        home_phone=row[18]
        fax_phone=row[19]
        office_email=row[20]
        home_email=row[21]
        gender=row[22]
        age=row[23]
        notes=row[24]
    conn.commit()
    conn.close()

    Label(master, text="Person ID:").grid(row=0, column=0, sticky=E)
    PersonID = Entry(master, width=5, font=small_font)
    PersonID.grid(row=0, column=1, sticky=W)
    
    Label(master, text="Salutation:").grid(row=1, column=0, sticky=E)
    salut = Entry(master, width=5, font=small_font)
    salut.grid(row=1, column=1, sticky=W)
    
    Label(master, text="First Name:").grid(row=1, column=2, sticky=E)
    firstname = Entry(master, width=25, font=small_font)
    firstname.grid(row=1, column=3, sticky=W)

    Label(master, text="Mid Init:").grid(row=1, column=4, sticky=E)
    mid_init = Entry(master, width=5, font=small_font)
    mid_init.grid(row=1, column=5, sticky=W)

    Label(master, text="Last Name:").grid(row=1, column=6, sticky=E)
    lastname = Entry(master, width=15, font=small_font)
    lastname.grid(row=1, column=7, sticky=W)

  
    Label(master, text="Suffix:").grid(row=1, column=8, sticky=E)
    suffix = Entry(master, width=5, font=small_font)
    suffix.grid(row=1, column=9, sticky=W)

    
    Label(master, text="Title:").grid(row=2, column=0, sticky=E)
    title = Entry(master, width=30, font=small_font)
    title.grid(row=2, column=1, sticky=W)

    
    Label(master, text="Company Name:").grid(row=3, column=0, sticky=E)
    company_name = Entry(master, width=30, font=small_font)
    company_name.grid(row=3, column=1, sticky=W)

   
    Label(master, text="Department:").grid(row=3, column=2, sticky=E)
    department = Entry(master, width=25, font=small_font)
    department.grid(row=3, column=3, sticky=W)

    
    Label(master, text="Address1:").grid(row=4, column=0, sticky=E)
    address1 = Entry(master, width=30, font=small_font)
    address1.grid(row=4, column=1, sticky=W)

    
    Label(master, text="Address2:").grid(row=4, column=2, sticky=E)
    address2 = Entry(master, width=30, font=small_font)
    address2.grid(row=4, column=3, sticky=W)
    
    Label(master, text="Suite No:").grid(row=4, column=4, sticky=E)
    suite_no = Entry(master, width=15, font=small_font)
    suite_no.grid(row=4, column=5, sticky=W)

    
    Label(master, text="City:").grid(row=5, column=0, sticky=E)
    city = Entry(master, width=25, font=small_font)
    city.grid(row=5, column=1, sticky=W)

    
    Label(master, text="State:").grid(row=5, column=2, sticky=E)
    state = Entry(master, width=5, font=small_font)
    state.grid(row=5, column=3, sticky=W)

    
    Label(master, text="Postal Code:").grid(row=5, column=4, sticky=E)
    postal_code = Entry(master, width=15, font=small_font)
    postal_code.grid(row=5, column=5, sticky=W)

    
    Label(master, text="Zip Code:").grid(row=5, column=6, sticky=E)
    zip_code = Entry(master, width=15, font=small_font)
    zip_code.grid(row=5, column=7, sticky=W)

   
    Label(master, text="Mobile Phone:").grid(row=6, column=0, sticky=E)
    mobile_phone = Entry(master, width=15, font=small_font)
    mobile_phone.grid(row=6, column=1, sticky=W)
    
    Label(master, text="Office Phone:").grid(row=6, column=2, sticky=E)
    office_phone = Entry(master, width=15, font=small_font)
    office_phone.grid(row=6, column=3, sticky=W)
    

    Label(master, text="Home Phone:").grid(row=6, column=4, sticky=E)
    home_phone = Entry(master, width=15, font=small_font)
    home_phone.grid(row=6, column=5, sticky=W)

    
    Label(master, text="Fax Phone:").grid(row=6, column=6, sticky=E)
    fax_phone = Entry(master, width=15, font=small_font)
    fax_phone.grid(row=6, column=7, sticky=W) 
    
    Label(master, text="Office Email:").grid(row=7, column=0, sticky=E)
    office_email = Entry(master, width=30, font=small_font)
    office_email.grid(row=7, column=1, sticky=W)

    
    Label(master, text="Home Email:").grid(row=7, column=2, sticky=E)
    home_email = Entry(master, width=30, font=small_font)
    home_email.grid(row=7, column=3, sticky=W)

    
    Label(master, text="Gender:").grid(row=8, column=0, sticky=E)
    gender = Entry(master, width=7, font=small_font)
    gender.grid(row=8, column=1, sticky=W)

    
    Label(master, text="Age:").grid(row=8, column=2, sticky=E)
    age = Entry(master, width=5, font=small_font)
    age.grid(row=8, column=3, sticky=W)

    
    Label(master, text="Notes:").grid(row=9, column=0, sticky=E)
    notes = Entry(master, width=30, font=small_font)
    notes.grid(row=9, column=1, sticky=W)

    
    PersonID.insert(END, row[0])
    salut.insert(END, row[1])
    firstname.insert(END, row[2])
    mid_init.insert(END, row[3])
    lastname.insert(END, row[4])
    suffix.insert(END, row[5])
    title.insert(END, row[6])
    company_name.insert(END, row[7])
    department.insert(END, row[8])
    address1.insert(END, row[9])
    address2.insert(END, row[10])
    suite_no.insert(END, row[11])
    city.insert(END, row[12])
    state.insert(END, row[13])
    postal_code.insert(END, row[14])
    zip_code.insert(END, row[15])
    mobile_phone.insert(END, row[16])
    office_phone.insert(END, row[17])
    home_phone.insert(END, row[18])
    fax_phone.insert(END, row[19])
    office_email.insert(END, row[20])
    home_email.insert(END, row[21])
    gender.insert(END, row[22])
    age.insert(END, row[23])
    notes.insert(END, row[24])


def get_previous_record():
    global PersonID
    global salut
    global firstname
    global mid_init
    global lastname
    global suffix
    global title
    global company_name
    global department
    global address1
    global address2
    global suite_no
    global city
    global state
    global postal_code
    global zip_code
    global mobile_phone
    global office_phone
    global home_phone
    global fax_phone
    global office_email
    global home_email
    global gender
    global age
    global notes


    
    prev_PersonID = int(PersonID.get()) - 1
    if prev_PersonID < 1:
        get_first_record()
    else:    
        PersonID.delete(0, END)
        salut.delete(0,END)
        firstname.delete(0,END)
        mid_init.delete(0,END)
        lastname.delete(0,END)
        suffix.delete(0,END)
        title.delete(0,END)
        company_name.delete(0,END)
        department.delete(0,END)
        address1.delete(0,END)
        address2.delete(0,END)
        suite_no.delete(0,END)
        city.delete(0,END)
        state.delete(0,END)
        postal_code.delete(0,END)
        zip_code.delete(0,END)
        mobile_phone.delete(0,END)
        office_phone.delete(0,END)
        home_phone.delete(0,END)
        fax_phone.delete(0,END)
        office_email.delete(0,END)
        home_email.delete(0,END)
        gender.delete(0,END)
        age.delete(0,END)
        notes.delete(0,END)
       
        conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
        with conn:
            c = conn.cursor()
            c.execute( "SELECT * FROM clientinfo WHERE PersonID LIKE %s", [prev_PersonID] )
            list_load = c.fetchall()
        
        for row in list_load:
            PersonID=row[0]
            salut=row[1]
            firstname=row[2]
            mid_init=row[3]
            lastname=row[4]
            suffix=row[5]
            title=row[6]
            company_name=row[7]
            department=row[8]
            address1=row[9]
            address2=row[10]
            suite_no=row[11]
            city=row[12]
            state=row[13]
            postal_code=row[14]
            zip_code=row[15]
            mobile_phone=row[16]
            office_phone=row[17]
            home_phone=row[18]
            fax_phone=row[19]
            office_email=row[20]
            home_email=row[21]
            gender=row[22]
            age=row[23]
            notes=row[24]
        conn.commit()
        conn.close()
        
        Label(master, text="Person ID:").grid(row=0, column=0, sticky=E)
        PersonID = Entry(master, width=5, font=small_font)
        PersonID.grid(row=0, column=1, sticky=W)
        
        Label(master, text="Salutation:").grid(row=1, column=0, sticky=E)
        salut = Entry(master, width=5, font=small_font)
        salut.grid(row=1, column=1, sticky=W)
        
        Label(master, text="First Name:").grid(row=1, column=2, sticky=E)
        firstname = Entry(master, width=25, font=small_font)
        firstname.grid(row=1, column=3, sticky=W)

        Label(master, text="Mid Init:").grid(row=1, column=4, sticky=E)
        mid_init = Entry(master, width=5, font=small_font)
        mid_init.grid(row=1, column=5, sticky=W)

        Label(master, text="Last Name:").grid(row=1, column=6, sticky=E)
        lastname = Entry(master, width=15, font=small_font)
        lastname.grid(row=1, column=7, sticky=W)

      
        Label(master, text="Suffix:").grid(row=1, column=8, sticky=E)
        suffix = Entry(master, width=5, font=small_font)
        suffix.grid(row=1, column=9, sticky=W)

        
        Label(master, text="Title:").grid(row=2, column=0, sticky=E)
        title = Entry(master, width=30, font=small_font)
        title.grid(row=2, column=1, sticky=W)

        
        Label(master, text="Company Name:").grid(row=3, column=0, sticky=E)
        company_name = Entry(master, width=30, font=small_font)
        company_name.grid(row=3, column=1, sticky=W)

       
        Label(master, text="Department:").grid(row=3, column=2, sticky=E)
        department = Entry(master, width=25, font=small_font)
        department.grid(row=3, column=3, sticky=W)

        
        Label(master, text="Address1:").grid(row=4, column=0, sticky=E)
        address1 = Entry(master, width=30, font=small_font)
        address1.grid(row=4, column=1, sticky=W)

        
        Label(master, text="Address2:").grid(row=4, column=2, sticky=E)
        address2 = Entry(master, width=30, font=small_font)
        address2.grid(row=4, column=3, sticky=W)
        
        Label(master, text="Suite No:").grid(row=4, column=4, sticky=E)
        suite_no = Entry(master, width=15, font=small_font)
        suite_no.grid(row=4, column=5, sticky=W)

        
        Label(master, text="City:").grid(row=5, column=0, sticky=E)
        city = Entry(master, width=25, font=small_font)
        city.grid(row=5, column=1, sticky=W)

        
        Label(master, text="State:").grid(row=5, column=2, sticky=E)
        state = Entry(master, width=5, font=small_font)
        state.grid(row=5, column=3, sticky=W)

        
        Label(master, text="Postal Code:").grid(row=5, column=4, sticky=E)
        postal_code = Entry(master, width=15, font=small_font)
        postal_code.grid(row=5, column=5, sticky=W)

        
        Label(master, text="Zip Code:").grid(row=5, column=6, sticky=E)
        zip_code = Entry(master, width=15, font=small_font)
        zip_code.grid(row=5, column=7, sticky=W)

       
        Label(master, text="Mobile Phone:").grid(row=6, column=0, sticky=E)
        mobile_phone = Entry(master, width=15, font=small_font)
        mobile_phone.grid(row=6, column=1, sticky=W)
        
        Label(master, text="Office Phone:").grid(row=6, column=2, sticky=E)
        office_phone = Entry(master, width=15, font=small_font)
        office_phone.grid(row=6, column=3, sticky=W)
        
        Label(master, text="Home Phone:").grid(row=6, column=4, sticky=E)
        home_phone = Entry(master, width=15, font=small_font)
        home_phone.grid(row=6, column=5, sticky=W)


        Label(master, text="Fax Phone:").grid(row=6, column=6, sticky=E)
        fax_phone = Entry(master, width=15, font=small_font)
        fax_phone.grid(row=6, column=7, sticky=W)
        
        
        Label(master, text="Office Email:").grid(row=7, column=0, sticky=E)
        office_email = Entry(master, width=30, font=small_font)
        office_email.grid(row=7, column=1, sticky=W)

        
        Label(master, text="Home Email:").grid(row=7, column=2, sticky=E)
        home_email = Entry(master, width=30, font=small_font)
        home_email.grid(row=7, column=3, sticky=W)

        
        Label(master, text="Gender:").grid(row=8, column=0, sticky=E)
        gender = Entry(master, width=7, font=small_font)
        gender.grid(row=8, column=1, sticky=W)

        
        Label(master, text="Age:").grid(row=8, column=2, sticky=E)
        age = Entry(master, width=5, font=small_font)
        age.grid(row=8, column=3, sticky=W)

        
        Label(master, text="Notes:").grid(row=9, column=0, sticky=E)
        notes = Entry(master, width=30, font=small_font)
        notes.grid(row=9, column=1, sticky=W)

        PersonID.insert(END, row[0])
        salut.insert(END, row[1])
        firstname.insert(END, row[2])
        mid_init.insert(END, row[3])
        lastname.insert(END, row[4])
        suffix.insert(END, row[5])
        title.insert(END, row[6])
        company_name.insert(END, row[7])
        department.insert(END, row[8])
        address1.insert(END, row[9])
        address2.insert(END, row[10])
        suite_no.insert(END, row[11])
        city.insert(END, row[12])
        state.insert(END, row[13])
        postal_code.insert(END, row[14])
        zip_code.insert(END, row[15])
        mobile_phone.insert(END, row[16])
        office_phone.insert(END, row[17])
        home_phone.insert(END, row[18])
        fax_phone.insert(END, row[19])
        office_email.insert(END, row[20])
        home_email.insert(END, row[21])
        gender.insert(END, row[22])
        age.insert(END, row[23])
        notes.insert(END, row[24])

    
def get_first_record():
    global PersonID
    global salut
    global firstname
    global mid_init
    global lastname
    global suffix
    global title
    global company_name
    global department
    global address1
    global address2
    global suite_no
    global city
    global state
    global postal_code
    global zip_code
    global mobile_phone
    global office_phone
    global home_phone
    global fax_phone
    global office_email
    global home_email
    global gender
    global age
    global notes
    global rowid
    global fname
    global lname
    
##    PersonID.delete(0, END)
##    salut.delete(0,END)
##    firstname.delete(0,END)
##    mid_init.delete(0,END)
##    lastname.delete(0,END)
##    suffix.delete(0,END)
##    title.delete(0,END)
##    company_name.delete(0,END)
##    department.delete(0,END)
##    address1.delete(0,END)
##    address2.delete(0,END)
##    suite_no.delete(0,END)
##    city.delete(0,END)
##    state.delete(0,END)
##    postal_code.delete(0,END)
##    zip_code.delete(0,END)
##    mobile_phone.delete(0,END)
##    office_phone.delete(0,END)
##    home_phone.delete(0,END)
##    fax_phone.delete(0,END)
##    office_email.delete(0,END)
##    home_email.delete(0,END)
##    gender.delete(0,END)
##    age.delete(0,END)
##    notes.delete(0,END)

    
    conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM clientinfo WHERE PersonID = (SELECT min(PersonID) from clientinfo)")
        list_load = c.fetchall()
        
    for row in list_load:
        PersonID=row[0]
        salut=row[1]
        firstname=row[2]
        mid_init=row[3]
        lastname=row[4]
        suffix=row[5]
        title=row[6]
        company_name=row[7]
        department=row[8]
        address1=row[9]
        address2=row[10]
        suite_no=row[11]
        city=row[12]
        state=row[13]
        postal_code=row[14]
        zip_code=row[15]
        mobile_phone=row[16]
        office_phone=row[17]
        home_phone=row[18]
        fax_phone=row[19]
        office_email=row[20]
        home_email=row[21]
        gender=row[22]
        age=row[23]
        notes=row[24]
    conn.commit()
    conn.close()

    Label(master, text="Person ID:").grid(row=0, column=0, sticky=E)
    PersonID = Entry(master, width=5, font=small_font)
    PersonID.grid(row=0, column=1, sticky=W)  

    Label(master, text="Salutation:").grid(row=1, column=0, sticky=E)
    salut = Entry(master, width=5, font=small_font)
    salut.grid(row=1, column=1, sticky=W)
    
    Label(master, text="First Name:").grid(row=1, column=2, sticky=E)
    firstname = Entry(master, width=25, font=small_font)
    firstname.grid(row=1, column=3, sticky=W)

    Label(master, text="Mid Init:").grid(row=1, column=4, sticky=E)
    mid_init = Entry(master, width=5, font=small_font)
    mid_init.grid(row=1, column=5, sticky=W)

    Label(master, text="Last Name:").grid(row=1, column=6, sticky=E)
    lastname = Entry(master, width=15, font=small_font)
    lastname.grid(row=1, column=7, sticky=W)

  
    Label(master, text="Suffix:").grid(row=1, column=8, sticky=E)
    suffix = Entry(master, width=5, font=small_font)
    suffix.grid(row=1, column=9, sticky=W)

    
    Label(master, text="Title:").grid(row=2, column=0, sticky=E)
    title = Entry(master, width=30, font=small_font)
    title.grid(row=2, column=1, sticky=W)

    
    Label(master, text="Company Name:").grid(row=3, column=0, sticky=E)
    company_name = Entry(master, width=30, font=small_font)
    company_name.grid(row=3, column=1, sticky=W)

   
    Label(master, text="Department:").grid(row=3, column=2, sticky=E)
    department = Entry(master, width=25, font=small_font)
    department.grid(row=3, column=3, sticky=W)

    
    Label(master, text="Address1:").grid(row=4, column=0, sticky=E)
    address1 = Entry(master, width=30, font=small_font)
    address1.grid(row=4, column=1, sticky=W)

    
    Label(master, text="Address2:").grid(row=4, column=2, sticky=E)
    address2 = Entry(master, width=30, font=small_font)
    address2.grid(row=4, column=3, sticky=W)
    
    Label(master, text="Suite No:").grid(row=4, column=4, sticky=E)
    suite_no = Entry(master, width=15, font=small_font)
    suite_no.grid(row=4, column=5, sticky=W)

    
    Label(master, text="City:").grid(row=5, column=0, sticky=E)
    city = Entry(master, width=25, font=small_font)
    city.grid(row=5, column=1, sticky=W)

    
    Label(master, text="State:").grid(row=5, column=2, sticky=E)
    state = Entry(master, width=5, font=small_font)
    state.grid(row=5, column=3, sticky=W)

    
    Label(master, text="Postal Code:").grid(row=5, column=4, sticky=E)
    postal_code = Entry(master, width=15, font=small_font)
    postal_code.grid(row=5, column=5, sticky=W)

    
    Label(master, text="Zip Code:").grid(row=5, column=6, sticky=E)
    zip_code = Entry(master, width=15, font=small_font)
    zip_code.grid(row=5, column=7, sticky=W)

   
    Label(master, text="Mobile Phone:").grid(row=6, column=0, sticky=E)
    mobile_phone = Entry(master, width=15, font=small_font)
    mobile_phone.grid(row=6, column=1, sticky=W)
    
    Label(master, text="Office Phone:").grid(row=6, column=2, sticky=E)
    office_phone = Entry(master, width=15, font=small_font)
    office_phone.grid(row=6, column=3, sticky=W)
    
    Label(master, text="Home Phone:").grid(row=6, column=4, sticky=E)
    home_phone = Entry(master, width=15, font=small_font)
    home_phone.grid(row=6, column=5, sticky=W)


    Label(master, text="Fax Phone:").grid(row=6, column=6, sticky=E)
    fax_phone = Entry(master, width=15, font=small_font)
    fax_phone.grid(row=6, column=7, sticky=W)

    
    Label(master, text="Office Email:").grid(row=7, column=0, sticky=E)
    office_email = Entry(master, width=30, font=small_font)
    office_email.grid(row=7, column=1, sticky=W)

    
    Label(master, text="Home Email:").grid(row=7, column=2, sticky=E)
    home_email = Entry(master, width=30, font=small_font)
    home_email.grid(row=7, column=3, sticky=W)

    
    Label(master, text="Gender:").grid(row=8, column=0, sticky=E)
    gender = Entry(master, width=7, font=small_font)
    gender.grid(row=8, column=1, sticky=W)

    
    Label(master, text="Age:").grid(row=8, column=2, sticky=E)
    age = Entry(master, width=5, font=small_font)
    age.grid(row=8, column=3, sticky=W)

    
    Label(master, text="Notes:").grid(row=9, column=0, sticky=E)
    notes = Entry(master, width=30, font=small_font)
    notes.grid(row=9, column=1, sticky=W)

    PersonID.insert(END, row[0])
    salut.insert(END, row[1])
    firstname.insert(END, row[2])
    mid_init.insert(END, row[3])
    lastname.insert(END, row[4])
    suffix.insert(END, row[5])
    title.insert(END, row[6])
    company_name.insert(END, row[7])
    department.insert(END, row[8])
    address1.insert(END, row[9])
    address2.insert(END, row[10])
    suite_no.insert(END, row[11])
    city.insert(END, row[12])
    state.insert(END, row[13])
    postal_code.insert(END, row[14])
    zip_code.insert(END, row[15])
    mobile_phone.insert(END, row[16])
    office_phone.insert(END, row[17])
    home_phone.insert(END, row[18])
    fax_phone.insert(END, row[19])
    office_email.insert(END, row[20])
    home_email.insert(END, row[21])
    gender.insert(END, row[22])
    age.insert(END, row[23])
    notes.insert(END, row[24])

    
def get_last_record():
    global PersonID
    global salut
    global firstname
    global mid_init
    global lastname
    global suffix
    global title
    global company_name
    global department
    global address1
    global address2
    global suite_no
    global city
    global state
    global postal_code
    global zip_code
    global mobile_phone
    global office_phone
    global home_phone
    global fax_phone
    global office_email
    global home_email
    global gender
    global age
    global notes
    global rowid
    global fname
    global lname

##    PersonID.delete(0, END)
##    salut.delete(0,END)
##    firstname.delete(0,END)
##    mid_init.delete(0,END)
##    lastname.delete(0,END)
##    suffix.delete(0,END)
##    title.delete(0,END)
##    company_name.delete(0,END)
##    department.delete(0,END)
##    address1.delete(0,END)
##    address2.delete(0,END)
##    suite_no.delete(0,END)
##    city.delete(0,END)
##    state.delete(0,END)
##    postal_code.delete(0,END)
##    zip_code.delete(0,END)
##    mobile_phone.delete(0,END)
##    office_phone.delete(0,END)
##    home_phone.delete(0,END)
##    fax_phone.delete(0,END)
##    office_email.delete(0,END)
##    home_email.delete(0,END)
##    gender.delete(0,END)
##    age.delete(0,END)
##    notes.delete(0,END)
    
    conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM clientinfo WHERE PersonID = (SELECT max(PersonID) from clientinfo)")
        list_load = c.fetchall()
        
    for row in list_load:
        PersonID=row[0]
        salut=row[1]
        firstname=row[2]
        mid_init=row[3]
        lastname=row[4]
        suffix=row[5]
        title=row[6]
        company_name=row[7]
        department=row[8]
        address1=row[9]
        address2=row[10]
        suite_no=row[11]
        city=row[12]
        state=row[13]
        postal_code=row[14]
        zip_code=row[15]
        mobile_phone=row[16]
        office_phone=row[17]
        home_phone=row[18]
        fax_phone=row[19]
        office_email=row[20]
        home_email=row[21]
        gender=row[22]
        age=row[23]
        notes=row[24]
    conn.commit()
    conn.close()
    
    Label(master, text="Person ID:").grid(row=0, column=0, sticky=E)
    PersonID = Entry(master, width=5, font=small_font)
    PersonID.grid(row=0, column=1, sticky=W)  

    Label(master, text="Salutation:").grid(row=1, column=0, sticky=E)
    salut = Entry(master, width=5, font=small_font)
    salut.grid(row=1, column=1, sticky=W)
    
    Label(master, text="First Name:").grid(row=1, column=2, sticky=E)
    firstname = Entry(master, width=25, font=small_font)
    firstname.grid(row=1, column=3, sticky=W)

    Label(master, text="Mid Init:").grid(row=1, column=4, sticky=E)
    mid_init = Entry(master, width=5, font=small_font)
    mid_init.grid(row=1, column=5, sticky=W)

    Label(master, text="Last Name:").grid(row=1, column=6, sticky=E)
    lastname = Entry(master, width=15, font=small_font)
    lastname.grid(row=1, column=7, sticky=W)

  
    Label(master, text="Suffix:").grid(row=1, column=8, sticky=E)
    suffix = Entry(master, width=5, font=small_font)
    suffix.grid(row=1, column=9, sticky=W)

    
    Label(master, text="Title:").grid(row=2, column=0, sticky=E)
    title = Entry(master, width=30, font=small_font)
    title.grid(row=2, column=1, sticky=W)

    
    Label(master, text="Company Name:").grid(row=3, column=0, sticky=E)
    company_name = Entry(master, width=30, font=small_font)
    company_name.grid(row=3, column=1, sticky=W)

   
    Label(master, text="Department:").grid(row=3, column=2, sticky=E)
    department = Entry(master, width=25, font=small_font)
    department.grid(row=3, column=3, sticky=W)

    
    Label(master, text="Address1:").grid(row=4, column=0, sticky=E)
    address1 = Entry(master, width=30, font=small_font)
    address1.grid(row=4, column=1, sticky=W)

    
    Label(master, text="Address2:").grid(row=4, column=2, sticky=E)
    address2 = Entry(master, width=30, font=small_font)
    address2.grid(row=4, column=3, sticky=W)
    
    Label(master, text="Suite No:").grid(row=4, column=4, sticky=E)
    suite_no = Entry(master, width=15, font=small_font)
    suite_no.grid(row=4, column=5, sticky=W)

    
    Label(master, text="City:").grid(row=5, column=0, sticky=E)
    city = Entry(master, width=25, font=small_font)
    city.grid(row=5, column=1, sticky=W)

    
    Label(master, text="State:").grid(row=5, column=2, sticky=E)
    state = Entry(master, width=5, font=small_font)
    state.grid(row=5, column=3, sticky=W)

    
    Label(master, text="Postal Code:").grid(row=5, column=4, sticky=E)
    postal_code = Entry(master, width=15, font=small_font)
    postal_code.grid(row=5, column=5, sticky=W)

    
    Label(master, text="Zip Code:").grid(row=5, column=6, sticky=E)
    zip_code = Entry(master, width=15, font=small_font)
    zip_code.grid(row=5, column=7, sticky=W)

   
    Label(master, text="Mobile Phone:").grid(row=6, column=0, sticky=E)
    mobile_phone = Entry(master, width=15, font=small_font)
    mobile_phone.grid(row=6, column=1, sticky=W)
    
    Label(master, text="Office Phone:").grid(row=6, column=2, sticky=E)
    office_phone = Entry(master, width=15, font=small_font)
    office_phone.grid(row=6, column=3, sticky=W)
    
    Label(master, text="Home Phone:").grid(row=6, column=4, sticky=E)
    home_phone = Entry(master, width=15, font=small_font)
    home_phone.grid(row=6, column=5, sticky=W)

    
    Label(master, text="Fax Phone:").grid(row=6, column=6, sticky=E)
    fax_phone = Entry(master, width=15, font=small_font)
    fax_phone.grid(row=6, column=7, sticky=W)
    
    Label(master, text="Office Email:").grid(row=7, column=0, sticky=E)
    office_email = Entry(master, width=30, font=small_font)
    office_email.grid(row=7, column=1, sticky=W)

    
    Label(master, text="Home Email:").grid(row=7, column=2, sticky=E)
    home_email = Entry(master, width=30, font=small_font)
    home_email.grid(row=7, column=3, sticky=W)

    
    Label(master, text="Gender:").grid(row=8, column=0, sticky=E)
    gender = Entry(master, width=7, font=small_font)
    gender.grid(row=8, column=1, sticky=W)

    
    Label(master, text="Age:").grid(row=8, column=2, sticky=E)
    age = Entry(master, width=5, font=small_font)
    age.grid(row=8, column=3, sticky=W)

    
    Label(master, text="Notes:").grid(row=9, column=0, sticky=E)
    notes = Entry(master, width=30, font=small_font)
    notes.grid(row=9, column=1, sticky=W)



    PersonID.insert(END, row[0])
    salut.insert(END, row[1])
    firstname.insert(END, row[2])
    mid_init.insert(END, row[3])
    lastname.insert(END, row[4])
    suffix.insert(END, row[5])
    title.insert(END, row[6])
    company_name.insert(END, row[7])
    department.insert(END, row[8])
    address1.insert(END, row[9])
    address2.insert(END, row[10])
    suite_no.insert(END, row[11])
    city.insert(END, row[12])
    state.insert(END, row[13])
    postal_code.insert(END, row[14])
    zip_code.insert(END, row[15])
    mobile_phone.insert(END, row[16])
    office_phone.insert(END, row[17])
    home_phone.insert(END, row[18])
    fax_phone.insert(END, row[19])
    office_email.insert(END, row[20])
    home_email.insert(END, row[21])
    gender.insert(END, row[22])
    age.insert(END, row[23])
    notes.insert(END, row[24])

def delete_record():
    global PersonID
    global salut
    global firstname
    global mid_init
    global lastname
    global suffix
    global title
    global company_name
    global department
    global address1
    global address2
    global suite_no
    global city
    global state
    global postal_code
    global zip_code
    global mobile_phone
    global office_phone
    global home_phone
    global fax_phone
    global office_email
    global home_email
    global gender
    global age
    global notes
    
    PersonID1 = PersonID.get()

    
    conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
    with conn:
        c = conn.cursor()
        c.execute( "DELETE FROM clientinfo WHERE PersonID LIKE %s", [PersonID1] )
        list_load = c.fetchall()
    
    PersonID.delete(0, END)
    salut.delete(0,END)
    firstname.delete(0,END)
    mid_init.delete(0,END)
    lastname.delete(0,END)
    suffix.delete(0,END)
    title.delete(0,END)
    company_name.delete(0,END)
    department.delete(0,END)
    address1.delete(0,END)
    address2.delete(0,END)
    suite_no.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    postal_code.delete(0,END)
    zip_code.delete(0,END)
    mobile_phone.delete(0,END)
    office_phone.delete(0,END)
    home_phone.delete(0,END)
    fax_phone.delete(0,END)
    office_email.delete(0,END)
    home_email.delete(0,END)
    gender.delete(0,END)
    age.delete(0,END)
    notes.delete(0,END)
    conn.close()
    
    conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
    with conn:
        c = conn.cursor()
        c.execute("ALTER TABLE clientinfo DROP COLUMN PersonID;")
    conn.commit()
    conn.close()

    conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
    with conn:
        c = conn.cursor()    
        c.execute("ALTER TABLE clientinfo ADD PersonID INT PRIMARY KEY AUTO_INCREMENT FIRST;")
    conn.commit()
    conn.close()

    conn = pymysql.connect(host='localhost', port=3306, user='staffmember', passwd='Customer1', db='business_info')
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM clientinfo;")
    conn.commit()
    conn.close()

  
    get_first_record()


if __name__ == "__main__":
               
    master.configure(background='#ff8c8c')
    
    addcustbutton = Button(master, text=' Add New Customer   ',fg="green", font=small_font, command=add_new_customer).grid(row=25, column=1, sticky=W, padx=4, pady=4)
    insertbutton = Button(master, text='  Insert Customer  ',fg="red",font=small_font, command=insert_data).grid(row=25, column=2, sticky=W, padx=4, pady=4)
    getrecordbutton = Button(master, text='  Get Records    ', fg="purple",font=small_font, command=get_customer_record).grid(row=25, column=3, sticky=W, padx=4, pady=4)
    updatebutton = Button(master, text='Update Record', fg="Blue",font=small_font, command=update_record).grid(row=25,  column=4, sticky=W, padx=4, pady=4)

    getfirstrecbutton = Button(master, text='       First Record         ',fg="black", font=small_font,command=get_first_record).grid(row=26, column=1, sticky=W, padx=4, pady=4)
    getprevrecordbutton = Button(master, text=' Previous Record ', fg="dark green",font=small_font, command=get_previous_record).grid(row=26, column=2, sticky=W, padx=4, pady=4)
    getnextrecbutton = Button(master, text='  Next Record     ', fg="blue",font=small_font, command=get_next_record).grid(row=26, column=3, sticky=W, padx=4, pady=4)
    getlastbuttonbutton = Button(master, text='   Last Record  ', fg="brown",font=small_font, command=get_last_record).grid(row=26, column=4, sticky=W, padx=4, pady=4)

    deletebutton = Button(master, text=  ' Delete Record', fg="red",font=small_font, command=delete_record).grid(row=27, column=4, sticky=W, padx=4, pady=4)

    quitbutton = Button(master, text='           Quit            ', fg="red",font=small_font, command=master.destroy).grid(row=30, column=2, sticky=W, padx=4, pady=4)


master.mainloop()
