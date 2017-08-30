
# Logs Analysis Project

By Ryan Meyers


## About

This is the first project in the section "The Backend" in the Udacity course for Fullstack Web Development.


## To Run

### You will need:

* Python 2.7
* Vagrant
* VirtualBox


### Setup

1. Install Vagrant And VirtualBox
2. Clone this repository


### To Run

Launch Vagrant VM by running vagrant up, you can the log in with vagrant ssh

To load the data, use the command psql -d news -f newsdata.sql to connect a database and run the necessary SQL statements.

The database includes three tables:

* Authors table
* Articles table
* Log table

To execute the program, run python run.py from the command line.
