from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                "Username already exist! Please try a different username"
            )

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(
            email_address=email_address_to_check.data
        ).first()
        if email_address:
            raise ValidationError(
                "Email address already exist! Please try a different email address"
            )

    username = StringField(
        label="Username", validators=[Length(min=5, max=30), DataRequired()]
    )
    email_address = StringField(label="Email", validators=[Email(), DataRequired()])
    password = PasswordField(
        label="Password", validators=[Length(min=6), DataRequired()]
    )
    password_confirm = PasswordField(
        label="Password Confirmation", validators=[EqualTo("password"), DataRequired()]
    )
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Sign In")


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Yes, Purchase this item")


class SellItemForm(FlaskForm):
    submit = SubmitField(label="Yes, Sell this item")