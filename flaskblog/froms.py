#-*- coding: utf-8 -*-
##表单
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,TextField
from wtforms.validators import Required,Email,Length,DataRequired

class NameForm(FlaskForm):
    name = StringField('用户名', validators=[Required()],render_kw={"placeholder":"请输入用户名"})
    password = PasswordField('密码', validators=[Required()],render_kw={"placeholder":"请输入密码"})
    email = StringField('邮箱',validators=[Email()],render_kw={"placeholder":"请输入邮箱"})
    submit = SubmitField('登录')


class CommentForm(FlaskForm):
    """Form vaildator for comment."""

    # Set some field(InputBox) for enter the data.
    # patam validators: setup list of validators
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)])

    text = TextField(u'Comment', validators=[DataRequired()])