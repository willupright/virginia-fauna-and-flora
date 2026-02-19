"""Flask-AppBuilder menu configuration for Virginia Flora and Fauna Database."""

# See https://fontawesome.com/icons for icon names.

from views.base import AboutView, CountySpeciesView, LikedObservationsView, ObservationsListView
from views.charts import (
    Species_By_Category,
    Species_By_Habitat
)
from views.queries import (
    ForestSpeciesView,
    InvasiveSpeciesView,
    NumberSpeciesInEachCountyView,
    RockinghamCountyView,
)
from views.tables import (
    CommentView,
    CountyView,
    HabitatView,
    MediaView,
    ObservationView,
    SpecialtyView,
    SpeciesView,
    UserrView,
)

from views.forms import (
    ObservationFormView,
    CommentFormView,
    UserFormView
)


def setup_menu(appbuilder):

    # --------------------------------------------------------------------------
    # Tables Menu (Admin - in an order that makes sense for the GUI)
    # --------------------------------------------------------------------------

    appbuilder.add_view(
        SpeciesView,
        "Species",
        icon="fa-leaf",
        category="Admin",
        category_icon="fa-database",
    )

    appbuilder.add_view(
        CountyView,
        "Counties",
        icon="fa-map-marker-alt",
        category="Admin",
    )

    appbuilder.add_separator("Admin")

    appbuilder.add_view(
        ObservationView,
        "Observations",
        icon="fa-binoculars",
        category="Admin",
    )

    appbuilder.add_view(
        HabitatView,
        "Habitats",
        icon="fa-tree",
        category="Admin",
    )

    appbuilder.add_view(
        MediaView,
        "Media",
        icon="fa-image",
        category="Admin",
    )

    appbuilder.add_view(
        CommentView,
        "Comments",
        icon="fa-comment",
        category="Admin",
    )

    appbuilder.add_separator("Admin")

    appbuilder.add_view(
        UserrView,
        "Users",
        icon="fa-users",
        category="Admin",
    )

    appbuilder.add_view(
        SpecialtyView,
        "Specialties",
        icon="fa-certificate",
        category="Admin",
    )

    # --------------------------------------------------------------------------
    # Views Menu (Database Views - read-only)
    # --------------------------------------------------------------------------

    appbuilder.add_view(
        RockinghamCountyView,
        "Rockingham County",
        icon="fa-map",
        category="Views",
        category_icon="fa-eye",
    )

    appbuilder.add_view(
        NumberSpeciesInEachCountyView,
        "Species by County",
        icon="fa-bar-chart",
        category="Views",
    )

    appbuilder.add_view(
        ForestSpeciesView,
        "Forest Species",
        icon="fa-tree",
        category="Views",
    )

    appbuilder.add_view(
        InvasiveSpeciesView,
        "Invasive Species",
        icon="fa-exclamation-triangle",
        category="Views",
    )

    appbuilder.add_view_no_menu(ObservationsListView())

    appbuilder.add_view(
        LikedObservationsView,
        "My Liked Observations",
        icon="fa-heart",
        category="Views"
    )


    # --------------------------------------------------------------------------
    # Charts Menu (Data Visualizations)
    # --------------------------------------------------------------------------

    appbuilder.add_view(
        Species_By_Category,
        "Species by Category",
        icon="fa-pie-chart",
        category="Charts",
        category_icon="fa-chart-pie",
    )

    appbuilder.add_view(
        Species_By_Habitat,
        "Species by Habitat",
        icon="fa-pie-chart",
        category="Charts"
    )


    # --------------------------------------------------------------------------
    # Custom Views (not in the menu - accessed via URL)
    # --------------------------------------------------------------------------

    appbuilder.add_view_no_menu(CountySpeciesView())
    appbuilder.add_view_no_menu(AboutView())


    #form view
    appbuilder.add_view(
        ObservationFormView,
        "Submit Observation",
        icon="fa-plus-circle",
        category="Admin"
    )

    appbuilder.add_view(
        UserFormView,
        "Add User",
        icon="fa-user-plus",
        category="Admin"
    )

    appbuilder.add_view_no_menu(CommentFormView)



