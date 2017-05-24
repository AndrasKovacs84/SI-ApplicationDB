from flask import Flask, render_template, redirect, request, make_response
import queries
import helpers

app = Flask(__name__)

basic_menu_options = [{'option_name': 'List mentor names', 'query': 'mentor_name'},
                      {'option_name': 'List mentor nicknames', 'query': 'mentor_nicks'},
                      {'option_name': 'Find applicant "Carol"', 'query': 'applicant_carol'},
                      {'option_name': 'Find applicant by email', 'query': 'find_applicant_by_email'},
                      {'option_name': 'Insert new applicant Markus', 'query': 'new_applicant_insert_select'},
                      {'option_name': 'Update applicant tel nr, Jemima', 'query': 'jemima_tel_nr_update'},
                      {'option_name': 'Delete applicants by email', 'query': 'delete_by_email'},
                      {'option_name': 'Display mentors table', 'query': 'show_mentors'},
                      {'option_name': 'Display applicants table', 'query': 'show_applicants'},
                      {'option_name': 'Custom query', 'query': 'custom_query'}]

adv_menu_options = [{'option_name': 'Mentors and schools', 'query': 'mentors'},
                    {'option_name': 'All schools', 'query': 'all_school'},
                    {'option_name': 'Contacts (Mentors by country)', 'query': 'mentors_by_country'},
                    {'option_name': 'Contacts', 'query': 'contacts'},
                    {'option_name': 'Applicants page', 'query': 'applicants'},
                    {'option_name': 'Applicants and mentors', 'query': 'applicants-and-mentors'}]


@app.route("/", methods=['GET'])
def index():
    '''Renders template for the main page, where the user can choose a query to display'''
    global basic_menu_options
    response = make_response(render_template('top_nav_bar.html',
                                             basic_menu_options=basic_menu_options,
                                             adv_menu_options=adv_menu_options))
    response.set_cookie('table', '', expires=0)
    response.set_cookie('columns', '', expires=0)
    response.set_cookie('filter', '', expires=0)
    response.set_cookie('order_by', '', expires=0)
    return response


@app.route("/queries/<query>", methods=['GET'])
def display_query(query):
    function_to_call = getattr(queries, query)
    query_result = function_to_call()
    return render_template('list.html', query_result=query_result,
                           basic_menu_options=basic_menu_options,
                           adv_menu_options=adv_menu_options)


@app.route("/queries/custom_query", methods=['GET'])
def custom_query():
    response = None

    query = {'table': None,
             'columns': None,
             'filter': None,
             'order_by': None,
             'method': 'GET'}

    query = helpers.read_qry_from_cookies()

    if None not in query.values():
        query_result = queries.custom_query(query)
        return render_template('list.html', query_result=query_result,
                               basic_menu_options=basic_menu_options,
                               adv_menu_options=adv_menu_options)

    if request.args.get('table') is not None:
        query['table'] = request.args.get('table')
        response = make_response(redirect('/queries/custom_query'))
        response.set_cookie('table', request.args.get('table'))
        return response

    if request.args.getlist('columns') != []:
        query['columns'] = ', '.join(request.args.getlist('columns'))
        response = make_response(redirect('/queries/custom_query'))
        response.set_cookie('columns', query['columns'])
        return response

    if request.args.get('column_to_search') is not None:
        if request.args.get('search_pos') == 'start':
            where_statement = (request.args.get('column_to_search') + " LIKE '" +
                               str(request.args.get('keyword')) + "%'")
        if request.args.get('search_pos') == 'mid':
            where_statement = (request.args.get('column_to_search') + " LIKE " +
                               "'%" + str(request.args.get('keyword')) + "%'")
        if request.args.get('search_pos') == 'end':
            where_statement = (request.args.get('column_to_search') + " LIKE " +
                               "'%" + str(request.args.get('keyword')) + "'")
        if request.args.get('search_pos') == 'exact':
            where_statement = (request.args.get('column_to_search') + " = " +
                               "'" + str(request.args.get('keyword')) + "'")
        query['filter'] = where_statement
        response = make_response(redirect('/queries/custom_query'))
        response.set_cookie('filter', where_statement)
        return response

    if request.args.get('column_to_order_by') is not None:
        order_by = request.args.get('column_to_order_by')
        if request.args.get('sort_order') == 'asc':
            order_by += ' ASC'
        if request.args.get('sort_order') == 'desc':
            order_by += ' DESC'
        query['order_by'] = order_by
        response = make_response(redirect('/queries/custom_query'))
        response.set_cookie('order_by', order_by)
        return response

    response = make_response(render_template('custom_query.html', query=query,
                             basic_menu_options=basic_menu_options,
                             adv_menu_options=adv_menu_options))
    return response


if __name__ == '__main__':
    app.run(debug=True)
