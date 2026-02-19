from flask import flash, redirect
from flask_appbuilder import SimpleFormView
from wtforms import StringField, SelectField, TextAreaField, DateTimeField, IntegerField
from wtforms.validators import InputRequired, Length, Email, NumberRange, URL, Optional
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget
from flask_appbuilder.security.sqla.models import User
from flask_login import current_user
import psycopg
import socket
from datetime import datetime
from models.tables import County
from flask import request
from flask_appbuilder import expose


# --- Database connection setup ---
try:
    socket.gethostbyname("data.cs.jmu.edu")
    DSN = "host=data.cs.jmu.edu user=team27 dbname=team27"
except:
    DSN = "host=localhost user=team27 dbname=team27"


# insert observation from form
def insert_observation(date_time, species_observed, observer_id, county_id, observation_type, notes, status):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO observation
                (date_time, species_observed, observer_id, county_id, observation_type, notes, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (date_time, species_observed, observer_id, county_id, observation_type, notes, status),
            )
            conn.commit()
            return True

# insert media from observation form        
def insert_media(date_time, species_id, observer_id, media_type, media_url, description):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO media
                (media_date_time, media_species_observed, media_observer_id, media_type, "media_URL", description)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (date_time, species_id, observer_id, media_type, media_url, description),
            )
            conn.commit()
            return True

# insert comment
def insert_comment(user_id, observation_date_time, observation_species_observed, observation_observer_id, comment_text, time_stamp):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO comment
                (user_id, observation_date_time, observation_species_observed, observation_observer_id, comment_text, time_stamp)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (user_id, observation_date_time, observation_species_observed, observation_observer_id, comment_text, time_stamp),
            )
            conn.commit()
            return True

# insert user
def insert_user(user_id, name, permission_level, email):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO "user"
                (user_id, name, permission_level, email)
                VALUES (%s, %s, %s, %s)
                """,
                (user_id, name, permission_level, email),
            )
            conn.commit()
            return True

# observation Form
class ObservationForm(DynamicForm):
    f_species_name = SelectField(
        "Species Observed",
        description="Select the species observed.",
        validators=[InputRequired()],
        choices=[],
        widget=Select2Widget(),
    )

    f_observer_name = StringField(
        "Observer Name",
        description="Enter your full name (as in the system).",
        validators=[InputRequired()],
        widget=BS3TextFieldWidget(),
    )

    f_county_name = SelectField(
        "County",
        validators=[InputRequired()],
        choices=[],
        widget=Select2Widget(),
    )

    f_type = SelectField(
        "Observation Type",
        validators=[InputRequired()],
        choices=[
            ("Private", "Private"),
            ("Public", "Public"),
            ("Research", "Research"),
        ],
        widget=Select2Widget(),
        default="Private",
    )

    f_media_url = TextAreaField(
        "Media URL",
        description="Optional: add any relevant media.",
        validators=[Optional(), Length(max=500), URL(require_tld=False)],
        widget=BS3TextFieldWidget(),
    )

    f_media_type = TextAreaField(
        "Media Type",
        description="Optional: describe the type media.",
        validators=[Length(max=500)],
        widget=BS3TextFieldWidget(),
    )

    f_media_description = TextAreaField(
        "Media Description",
        description="Optional: describe the media.",
        validators=[Length(max=500)],
        widget=BS3TextFieldWidget(),
    )

    f_notes = TextAreaField(
        "Notes",
        description="Optional: add any relevant notes.",
        validators=[Length(max=500)],
        widget=BS3TextFieldWidget(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # get counties from database
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT county_id, name FROM county ORDER BY name')
                self.f_county_name.choices = [(row[1], row[1]) for row in cur.fetchall()]

        # get species names from database
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT species_id, common_name FROM species ORDER BY common_name')
                self.f_species_name.choices = [(row[1], row[1]) for row in cur.fetchall()]


class CommentForm(DynamicForm):
    f_comment_text = TextAreaField("Comment", validators=[InputRequired(), Length(max=500)], widget=BS3TextFieldWidget())

    def __init__(self, date_time, species_observed, observer_id, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT date_time, species_observed, observer_id FROM observation "
                    "WHERE date_time = %s AND species_observed = %s AND observer_id = %s",
                    (date_time, species_observed, observer_id)
                )
                row = cur.fetchone()
                if row:
                    self.observation_date_time = row[0]
                    self.observation_species_id = row[1]
                    self.observation_observer_id = row[2]
                else:
                    raise ValueError("Observation not found")
        

# form View 
class ObservationFormView(SimpleFormView):
    route_base = "/add_observation"
    form = ObservationForm
    form_title = "Add a New Observation"

    def form_post(self, form):
        # find observer id
        observer_name = form.f_observer_name.data.strip()
        observer_id = None
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT user_id FROM "user" WHERE name = %s', (observer_name,))
                row = cur.fetchone()
                if row:
                    observer_id = row[0]
                else:
                    flash(f"Error: No user found with name '{observer_name}'.", "danger")
                    return self.this_form_get()

        # find county id
        county_name = form.f_county_name.data
        county_id = None
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT county_id FROM county WHERE name = %s', (county_name,))
                row = cur.fetchone()
                if row:
                    county_id = row[0]
                else:
                    flash(f"Error: No county found with name '{county_name}'.", "danger")
                    return self.this_form_get()

        # find species id
        species_name = form.f_species_name.data
        species_id = None
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT species_id FROM species WHERE common_name = %s', (species_name,))
                row = cur.fetchone()
                if row:
                    species_id = row[0]
                else:
                    flash(f"Error: No species found with name '{species_name}'.", "danger")
                    return self.this_form_get()

        datetime_now = datetime.now()

        insert_observation(
            datetime_now,
            species_id,
            observer_id,
            county_id,
            form.f_type.data,
            form.f_notes.data,
            "Pending"
        )

        media_url = form.f_media_url.data.strip()
        media_type = form.f_media_type.data
        media_description = form.f_media_description.data.strip()

        if media_url:  # only if url is input
            insert_media(
                datetime_now,
                species_id,
                observer_id,
                media_type,
                media_url,
                media_description
            )


        flash(f"Observation of {species_name} added successfully!", "success")
        return self.this_form_get()


class CommentFormView(SimpleFormView):
    route_base = "/add_comment"
    form = CommentForm
    form_title = "Add a New Comment"

    @expose("/form", methods=["GET", "POST"])
    def this_form_get(self):

        from app import db
        from models.tables import Comment, Observation, Species

        date_time = request.args.get("date_time")
        species_observed = request.args.get("species_observed")
        observer_id = request.args.get("observer_id")

        # Create observation to give to the form
        observation = None
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT date_time, species_observed, observer_id, county_id "
                    "FROM observation "
                    "WHERE date_time = %s AND species_observed = %s AND observer_id = %s",
                    (date_time, species_observed, observer_id),
                )
                row = cur.fetchone()
                if row:
                    observation = {
                        "date_time": row[0],
                        "species_observed": row[1],
                        "observer_id": row[2],
                        "county_id": row[3],
                    }
        
        species = (
            db.session.query(Species)
            .filter(observation['species_observed'] == Species.species_id)
            .first()
        )


        # When sending over the form to add_comment, use args from observation_detail to create a comment object
        if request.method == "POST":
            form = CommentForm(date_time, species_observed, observer_id, request.form)
            if form.validate_on_submit():
                user_id = current_user.id
                insert_comment(
                    user_id,
                    form.observation_date_time,
                    form.observation_species_id,
                    form.observation_observer_id,
                    form.f_comment_text.data,
                    datetime.now(),
                )
                flash("Comment added successfully!", "success")
                return redirect(
                    f"/observation/show/{date_time}/{species_observed}/{observer_id}"
                )
        else:
            # GET request (blank form)
            form = CommentForm(date_time, species_observed, observer_id)

        return self.render_template("observation_detail.jinja", form=form, observation=observation, species=species)

    def this_form_post(self, form, date_time, species_observed, observer_id):
        if form.validate_on_submit():
            user_id = current_user.id
            insert_comment(
                user_id,
                form.observation_date_time,
                form.observation_species_id,
                form.observation_observer_id,
                form.f_comment_text.data,
                datetime.now(),
            )
            flash("Comment added successfully!", "success")


class UserForm(DynamicForm):
    f_name = StringField(
        "Name",
        description="Enter the user's full name.",
        validators=[InputRequired(), Length(max=100)],
        widget=BS3TextFieldWidget(),
    )

    f_email = StringField(
        "Email",
        description="Enter the user's email address.",
        validators=[InputRequired(), Email(), Length(max=100)],
        widget=BS3TextFieldWidget(),
    )

    f_permission_level = SelectField(
        "Permission Level",
        description="Select the user's permission level.",
        validators=[InputRequired()],
        choices=[
            (1, "Public (1)"),
            (2, "Researcher (2)"),
            (3, "Admin (3)"),
        ],
        widget=Select2Widget(),
        coerce=int,
    )


class UserFormView(SimpleFormView):
    route_base = "/add_user"
    form = UserForm
    form_title = "Add a New User"

    def form_post(self, form):
        # Get the next available user_id
        user_id = None
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT COALESCE(MAX(user_id), 0) + 1 FROM "user"')
                row = cur.fetchone()
                if row:
                    user_id = row[0]

        if not user_id:
            flash("Error: Could not generate user ID.", "danger")
            return self.this_form_get()

        # Check if email already exists
        email = form.f_email.data.strip()
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT user_id FROM "user" WHERE email = %s', (email,))
                row = cur.fetchone()
                if row:
                    flash(f"Error: A user with email '{email}' already exists.", "danger")
                    return self.this_form_get()

        # Insert the new user
        insert_user(
            user_id,
            form.f_name.data.strip(),
            form.f_permission_level.data,
            email
        )

        flash(f"User '{form.f_name.data}' added successfully with ID {user_id}!", "success")
        return self.this_form_get()
    

