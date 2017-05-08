# SI-ApplicationDB

The HR department wants answers to the following questions:

1. - Write a query that returns the 2 name columns of the mentors table.
columns: first_name, last_name
2. - Write a query that returns the nick_name-s of all mentors working at Miskolc.
column: nick_name
3. - We had interview with an applicant, some Carol. We don't remember her name, but she left her hat at the school. We want to call her to give her back her hat. To look professional, we also need her full name when she answers the phone (for her full_name, you want to include a concatenation into your query, to get her full_name, like: "Carol Something" instead of having her name in 2 different columns in the result. This columns should be called: full_name).
columns: full_name, phone_number
4. - We called Carol, and she said it's not her hat. It belongs to another girl, who went to the famous Adipiscingenimmi University.
You should write a query to get the same informations like with Carol, but for this other girl.
The only thing we know about her is her school e-mail address ending: '@adipiscingenimmi.edu'.
columns: full_name, phone_number
5. - After we returned the hat, a new applicant appeared at the school, and he wants to get into the application process.
His name is Markus Schaffarzyk, has a number: 003620/725-2666 and e-mail address: djnovus@groovecoverage.com
Our generator gave him the following application code: 54823

After INSERTing the data, write a SELECT query, that returns with all the columns of this applicant! (use the unique application code for your condition!)

Jemima Foreman, an applicant called us, that her phone number changed to: 003670/223-7459
Write an UPDATE query, that changes this data in the database for this applicant.
Also, write a SELECT query, that checks the phone_number column of this applicant.
Use both of her name parts in the conditions!
Arsenio, an applicant called us, that he and his friend applied to Codecool.
They both want to cancel the process, because they got an investor for the site they run: mauriseu.net

Write DELETE query to remove all the applicants, who applied with emails for this domain (e-mail address has this domain after the @ sign).

You need to create a console application with some simple menu, where each menu point answers one question (or does what the question asks) from the above list. If the question is to print out some table, please print it out in some readable way (e.g. different rows on separate lines, no unnecessary parenthesis around values etc.), but don't mess a lot with formatting.
