"""Base views that provide custom routes and functionality."""

from flask_appbuilder import BaseView, expose
from flask_appbuilder.security.decorators import has_access
from flask_login import current_user
from markdown import markdown
from pathlib import Path


def md_to_html(filename: str) -> str:
    """Render a markdown file as html."""
    path = Path("templates") / filename
    text = path.read_text(encoding="utf-8")
    return markdown(text, extensions=["attr_list"])


class AboutView(BaseView):
    """View for the about page."""
    route_base = "/about"

    @expose("/")
    def about(self):
        return self.render_template("about.jinja")


class CountySpeciesView(BaseView):
    """View for displaying species by county."""
    route_base = '/species'
    
    @expose("/<county_slug>")
    def by_county(self, county_slug):
        """
        Example URL: /species/bristol
        Query species observed in this county
        """
        # Import here to avoid circular import
        from app import db
        from models.tables import County, Species, t_species_exists
        
        county_name = county_slug.replace("_", " ").title()
        
        county = db.session.query(County).filter(County.name.ilike(f"%{county_name}%")).first()
        if not county:
            return f"County '{county_name}' not found.", 404
        
        species_list = (
            db.session.query(Species)
            .join(t_species_exists, t_species_exists.c.species_id == Species.species_id)
            .filter(t_species_exists.c.county_id == county.county_id)
            .all()
        )

        return self.render_template(
            "county_species.jinja",
            county_name=county.name,
            species_list=species_list
        )

class ObservationsListView(BaseView):
    """View for listing all observations."""
    route_base = '/observations'

    @expose('/')
    def list(self):
        from app import db, app
        from models.tables import Observation, County
        import os

        images_dir = os.path.join(app.static_folder, 'images', 'counties')
        images = sorted([f for f in os.listdir(images_dir) if f.endswith('.png')])

        county_images = []

        for image in images:

            county_name = image.replace('.png', '').replace('_', ' ').title()

            for county in db.session.query(County):
                if county_name == county.name:
                    county_images.append(image)


        return self.render_template(
            'observations.jinja',
            county_images=county_images
        )
    
    @expose("/<county_slug>")
    def by_county(self, county_slug):
        """
        Example URL: /species/bristol
        Query species observed in this county
        """
        from app import db
        from models.tables import Observation, County
        
        county_name = county_slug.replace("_", " ").title()
        
        county = db.session.query(County).filter(County.name.ilike(f"%{county_name}%")).first()
        if not county:
            return f"County '{county_name}' not found.", 404
        
        observations = (
            db.session.query(Observation)
            .filter(county.county_id == Observation.county_id)
            .all()
        )

        return self.render_template(
            'county_observations.jinja',
            county_name=county.name,
            observations=observations
        )


class LikedObservationsView(BaseView):
    """View for displaying observations that the current user has liked."""
    route_base = '/liked_observations'

    @expose('/')
    @has_access
    def list(self):
        """Display all observations liked by the current user."""
        from app import db
        from models.tables import Observation, LikedObservation
        
        if not current_user.is_authenticated:
            return "You must be logged in to view liked observations.", 403
        
        # Get all liked observations for the current user
        liked_observations = (
            db.session.query(Observation)
            .join(
                LikedObservation,
                (LikedObservation.observation_date_time == Observation.date_time) &
                (LikedObservation.observation_species_observed == Observation.species_observed) &
                (LikedObservation.observation_observer_id == Observation.observer_id)
            )
            .filter(LikedObservation.user_id == current_user.id)
            .order_by(LikedObservation.liked_at.desc())
            .all()
        )
        
        return self.render_template(
            'liked_observations.jinja',
            observations=liked_observations
        )



