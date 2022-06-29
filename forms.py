from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField, SelectField
# see http://wtforms.readthedocs.io/en/latest/validators.html
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet's name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Species", validators=[InputRequired(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    available = SelectField("Available?", choices=[("Yes", "No")])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )
    available = SelectField("Available?", choices=[("Yes", "No")])