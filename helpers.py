from flask import Flask, request


def read_qry_from_cookies():
    '''Tries to read the saved parameters of a custom query from cookies, returns the dict of query parameters'''
    query = {'table': None,
             'columns': None,
             'filter': None,
             'order_by': None,
             'method': 'GET'}
    query['table'] = request.cookies.get('table')
    query['columns'] = request.cookies.get('columns')

    if query['columns'] is not None:
        query['columns'] = query['columns'].split(', ')

    query['filter'] = request.cookies.get('filter')
    query['order_by'] = request.cookies.get('order_by')
    return query


def parse_column_names(list_of_column_names):
    '''Receives the list of chosen column names that are to be displayed, returns 1 string that is
    ready to be inserted into an sql query.'''
    pass