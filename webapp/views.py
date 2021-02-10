from webapp import app
from flask import render_template, request, redirect, url_for, session
'''from .services.checker /
import check_logged_in  /
# добавити декоратор над функціями для перевірки логування!'''
from .models import Users
from .services.form_editor import mass
from .forms import Table
import os
from sqlalchemy import (
                        Table, Column,
                        Integer, Unicode,
                        MetaData, create_engine)
from sqlalchemy.orm import mapper, create_session
from flask import jsonify
from wtforms import TextField, SelectField, IntegerField
from wtforms.validators import Required
from flask_wtf import FlaskForm


@app.route('/')
def test():
    return render_template('login.html')


@app.route('/check_login', methods=['POST'])  # перевірка логіну і паролю
def do_login():
    if request.method == "POST":
        u = Users.query.filter_by(username=request.form['uname']).first()
        if request.form['uname'] == u.username and \
           Users.check_password(u, request.form['psw']):
            session['logged_in'] = True
            return render_template('hello.html', user=u.username)
        return redirect(url_for('test'))  # в url for вписується ім'я функції


@app.route('/create_table', methods=['POST'])
def create_table():  # підготовка даних з форми для запису структури таблиці
    if request.method == "POST":
        d = {}
        f = {}
        x = request.form.to_dict()
        for key, value in x.items():
            if 'csrf' not in key and key != 'submit':
                d[key] = value
                print(key, '->', value)
        for k, v in d.items():
            if 'table_name' in k:
                f.setdefault(k, v)
            elif 'column_name' in k:
                f.setdefault('table_columns', []).append(v)
            elif 'column_type' in k:
                f.setdefault('columns_type', []).append(v)
            elif 'table_rows' in k:
                f.setdefault(k, v)
        # create_pandas_table(f)
        # return f
        print(f)
        return jsonify(x)


def create_pandas_table(dict):  # створення таблиці за допомогою pandas
    from webapp.services.pandasx import table_filling
    x = table_filling(dict)
    from webapp.services.create_engine import write_table
    write_table(x)


# цей метод потрібно видалити, створення через pandas!!!!
def create_table1(dict):  # створення таблиці в базі даних
    class Word(object):
        pass

    wordColumns = dict['table_column']
    e = create_engine(f"sqlite:///{os.path.abspath('test1.db')}")
    metadata = MetaData(bind=e)

    t = Table(dict['table_name'], metadata, Column(
                                                   'id',
                                                   Integer,
                                                   primary_key=True),
              *(Column(wordCol, Unicode(255)) for wordCol in wordColumns))
    metadata.create_all()
    mapper(Word, t)
    session = create_session(bind=e, autocommit=False, autoflush=True)


@app.route('/add', methods=['POST', 'GET'])
def add_row():
    mass.add_element()
    return redirect(url_for("test1"))


@app.route('/delete', methods=['POST', 'GET'])
def del_row():
    mass.del_element()
    return redirect(url_for("test1"))


@app.route('/create', methods=['POST', 'GET'])  # формування динамічної форми
def test1():
    class Table(FlaskForm):
        table_name = TextField('Ім\'я таблиці', validators=[Required()])
        table_rows = IntegerField('Кількість записів', validators=[Required()])
    lst = mass.lst
    for i in lst:
        setattr(Table, i[0], TextField('Ім\'я стовпця', validators=[Required()]))
    for i in lst:
        setattr(Table, i[1], SelectField('Тип сповпця', choices=[('street_address', 'Адреса'), ('name', 'Ім\'я'), ('phone_number', 'Телефон'), ('zipcode', 'Індекс')]))
    form = Table()
    return render_template('test2.html', form=form, lst=lst)


@app.route('/show', methods=['POST', 'GET'])
def show():
    return 'show page'
