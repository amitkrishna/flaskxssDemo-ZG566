from flask import Flask, render_template, request, make_response
import db
import logger

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])
        logger.info(request.form['comment'])

    search_query = request.args.get('q')
    logger.info(search_query)

    comments = db.get_comments(search_query)
    logger.info(comment)
    response = make_response(
        render_template('index.html', comments=comments, search_query=search_query)
        )
    logger.info(response)
    response.set_cookie("cookieInfo", "some sensitive data")
    logger.info()
    # response.headers.set('Content-Security-Policy', "script-src 'none'")
    return response
