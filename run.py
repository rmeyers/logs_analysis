#!/usr/bin/env python
# This code is used running Python version 2.7

import psycopg2
from datetime import datetime as dt

# 1. What are the most popular three articles of all time?
# Which articles have been accessed the most? Present this
# information as a sorted list with the most popular article
# at the top.

command1 = (
    """SELECT articles.title, COUNT(*) AS views
    FROM articles INNER JOIN log
    ON log.path = '/article/' || articles.slug
    WHERE log.status LIKE '%200%'
    GROUP BY articles.title, log.path
    ORDER BY views DESC
    LIMIT 3""")

# 2. Who are the most popular article authors of all time?
# That is, when you sum up all of the articles each author
# has written, which authors get the most page views? Present
# this as a sorted list with the most popular author at the top.

command2 = (
    """SELECT authors.name, COUNT(*) AS views
    FROM articles INNER JOIN authors
    ON articles.author = authors.id INNER JOIN log
    ON log.path = '/article/' || articles.slug
    WHERE log.status LIKE '%200%' GROUP
    BY authors.name ORDER BY views DESC""")

# 3. On which days did more than 1% of requests lead to errors?
# The log table includes a column status that indicates the HTTP
# status code that the news site sent to the user's browser.

command3 = (
    """SELECT day, perc FROM (
    SELECT day, round((sum(requests)/(SELECT COUNT(*)
    FROM log
    WHERE substring(cast(log.time AS text), 0, 11) = day) * 100), 2) AS perc
    FROM (SELECT substring(cast(log.time as text), 0, 11) AS day, COUNT(*)
    AS requests FROM log WHERE status
    LIKE '%404%' GROUP BY day)
    AS log_percentage GROUP BY day
    ORDER BY perc DESC) AS final_query
    WHERE perc >= 1""")

# command4 = (
#     """SELECT date, errors/requests
#     WHERE errors/requests >= 0.01
#     (FROM SELECT time::date AS date, count(*) AS errors
#     FROM log
#     WHERE status = '404 NOT FOUND'
#     GROUP BY date) AND
#     (SELECT time::date AS date, count(*) AS requests
#     FROM log
#     GROUP BY date;
#     """)


def run_query(command):
    ''' This runs the query on the 'news' database, fetches all
    results, and closes the DB connection. '''
    try:
        conn = psycopg2.connect("dbname=news")
    except psycopg2.Error as e:
        print "Error: ", e
        return "Unable to connect to the database."
    cur = conn.cursor()
    cur.execute(command)
    results = cur.fetchall()
    conn.close()

    return results

if __name__ == '__main__':
    request1 = run_query(command1)
    print("The three most popular articles of all time are: ")
    print("-" * 15)
    for result in request1:
        print("\"{}\" - {} views".format(result[0], result[1]))

    request2 = run_query(command2)
    print("\nThe three most popular article authors of all time are: ")
    print("-" * 15)
    for result in request2:
        print("{} - {} views".format(result[0], result[1]))

    request3 = run_query(command3)
    print("\nDays with more than 1% of requests leading to errors: ")
    print("-" * 15)
    for result in request3:
        date = result[0]
        date_object = dt.strptime(date, '%Y-%m-%d')
        percentage = str(result[1])
        print("{} - {}%").format(date_object.strftime("%d %B %Y"), percentage)

    # request4 = run_query(command4)
    # print request4




