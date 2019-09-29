#!/usr/bin/python

import psycopg2
import datetime

# database queries

# query 1: What are the three most popular articles of all time?

request_articles = \
    """select articles.title, count(*) as num
            from log, articles
            where log.status='200 OK'
            and articles.slug = substr(log.path, 10)
            group by articles.title
            order by num desc
            limit 3;"""

# query 2: Who are the most popular article authors of all time?

request_authors = \
    """select authors.name, count(*) as num
            from articles, authors, log
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by num desc;
            """

# query 3: On which day did more than 1% of requests lead to errors?

request_errors = \
    """(select log.time:: date, count(*):: decimal/(select count(*) from log) as num
            from log
            where log.status!='200 OK'
            group by log.time:: date
            order by num desc);
            """

# query data from the database, open and close the connection

def query_db(sql_request):
    conn = psycopg2.connect(database='news')
    cursor = conn.cursor()
    cursor.execute(sql_request)
    results = cursor.fetchall()
    conn.close()
    return results


# write the report

# print title

def print_title(title):
    print '\n\t\t' + title + '\n'


# print answer to question one (1. What are the most popular three articles of all time?)

def top_three_articles():
    top_three_articles = query_db(request_articles)
    print_title('1. What are the most popular three articles of all time?'
                )

    for (title, num) in top_three_articles:
        print ' "{}" -- {} views'.format(title, num)


# print answer to question two (2. Who are the most popular article authors of all time)

def top_three_authors():
    top_three_authors = query_db(request_authors)
    print_title('2. Who are the most popular article authors of all time?'
                )

    for (name, num) in top_three_authors:
        print ' {} -- {} views'.format(name, num)


# print answer to question three (3. On which days did more than one percent of requests lead to errors?)

def high_error_days():
    high_error_days = query_db(request_errors)
    print_title('3. On which days did more than one percent of requests lead to errors?'
                )

    for (time, num) in high_error_days:
        print ' {} -- {} errors'.format(time, num*100)


if __name__ == '__main__':
    top_three_articles()
    top_three_authors()
    high_error_days()
