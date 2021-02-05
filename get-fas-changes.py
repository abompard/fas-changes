#!/usr/bin/env python2
# vim: set et ts=4 sw=4:

from argparse import ArgumentParser
from datetime import datetime

import psycopg2


DB_NAME = ""
DB_HOST = ""
DB_USER = ""
DB_PASSWORD = ""


QUERY = """
    SELECT p.username, l.description, l.changetime
    FROM log l JOIN people p ON l.author_id = p.id
    WHERE l.changetime >= %s
    ORDER BY l.changetime DESC
"""


parser = ArgumentParser()
parser.add_argument("since", type=int)
args = parser.parse_args()

since = datetime.fromtimestamp(args.since)

users = []
with psycopg2.connect(dbname=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASSWORD) as conn:
    with conn.cursor() as cur:
        cur.execute(QUERY, (since,))
        for row in cur:
            #print(row)
            user = row[0]
            if user not in users:
                users.append(user)

print(" ".join(users))
