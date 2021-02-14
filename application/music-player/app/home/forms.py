from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AlbumForm(FlaskForm):    
    name = StringField('Name', validators=[DataRequired()])
    picturelink = StringField('Picture url', validators=[DataRequired()])
    submit = SubmitField('Add Album')
    
class SongForm(FlaskForm):    
    name = StringField('Name', validators=[DataRequired()])
    link = StringField('Embeded link, like https://www.youtube.com/embed/GY9kQcWLvEM ', validators=[DataRequired()])
    submit = SubmitField('Add Song')