"""Flask-AppBuilder views that provide CRUD web interfaces for database tables."""

from flask import flash, redirect
from datetime import datetime
from flask_appbuilder import expose
from flask_appbuilder.security.decorators import has_access
from flask_appbuilder import ModelView
from flask_appbuilder.actions import action
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_login import current_user
from models.tables import (
    Comment,
    County,
    Habitat,
    LikedObservation,
    Media,
    Observation,
    Specialty,
    Species,
    Userr,
)
from .forms import CommentForm, insert_comment
from flask import request


class CommentView(ModelView):
    datamodel = SQLAInterface(Comment)
    route_base = '/comment'
    list_title = 'Comments'
    list_columns = ['comment_id', 'user_id', 'observation_date_time', 'observation_species_observed', 'observation_observer_id', 'comment_text', 'time_stamp']


class CountyView(ModelView):
    datamodel = SQLAInterface(County)
    route_base = '/county'
    list_title = 'Counties'
    list_columns = ['county_id', 'state', 'name', 'region']


class HabitatView(ModelView):
    datamodel = SQLAInterface(Habitat)
    route_base = '/habitat'
    list_title = 'Habitats'
    list_columns = ['species_id', 'habitat']


class MediaView(ModelView):
    datamodel = SQLAInterface(Media)
    route_base = '/media'
    list_title = 'Media'
    list_columns = ['media_id', 'media_date_time', 'media_species_observed', 'media_observer_id', 'media_type', 'media_URL', 'description']


class ObservationView(ModelView):
    datamodel = SQLAInterface(Observation)
    route_base = '/observation'
    list_title = 'Observations'
    list_columns = ['date_time', 'species_observed', 'observer_id', 'county_id', 'observation_type', 'notes', 'status']

    @action("myaction", "Like Observation", "Are you sure?", "fa-heart")
    def send_email(self, items):
        """Action to like observations and save them to the database."""
        if not isinstance(items, list):
            items = [items]
        
        if not current_user.is_authenticated:
            flash("You must be logged in to like observations.", "warning")
            return redirect(self.get_redirect())
        
        liked_count = 0
        already_liked_count = 0
        
        for item in items:
            # Check if already liked
            existing_like = (
                self.datamodel.session.query(LikedObservation)
                .filter_by(
                    user_id=current_user.id,
                    observation_date_time=item.date_time,
                    observation_species_observed=item.species_observed,
                    observation_observer_id=item.observer_id
                )
                .first()
            )
            
            if not existing_like:
                # Create new like
                like = LikedObservation(
                    user_id=current_user.id,
                    observation_date_time=item.date_time,
                    observation_species_observed=item.species_observed,
                    observation_observer_id=item.observer_id,
                    liked_at=datetime.now()
                )
                self.datamodel.session.add(like)
                liked_count += 1
            else:
                already_liked_count += 1
        
        self.datamodel.session.commit()
        
        if liked_count > 0:
            flash(f"{liked_count} observation(s) liked!", "success")
        if already_liked_count > 0:
            flash(f"{already_liked_count} observation(s) were already liked.", "info")
        
        return redirect(self.get_redirect())
    
    @action("confirm", "Confirm Observation", "Mark selected observations as confirmed?", "fa-check-circle")
    def confirm_observation(self, items):
        """Action to mark observations as confirmed."""
        if not isinstance(items, list):
            items = [items]
        
        confirmed_count = 0
        for item in items:
            item.status = "Confirmed"
            self.datamodel.session.merge(item)
            confirmed_count += 1
        
        self.datamodel.session.commit()
        flash(f"{confirmed_count} observation(s) marked as confirmed!", "success")
        return redirect(self.get_redirect())
    
    @expose("/show/<date_time>/<species_observed>/<observer_id>", methods=["GET", "POST"])
    def show_observation(self, date_time, species_observed, observer_id):
        from app import db, app
        from models.tables import Comment, Observation, Species

        try:
            # Convert from ISO string (with 'T') to datetime
            parsed_date = datetime.fromisoformat(date_time)
        except ValueError:
            flash("Invalid date format in URL", "danger")
            return redirect(self.get_redirect())

        obs = (
            self.datamodel.session.query(Observation)
            .filter_by(
                date_time=parsed_date,
                species_observed=int(species_observed),
                observer_id=int(observer_id),
            )
            .first()
        )

        if not obs:
            flash("Observation not found", "danger")
            return redirect(self.get_redirect())

        comments = (
            db.session.query(Comment)
            .filter(obs.date_time == Comment.observation_date_time,
                    obs.species_observed == Comment.observation_species_observed,
                    obs.observer_id == Comment.observation_observer_id)
        )

        species = (
            db.session.query(Species)
            .filter(obs.species_observed == Species.species_id)
            .first()
        )

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

        return self.render_template(
            "observation_detail.jinja",
            observation=obs,
            comments=comments,
            species=species,
            form=form
        )


class SpecialtyView(ModelView):
    datamodel = SQLAInterface(Specialty)
    route_base = '/specialty'
    list_title = 'Specialties'
    list_columns = ['specialty_id', 'admin_specialty']


class SpeciesView(ModelView):
    datamodel = SQLAInterface(Species)
    route_base = '/species'
    list_title = 'Species'
    list_columns = ['species_id', 'common_name', 'scientific_name', 'category', 'conservation_status', 'description']

    # show_template = 'species_show.html'
    @expose('/show/<pk>')
    @has_access
    def show(self, pk):
        """
        Direct show page for a single species.
        """
        from app import db

        species = db.session.get(Species, pk)
        if not species:
            return self.show_error_message(f"Species with id {pk} not found.")

        return self.render_template('species_show.html', item=species, model=species)

class UserrView(ModelView):
    datamodel = SQLAInterface(Userr)
    route_base = '/user'
    list_title = 'Users'
    list_columns = ['user_id', 'name', 'permission_level', 'email']
