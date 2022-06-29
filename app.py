from flask import Flask, request, render_template,  redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


connect_db(app)

############################################################################################################################################

@app.route('/')
def home_page():
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_new_pet(): 
    # print(request.form)
    # when we create a new instance of AddSnackForm, we'll see that the request will store all the form data. 
    form = AddPetForm()
    
    # adds selection to first_name Selection on our form
    # pets = [(u.name) for u in Pet.query.all()]
    # form.name.choices = pets


    # is this a post request, AND is the CSRF token valid? if we submit a GET request, else will run.
    # this method also fills the form object above with data from the POST request (from  request.form), configured through forms.py.
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet=Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        flash(f"Created new pet: name is {name}, species is ${species}")
        return redirect('/')
   
    else: 
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        return redirect('/')
   
    else: 
        return render_template("pet_detail.html", pet=pet, form=form)