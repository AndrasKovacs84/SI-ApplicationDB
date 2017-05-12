from flask import Flask, render_template, redirect, request, make_response
import queries
import helpers

app = Flask(__name__)

menu_options = [{'option_name': 'List mentor names', 'query': 'mentor_name'},
                {'option_name': 'List mentor nicknames', 'query': 'mentor_nicks'},
                {'option_name': 'Find applicant "Carol"', 'query': 'applicant_carol'},
                {'option_name': 'Find applicant by email', 'query': 'find_applicant_by_email'},
                {'option_name': 'Insert new applicant Markus', 'query': 'new_applicant_insert_select'},
                {'option_name': 'Update applicant tel nr, Jemima', 'query': 'jemima_tel_nr_update'},
                {'option_name': 'Delete applicants by email', 'query': 'delete_by_email'},
                {'option_name': 'Display mentors table', 'query': 'show_mentors'},
                {'option_name': 'Display applicants table', 'query': 'show_applicants'}]

'''
    query = {'table': None,
             'columns': None,
             'filter': None,
             'order_by': None,
             'method': 'GET'}
'''


@app.route("/", methods=['GET'])
def index():
    '''Renders template for the main page, where the user can choose a query to display'''
    global menu_options
    print(menu_options)
    return render_template('index.html', menu_options=menu_options)


@app.route("/queries/<query>", methods=['GET'])
def display_query(query):
    function_to_call = getattr(queries, query)
    query_result = function_to_call()
    return render_template('list.html', query_result=query_result)


@app.route("/custom_query", methods=['GET'])
def custom_query():
    response = None

    query = {'table': None,
             'columns': None,
             'filter': None,
             'order_by': None,
             'method': 'GET'}

    query = helpers.read_qry_from_cookies()
    print(query['columns'])

    if request.args.get('table') is not None:
        query['table'] = request.args.get('table')
        response = make_response(redirect('/custom_query'))
        response.set_cookie('table', request.args.get('table'))
        return response

    if request.args.getlist('columns') != []:
        query['columns'] = ', '.join(request.args.getlist('columns'))
        response = make_response(redirect('/custom_query'))
        response.set_cookie('columns', query['columns'])
        return response

    if request.args.get('column_to_search') is not None:
        if request.args.get('search_pos') == 'start':
            where_statement = (request.args.get('column_to_search') + " LIKE " +
                               str(request.args.get('keyword')) + "%")
        if request.args.get('search_pos') == 'mid':
            where_statement = (request.args.get('column_to_search') + " LIKE " +
                               "%" + str(request.args.get('keyword')) + "%")
        if request.args.get('search_pos') == 'end':
            where_statement = (request.args.get('column_to_search') + " LIKE " +
                               "%" + str(request.args.get('keyword')))
        query['filter'] = where_statement
        response = make_response(redirect('/custom_query'))
        response.set_cookie('filter', where_statement)
        return response

    response = make_response(render_template('custom_query.html', query=query))
    return response

'''
        query['table'] = request.args.get('table')
    else:
        if query['columns'] is None:
            query['columns'] = request.args.getlist('column')
    query['filter'] = request.args.get('filter')
    query['order_by'] = request.args.get('order_by')
    print(query)

    return render_template("custom_query.html", query=query)
'''

if __name__ == '__main__':
    app.run(debug=True)