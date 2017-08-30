# This code is used running Python version 2.7

import psycopg2
from datetime import datetime as dt

# 1. What are the most popular three articles of all time?
# Which articles have been accessed the most? Present this
# information as a sorted list with the most popular article
# at the top.

command1 = (
    "SELECT articles.title, COUNT(*) AS views "
    "FROM articles INNER JOIN log ON log.path "
    "LIKE concat('%', articles.slug, '%') "
    "WHERE log.status LIKE '%200%' GROUP BY "
    "articles.title, log.path ORDER BY views DESC LIMIT 3")

# 2. Who are the most popular article authors of all time?
# That is, when you sum up all of the articles each author
# has written, which authors get the most page views? Present
# this as a sorted list with the most popular author at the top.

command2 = (
    "SELECT authors.name, COUNT(*) AS views "
    "FROM articles INNER JOIN authors ON "
    "articles.author = authors.id INNER JOIN log "
    "ON log.path LIKE concat('%', articles.slug, '%') WHERE "
    "log.status LIKE '%200%' GROUP "
    "BY authors.name ORDER BY views DESC")

# 3. On which days did more than 1% of requests lead to errors?
# The log table includes a column status that indicates the HTTP
# status code that the news site sent to the user's browser.

command3 = (
    "SELECT day, perc FROM ("
    "SELECT day, round((sum(requests)/(SELECT COUNT(*) FROM log WHERE "
    "substring(cast(log.time AS text), 0, 11) = day) * 100), 2) AS "
    "perc FROM (SELECT substring(cast(log.time as text), 0, 11) AS day, "
    "COUNT(*) AS requests FROM log WHERE status LIKE '%404%' GROUP BY day)"
    "AS log_percentage GROUP BY day ORDER BY perc DESC) AS final_query "
    "WHERE perc >= 1")


def run_query(command):
    conn = psycopg2.connect("dbname=news")
    cur = conn.cursor()

    cur.execute(command)

    return cur.fetchall()

    conn.close()


if __name__ == '__main__':
    request1 = run_query(command1)
    num1 = str(request1[0][1])
    num2 = str(request1[1][1])
    num3 = str(request1[2][1])
    print "The three most popular articles of all time are: \n1. " +\
        request1[0][0] + " - " + num1 + "views\n2. " + request1[1][0] + \
        " - " + num2 + "views, and \n3. " + request1[2][0] + " - " + \
        num3 + "views"

    request2 = run_query(command2)
    num1 = str(request2[0][1])
    num2 = str(request2[1][1])
    num3 = str(request2[2][1])
    print "\nThe three most popular article authors of all time are: \n1. " +\
        request2[0][0] + " - " + num1 + "views\n2. " + request2[1][0] +\
        " - " + num2 + "views, and \n3. " + request2[2][0] + " - " + num3 +\
        "views"

    request3 = run_query(command3)
    date = request3[0][0]
    date_object = dt.strptime(date, '%Y-%m-%d')
    percentage = str(request3[0][1])
    print "\nDays with more than 1% of requests leading to errors: \n" + \
        date_object.strftime("%d %B %Y") + " - " + percentage + "%"
