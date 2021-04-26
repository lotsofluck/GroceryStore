from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=80)])
    address = TextAreaField('Address', validators=[DataRequired(), Length(min=3, max=300)])
    submit = SubmitField('Submit')
    

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=300)])
    price = FloatField('Price', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired(), Length(min=1, max=80)])
    photo_url = StringField('Photo url', validators=[DataRequired(), URL()])
    store = QuerySelectField('store', query_factory=lambda: GroceryStore.query, allow_blank=False)
    submit = SubmitField('Submit')
