import sys
import os
import sqlite3
from contextlib import closing

from Customer import Person
from Customer import Product
from Customer import Category
from Customer import Movie

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

def make_category(row):
    return Category(row["categoryID"], row["categoryname"])

def make_movie(row):
    return Movie(row["movieID"], row["name"], row["year"], row["minutes"], row["price"],
                 make_category(row))

def make_person(row):
    return Person(row["salut"], row["firstname"], row["mid_init"], row["lastname"],row["address1"],row["address2"], row["city"], row["state"], row["zip_code"],
                  row["mobile_phone"], row["home_phone"], row["home_email"], row["gender"], row["age"])

def get_categories():
    query = '''SELECT categoryID, category_name as categoryname 
               FROM Category'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories

def get_category(category_id):
    query = '''SELECT categoryID, category_name as categoryname 
                FROM Category WHERE categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()

    category = make_category(row)
    return category

def get_movies_by_category(category_id):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.category_name as categoryname, 
                      movie.price  
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE Movie.categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

def get_movies_by_year(year):
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID as categoryID,
                      Category.category_name as categoryname, movie.price 
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE Movie.year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies
               
def add_movie(movie):
    sql = '''INSERT INTO Movie(categoryID, name, year, minutes, price)
             VALUES(?,?,?,?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie.category.id, movie.name, movie.year,
                  movie.minutes, movie.price))
        conn.commit()

def add_person(person):
    sql = '''INSERT INTO Person(salut, firstname, mid_init, lastname,
                 suffix, title, company_name, department, address1,
                 address2, suite_no, city, state, postal_code, zip_code,
                 mobile_phone, office_phone, home_phone, office_email, home_email,
                 gender, age)
             VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (person.salut, person.firstname, person.mid_init,
                  person.lastname, person.suffix, person.title, person.company_name,
                  person.department, person.address1, person.address2, person.suite_no,
                  person.city, person.state, person.postal_code, person.zip_code,
                  person.mobile_phone, person.office_phone, person.home_phone,
                  person.office_email, person.home_email,person.gender, person.age))
        conn.commit()

def get_categories():
    query = '''SELECT categoryID, category_name as categoryname 
               FROM Category'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories

def get_person():
##    query = '''SELECT personid, salut, firstname, mid_init, lastname,
##                      address1, address2, city, state, zip_code,
##                      mobile_phone, home_phone, home_email, gender, age 
##
    query = '''SELECT * FROM Person'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    person = []
    for row in results:
        person.append(make_person(row))
    return person
        
def delete_movie(movie):
    sql = '''DELETE FROM Movie WHERE movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie_id,))
        conn.commit()

def delete_person(person_id):
    sql = '''DELETE FROM Person WHERE personid = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (person_id,))
        conn.commit()

