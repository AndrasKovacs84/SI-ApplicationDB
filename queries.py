import psycopg2

connect_str = "dbname='andras' user='andras' host='localhost' password='andras'"
# connect_str = "dbname='apha' user='apha' host='localhost' password='AndrasKovacs84'"
conn = psycopg2.connect(connect_str)
conn.autocommit = True
cursor = conn.cursor()


def mentor_name():
    '''Write a query that returns the 2 name columns of the mentors table.
    columns: first_name, last_name'''
    data = []
    cursor.execute("""SELECT first_name as "First Name", last_name as "Last Name"
                   FROM mentors""")
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def mentor_nicks():
    '''Write a query that returns the nick_name-s of all mentors working at Miskolc.
    column: nick_name'''
    data = []
    cursor.execute("""
                   SELECT nick_name as "Nickname"
                   FROM mentors
                   WHERE city='Miskolc';
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def applicant_carol():
    '''We had interview with an applicant, some Carol. We don't remember her name, but she left her hat at the school.
    We want to call her to give her back her hat. To look professional, we also need her full name when she answers
    the phone (for her full_name, you want to include a concatenation into your query, to get her full_name,
    like: "Carol Something" instead of having her name in 2 different columns in the result.
    This columns should be called: full_name). columns: full_name, phone_number'''
    data = []
    cursor.execute("""
                   SELECT CONCAT(first_name, ' ', last_name) as "Full name", phone_number as "Phone number"
                   FROM applicants
                   WHERE first_name='Carol';
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def find_applicant_by_email():
    '''We called Carol, and she said it's not her hat. It belongs to another girl, who went to the famous
    Adipiscingenimmi University. You should write a query to get the same informations like with Carol,
    but for this other girl. The only thing we know about her is her school e-mail address ending:
    '@adipiscingenimmi.edu'. columns: full_name, phone_number'''
    data = []
    cursor.execute("""
                   SELECT CONCAT(first_name, ' ', last_name) AS "Full Name", phone_number AS "Phone Number"
                   FROM applicants
                   WHERE email LIKE '%@adipiscingenimmi.edu';
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def new_applicant_insert_select():
    '''After we returned the hat, a new applicant appeared at the school, and he wants to get into the application process.
    His name is Markus Schaffarzyk, has a number: 003620/725-2666 and e-mail address: djnovus@groovecoverage.com
    Our generator gave him the following application code: 54823
    After INSERTing the data, write a SELECT query, that returns with all the columns of this applicant!
    (use the unique application code for your condition!)'''
    data = []

    try:
        cursor.execute("""
                       INSERT INTO applicants
                       (first_name, last_name, phone_number, email, application_code)
                       VALUES
                       ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823 )
                       """)
    except psycopg2.IntegrityError as err:
        print(err)

    cursor.execute("""
                   SELECT *
                   FROM applicants
                   WHERE application_code=54823
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def jemima_tel_nr_update():
    '''Jemima Foreman, an applicant called us, that her phone number changed to: 003670/223-7459
    Write an UPDATE query, that changes this data in the database for this applicant.
    Also, write a SELECT query, that checks the phone_number column of this applicant.
    Use both of her name parts in the conditions!'''
    data = []
    cursor.execute("""
                   UPDATE applicants
                   SET phone_number='003670/223-7459'
                   WHERE first_name='Jemima' AND last_name='Foreman'
                   """)
    cursor.execute("""
                   SELECT *
                   FROM applicants
                   WHERE first_name='Jemima' AND last_name='Foreman'
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def delete_by_email():
    '''Arsenio, an applicant called us, that he and his friend applied to Codecool.
    They both want to cancel the process, because they got an investor for the site they run: mauriseu.net
    Write DELETE query to remove all the applicants, who applied with emails for this domain
    (e-mail address has this domain after the @ sign).'''
    cursor.execute("""
                   DELETE FROM applicants
                   WHERE email LIKE '%@mauriseu.net'""")
    data = [['Taken action'], [['Applicants deleted']]]
    return data


def show_mentors():
    data = []
    cursor.execute("""
                   SELECT *
                   FROM mentors
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def show_applicants():
    data = []
    cursor.execute("""
                   SELECT *
                   FROM applicants
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def custom_query(query):
    '''Displays the query chosen by the user. Parameter is a dictionary of the relevant properties
    for a simple query. Returns the results of the query. data[0] = list of column names as header,
    data[1] = list of lists, where each nested list represents a row of data.'''
    data = []
    cursor.execute("""
                   SELECT DISTINCT {1}
                   FROM {0}
                   WHERE {2}
                   ORDER BY {3};
                   """.format(query['table'], ", ".join(query['columns']), query['filter'], query['order_by']))
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data
