from flask import Flask, render_template, jsonify
from data.news import News
from data.jobs import Jobs
from data import db_session, news_api
from data.users import User
from form.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init("db/mars_explorer.db")


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(news_api.blueprint)
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs)
    return render_template("index.html", job=job)

@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surmame=form.name.data,
            age=form.name.data,
            position=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
    return render_template('register.html', title='Регистрация', form=form)

import flask

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)

if __name__ == '__main__':
    main()
