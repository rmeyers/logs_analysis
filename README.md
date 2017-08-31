
# Logs Analysis Project

By Ryan Meyers


## About

This is the first project in the section "The Backend" in the Udacity course for Fullstack Web Development.
The script in run.py uses psycopg2 to query a mock PostgreSQL database for a fictional news website.
The news database contains three tables, articles, authors, and log. Using these tables, the script in run.py
answers the following three questions:

1. What are the most popular three articles of all time?
Which articles have been accessed the most? Present this
information as a sorted list with the most popular article
at the top.
2. Who are the most popular article authors of all time?
That is, when you sum up all of the articles each author
has written, which authors get the most page views? Present
this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors?
The log table includes a column status that indicates the HTTP
status code that the news site sent to the user's browser.

## To Run

### You will need:

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)


### Setup

1. Install Vagrant And VirtualBox
2. [Clone this repository](https://github.com/rmeyers/logs_analysis.git)


### To Run

Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

The database can be downloaded [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

The database includes three tables:

* Authors table
* Articles table
* Log table

To execute the program, run `python run.py` from the command line.
