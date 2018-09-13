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
                userId INTEGER NOT NULL,
                Question varchar NOT NULL,
                FOREIGN KEY (userId) REFERENCES users(userId) ON DELETE CASCADE ON UPDATE CASCADE)""",
               """CREATE TABLE IF NOT EXISTS answers(
                         ansId SERIAL PRIMARY KEY,
                         qnId INTEGER NOT NULL,
                         Ans_Auth_Id INTEGER NOT NULL,
                         Answers varchar NOT NULL,
                         Prefered_Ans_Status boolean DEFAULT FALSE,
                         FOREIGN KEY (qnId) REFERENCES questions(qnId) ON DELETE CASCADE ON UPDATE CASCADE)""")
        for sql_command in sql_commands:
            self.cur.execute(sql_command)


    def create_user(self, data):
        """Methods to manage users"""
        self.cur.execute("INSERT INTO users (email, username, password)"
                         "VALUES ('{}', '{}', '{}');".format
                         (data['email'], data['username'],
                          generate_password_hash(data['password'], method='sha256')))

    def create_question(self,userId, data):
        """Methods to manage Question"""
        self.cur.execute("INSERT INTO questions (userId, Question)"
                         "VALUES ('{}', '{}');".format
                         (userId, data['Question']))

    def create_answer(self, qnId,Ans_Auth_Id, data):
        """Methods to manage Question"""
        self.cur.execute("INSERT INTO answers (qnId, Ans_Auth_Id, Answers)"
                         "VALUES ('{}','{}','{}');".format
                         (qnId,Ans_Auth_Id, data['Answer']))

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

    def answer_screening(self, Answer):
        query = "SELECT * FROM answers WHERE Answer=%s"
        self.cur.execute(query, (Answer,))
        Answer = self.cur.fetchone()
        return Answer

    def fetch_by_param(self, table_name, column, param):
        """Fetches a single a parameter from a specific table and column"""
        query = "SELECT * FROM {} WHERE {} = '{}'".format(
            table_name, column, param )
        self.cur.execute( query )
        row = self.cur.fetchone()
        return row

    def fetch_by_specific_param(self, other_param, table_name, column, param):
        """Fetches a single a parameter from a specific table and column"""
        query = "SELECT {} FROM {} WHERE {} = '{}'".format(
           other_param, table_name, column, param )
        self.cur.execute( query )
        row = self.cur.fetchone()
        return row

    def fetch_by_id(self, qnId):
        """ Gets a question by id from the questions table"""
        self.cur.execute(
            "SELECT * FROM questions WHERE qnId = '{}'".format(qnId))
        rows = self.cur.fetchall()
        questions = []
        for row in rows:
            questions.append({'qnId': row[1], 'Question': row[2]})
        return questions

    def get_question(self, qnId):
        query = "SELECT * FROM questions WHERE qnId=%s"
        self.cur.execute(query, (qnId,))
        qn = self.cur.fetchone()
        if not qn:
            return {'message': 'Question does not exist'}
        qn_dict = {'qnId': qn[1]}
        return qn_dict

    def auth_user(self, username):
        query = "SELECT * FROM users WHERE username=%s"
        self.cur.execute(query, (username,))
        user = self.cur.fetchone()
        if not user:
            return {'message': 'User does not exist'}
        user_dict = {'userId': user[0],'username': user[2], "password": user[3]}
        return user_dict

    def trancate_table(self):
        """Trancates the table"""
        self.cur.execute("TRUNCATE TABLE users CASCADE;")

    def drop_table(self):
        """drop the table"""
        self.cur.execute("DROP TABLE users CASCADE;")

    def view_questions(self):
        query = "SELECT qnId, Question FROM questions;"
        self.cur.execute( query )
        rows = self.cur.fetchall()
        Questions = [Questions for Questions in rows]
        all_qns = []
        for value in range(len(Questions)):
            qn_variable =(
                {'qn_id': Questions[value][0],
                 'Question': Questions[value][1]})
            all_qns.append(qn_variable)
        return all_qns

    def view_question_single_id(self, qnId):
        query = "SELECT qnId, Question FROM questions;"
        self.cur.execute( query )
        rows = self.cur.fetchall()
        Questions = [Questions for Questions in rows]
        single_qns = []
        for value in range( len( Questions ) ):
            if Questions[value][0] == qnId:
                qn_variable = (
                    {'qn_id': Questions[value][0],
                     'Question': Questions[value][1]})
                single_qns.append( qn_variable )

        query = "SELECT ansId, Answers ,Prefered_Ans_Status FROM answers WHERE qnId = %s;"
        self.cur.execute( query, (qnId,) )
        rows = self.cur.fetchall()
        Answers = [Answers for Answers in rows]
        all_ans = []
        for value in range( len(Answers) ):
            ans_variable = (
                [{'Ans_id': Answers[value][0],
                 'Answer': Answers[value][1],
                 'Prefered_Ans_Status': Answers[value][2]}])
            all_ans.append( ans_variable )
        return {'Your question is': single_qns+all_ans}

    def delete_question(self, qnId):
        query = "DELETE FROM questions WHERE qnId=%s"
        self.cur.execute( query, (qnId,) )

    def fetch_question_values(self, qnId, userId):
        query = "SELECT  * FROM questions WHERE qnId=%s and userId=%s"
        self.cur.execute( query, (qnId, userId) )
        quest = self.cur.fetchone()
        return quest

    def fetch_question_value(self, qnId):
        query = "SELECT  * FROM questions WHERE qnId=%s "
        self.cur.execute( query, (qnId,) )
        quest = self.cur.fetchone()
        return quest

    def modify_ans_status(self,qnId,  ansId):
        self.cur.execute(
            "UPDATE Answers SET Prefered_Ans_Status=TRUE WHERE qnId= %s and ansId=%s",
            (qnId , ansId))

    def modify_ans(self,qnId,  ansId, data,):
        self.cur.execute(
            "UPDATE Answers SET Answers=%s WHERE qnId=%s and ansId=%s",
            (data['Answers'], qnId , ansId))

