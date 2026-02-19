"""Initialize the Flask application, database session, and appbuilder object."""

from flask import Flask
from flask_appbuilder import AppBuilder, IndexView
from flask_appbuilder.utils.legacy import get_sqla_class
from menu import setup_menu
from models.tables import County
from flask_appbuilder import expose


class MyIndexView(IndexView):
    index_template = 'index.jinja'
    
    @expose('/')
    def index(self):
        # Get all counties
        counties = db.session.query(County).order_by(County.name).all()
        
        # Pass them to the template
        return self.render_template(
            self.index_template,
            counties=counties
        )


app = Flask(__name__)
app.config.from_object("config")

db = get_sqla_class()()
appbuilder = AppBuilder(indexview=MyIndexView)

with app.app_context():
    db.init_app(app)
    appbuilder.init_app(app, db.session)  # type: ignore
    setup_menu(appbuilder)
    