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


def mentors():
    """On this page you should show the result of a query that returns the name of the mentors
    plus the name and country of the school (joining with the schools table) ordered by the mentors id column 
    (columns: mentors.first_name, mentors.last_name, schools.name, schools.country). """
    data = []
    cursor.execute("""
                   SELECT
                   mentors.first_name AS "First name",
                   mentors.last_name AS "Last name",
                   schools.name AS "School's name",
                   schools.country AS "School's country"
                   FROM mentors
                   LEFT JOIN schools ON mentors.city=schools.city
                   ORDER BY mentors.id;
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def all_school():
    """On this page you should show the result of a query that returns the name of the mentors plus the name
    and country of the school (joining with the schools table) ordered by the mentors id column.
    BUT include all the schools, even if there's no mentor yet!
    columns: mentors.first_name, mentors.last_name, schools.name, schools.country"""
    data = []
    cursor.execute("""
                   SELECT
                   mentors.first_name AS "First name",
                   mentors.last_name AS "Last name",
                   schools.name AS "School's name",
                   schools.country AS "School's country"
                   FROM mentors
                   FULL JOIN schools ON mentors.city=schools.city
                   ORDER BY mentors.id;
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def mentors_by_country():
    """On this page you should show the result of a query that returns the number of the mentors per country
    ordered by the name of the countries. columns: country, count"""
    data = []
    cursor.execute("""
                   SELECT
                   schools.country AS "Country",
                   COUNT(mentors) AS "Count"
                   FROM mentors
                   LEFT JOIN schools ON schools.city=mentors.city
                   GROUP BY schools.country
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def contacts():
    """On this page you should show the result of a query that returns the name of the school plus the name of
    contact person at the school (from the mentors table) ordered by the name of the school
    columns: schools.name, mentors.first_name, mentors.last_name"""
    data = []
    cursor.execute("""
                   SELECT
                   schools.name AS "School's name",
                   mentors.first_name AS "First name",
                   mentors.last_name AS "Last name"
                   FROM schools
                   INNER JOIN mentors ON schools.contact_person=mentors.id
                   ORDER BY schools.name
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def applicants():
    """On this page you should show the result of a query that returns the first name and the code
    of the applicants plus the creation_date of the application (joining with the applicants_mentors table)
    ordered by the creation_date in descending order BUT only for applications later than 2016-01-01
    columns: applicants.first_name, applicants.application_code, applicants_mentors.creation_date"""
    data = []
    cursor.execute("""
                   SELECT
                   applicants.first_name AS "First name",
                   applicants.application_code AS "Application code",
                   applicants_mentors.creation_date AS "Creation date"
                   FROM applicants
                   RIGHT JOIN applicants_mentors ON applicants_mentors.applicant_id=applicants.id
                   WHERE applicants_mentors.creation_date > '2016-01-01'
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data


def applicants_and_mentors():
    """On this page you should show the result of a query that returns the first name and the code of the applicants
    plus the name of the assigned mentor (joining through the applicants_mentors table) ordered by
    the applicants id column. Show all the applicants, even if they have no assigned mentor in the database!
    In this case use the string 'None' instead of the mentor name
    columns: applicants.first_name, applicants.application_code, mentor_first_name, mentor_last_name"""
    data = []
    cursor.execute("""
                   SELECT
                   applicants.first_name AS "Applicant's first name",
                   applicants.application_code AS "Application code",
                   mentors.first_name AS "Mentor's first name",
                   mentors.last_name AS "Mentor's last name"
                   FROM applicants_mentors
                   LEFT JOIN mentors ON mentors.id=applicants_mentors.mentor_id
                   RIGHT JOIN applicants on applicants.id=applicants_mentors.applicant_id
                   """)
    column_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    data.append(column_names)
    data.append(rows)
    return data
