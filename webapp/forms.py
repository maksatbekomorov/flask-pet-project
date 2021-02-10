from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField
from wtforms.validators import Required


class Table(FlaskForm):
    table_name = TextField('Ім\'я таблиці', validators=[Required()])
    table_rows = IntegerField('Кількість записів', validators=[Required()])
