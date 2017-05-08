import psycopg2

connect_str = "dbname='andras' user='andras' host='localhost' password='andras'"
conn = psycopg2.connect(connect_str)
conn.autocommit = True
cursor = conn.cursor()


'''
cursor.execute("""SELECT * FROM applicants""")
rows = cursor.fetchall()
print(rows)'''


def qry_mentor_name():
    '''Write a query that returns the 2 name columns of the mentors table.
    columns: first_name, last_name'''
    pass


def qry_mentor_nicks():
    '''Write a query that returns the nick_name-s of all mentors working at Miskolc.
    column: nick_name'''
    pass


def qry_applicant_carol():
    '''We had interview with an applicant, some Carol. We don't remember her name, but she left her hat at the school.
    We want to call her to give her back her hat. To look professional, we also need her full name when she answers
    the phone (for her full_name, you want to include a concatenation into your query, to get her full_name,
    like: "Carol Something" instead of having her name in 2 different columns in the result.
    This columns should be called: full_name). columns: full_name, phone_number'''
    pass


def qry_find_applicant_by_email():
    '''We called Carol, and she said it's not her hat. It belongs to another girl, who went to the famous
    Adipiscingenimmi University. You should write a query to get the same informations like with Carol,
    but for this other girl. The only thing we know about her is her school e-mail address ending:
    '@adipiscingenimmi.edu'. columns: full_name, phone_number'''
    pass


def qry_new_applicant_insert_select():
    '''After we returned the hat, a new applicant appeared at the school, and he wants to get into the application process.
    His name is Markus Schaffarzyk, has a number: 003620/725-2666 and e-mail address: djnovus@groovecoverage.com
    Our generator gave him the following application code: 54823
    After INSERTing the data, write a SELECT query, that returns with all the columns of this applicant!
    (use the unique application code for your condition!)'''
    pass


def qry_jemima_tel_nr_update():
    '''Jemima Foreman, an applicant called us, that her phone number changed to: 003670/223-7459
    Write an UPDATE query, that changes this data in the database for this applicant.
    Also, write a SELECT query, that checks the phone_number column of this applicant.
    Use both of her name parts in the conditions!'''
    pass


def qry_delete_by_email():
    '''Arsenio, an applicant called us, that he and his friend applied to Codecool.
    They both want to cancel the process, because they got an investor for the site they run: mauriseu.net
    Write DELETE query to remove all the applicants, who applied with emails for this domain
    (e-mail address has this domain after the @ sign).'''
    pass


