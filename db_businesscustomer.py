import sys
import os
import sqlite3
from contextlib import closing

from BusinessCustomer import Clientinfo


conn = None

def connect():
    global conn
    if not conn:
        if sys.platform == "Win32":
            DB_FILE = "/Users/User/AppData/Local/Programs/Python/Python37/_db/customerservice.sqlite"
        else:
            HOME = os.environ["HOME"]
            DB_FILE = "/Users/User/AppData/Local/Programs/Python/Python37/_db/customerservice.sqlite"

        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_client(row):
    return Clientinfo(row["salut"], row["firstname"], row["mid_init"], row["lastname"], row["suffix"], row["title"],row["company_name"], row["department"], row["address1"],row["address2"], row["city"], row["state"], row["postal_code"],row["zip_code"],
                  row["mobile_phone"], row["office_phone"],row["home_phone"],row["fax_phone"], row["office_email"], row["home_email"], row["gender"], row["age"]row["notes"])

def add_person(person):
    sql = '''INSERT INTO clientinfo(salut, firstname, mid_init, lastname,
                 suffix, title, company_name, department, address1,
                 address2, suite_no, city, state, postal_code, zip_code,
                 mobile_phone, office_phone, home_phone, fax_phone, office_email, home_email,
                 gender, age, notes)
             VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (clientinfo.salut, clientinfo.firstname, clientinfo.mid_init,
                  clientinfo.lastname, clientinfo.suffix, clientinfo.title, clientinfo.company_name,
                  clientinfo.department, clientinfo.address1, clientinfo.address2, clientinfo.suite_no,
                  clientinfo.city, clientinfo.state, clientinfo.postal_code, clientinfo.zip_code,
                  clientinfo.mobile_phone, clientinfo.office_phone, clientinfo.home_phone, clientinfo.fax_phone
                  clientinfo.office_email, clientinfo.home_email,clientinfo.gender, clientinfo.age, clientinfo.notes))
        conn.commit()

def get_person():

    query = '''SELECT * FROM clientinfo'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    clientinfo = []
    for row in results:
        clientinfo.append(make_clientinfo(row))
    return person
        
def delete_person(person_id):
    sql = '''DELETE FROM clientinfo WHERE personid = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (person_id,))
        conn.commit()

