from datetime import datetime

import flask
import psycopg2


app = flask.Flask(__name__)
app.config.from_envvar("FLASK_SETTINGS")


QUERY = """
    SELECT p.username, l.description, l.changetime
    FROM log l JOIN people p ON l.author_id = p.id
    WHERE l.changetime >= %s
    ORDER BY l.changetime DESC
"""


@app.route("/")
def root():
    try:
        since_ts = int(flask.request.args.get("since", "0"))
    except (TypeError, ValueError):
        since_ts = 0
    since = datetime.fromtimestamp(since_ts)

    users = []
    with psycopg2.connect(
        dbname=flask.current_app.config.DB_NAME,
        host=flask.current_app.config.DB_HOST,
        user=flask.current_app.config.DB_USER,
        password=flask.current_app.config.DB_PASSWORD,
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(QUERY, (since,))
            for row in cur:
                # print(row)
                user = row[0]
                if user not in users:
                    users.append(user)
    return flask.jsonify(users)


# from werkzeug.middleware.proxy_fix import ProxyFix
# application = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
