from flask import Flask, render_template, request, make_response
import db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    search_query = request.args.get('q')

    comments = db.get_comments(search_query)
    response = make_response(
        render_template('index.html', comments=comments, search_query=search_query)
        )
    response.set_cookie("cookieInfo", "some sensitive data")
    # response.headers.set('Content-Security-Policy', "script-src 'none'")
    return response
