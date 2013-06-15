from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_, desc
from coaster.sqlalchemy import TimestampMixin, IdMixin
import os
from recaptcha.client import captcha

# configuration
# DATABASE = '/tmp/flaskr.db'

DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('SETTINGS_FILE', silent=True)

RECAPTCHA_SECRETE = os.environ.get('RECAPTCHA_SECRETE')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('HEROKU_POSTGRESQL_GREEN_URL', 'postgresql://@localhost/ogigante')
db = SQLAlchemy(app)


class Entry(IdMixin, TimestampMixin, db.Model):
    """
    kinds: link, video, evento
    """
    __tablename__ = "entries"
    kind = db.Column(db.String(20), default='link')
    title = db.Column(db.String(200))
    text = db.Column(db.Text)

    approved = db.Column(db.Boolean, default=False)


    def __init__(self, kind, title, text, approved=False):
        self.kind = kind
        self.title = title
        self.text = text
        self.approved = approved

    def __repr__(self):
        return '<Entry [{}] {}>'.format(self.kind, self.title)


@app.route('/')
def index():
    entries = Entry.query.filter_by(approved=True).order_by(desc(Entry.created_at))
    return render_template('index.html', entries=entries)


@app.route('/show_all_entries')
def all_entries():
    entries = Entry.query.order_by(desc(Entry.created_at))
    return render_template('index.html', entries=entries, show_status=True)


@app.route('/eventos')
def events():
    entries = Entry.query.filter_by(kind='evento', approved=True).order_by(desc(Entry.title))
    return render_template('events.html', entries=entries)


@app.route('/novo', methods=['GET', 'POST'])
def new_entry():
    if request.method == 'GET':
        return render_template('new_entry.html')
    else:
        resp = captcha.submit(
            request.form['recaptcha_challenge_field'],
            request.form['recaptcha_response_field'],
            RECAPTCHA_SECRETE,
            request.remote_addr
            )

        if resp.is_valid:
            entry = Entry(request.form['kind'], request.form['title'], request.form['text'])
            db.session.add(entry)
            db.session.commit()
            return render_template('new_entry.html', success=True)
        else:
            return render_template('new_entry.html', fail=True, data=request.form)
        


if __name__ == '__main__':
    app.run()
