from werkzeug.security import generate_password_hash
from urllib.parse import urlparse
import psycopg2


class DBManager:
    def __init__(self, database_url):
        """Initializes the connection url"""
        parsed_url = urlparse( database_url )
        dbname = parsed_url.path[1:]
        username = parsed_url.username
        hostname = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port

        self.conn = psycopg2.connect(
            database= dbname,
            user= username,
            password= password,
            host= hostname,
            port= port)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def create_tables(self):
        """Create Tables"""
        sql_commands = (
               """CREATE TABLE IF NOT EXISTS users(
                userId SERIAL PRIMARY KEY,
                email varchar NOT NULL,
                username varchar NOT NULL,
                password varchar NOT NULL)""",

               """CREATE TABLE IF NOT EXISTS questions(
                qnId SERIAL PRIMARY KEY,
                Question varchar NOT NULL,
                FOREIGN KEY (qnId) REFERENCES users(userId) ON DELETE CASCADE ON UPDATE CASCADE)""",
               """CREATE TABLE IF NOT EXISTS answers(
                         ansId SERIAL PRIMARY KEY,
                         Answers varchar NOT NULL,
                         FOREIGN KEY (ansId) REFERENCES questions(qnId) ON DELETE CASCADE ON UPDATE CASCADE)""")
        for sql_command in sql_commands:
            self.cur.execute(sql_command)


    def create_user(self, data):
        """Methods to manage users"""
        self.cur.execute("INSERT INTO users (email, username, password)"
                         "VALUES ('{}', '{}', '{}');".format
                         (data['email'], data['username'],
                          generate_password_hash(data['password'], method='sha256')))

    def create_question(self, data):
        """Methods to manage Question"""
        self.cur.execute("INSERT INTO questions (Question)"
                         "VALUES ('{}');".format
                         (data['Question']))

    def create_answer(self, data):
        """Methods to manage Question"""
        self.cur.execute("INSERT INTO questions (Question)"
                         "VALUES ('{}');".format
                         (data['Question']))

    def user_name_screening(self, username):
        query = "SELECT * FROM users WHERE username=%s"
        self.cur.execute(query, (username,))
        user = self.cur.fetchone()
        return user

    def email_name_screening(self, email):
        query = "SELECT * FROM users WHERE email=%s"
        self.cur.execute(query, (email,))
        email = self.cur.fetchone()
        return email

    def question_screening(self, Question):
        query = "SELECT * FROM questions WHERE Question=%s"
        self.cur.execute(query, (Question,))
        Question = self.cur.fetchone()
        return Question

    def view_user(self):
        query = "SELECT email, username FROM users;"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def auth_user(self, username):
        query = "SELECT * FROM users WHERE username=%s"
        self.cur.execute(query, (username,))
        user = self.cur.fetchone()
        user_dict = {'username': user[2], "password": user[3]}
        return user_dict

    def trancate_table(self, table):
        """Trancates the table"""
        self.cur.execute("TRUNCATE TABLE {} RESTART IDENTITY".format(table))

    def view_questions(self):
        query = "SELECT qnId, Question FROM questions;"
        self.cur.execute( query )
        rows = self.cur.fetchall()
        return rows