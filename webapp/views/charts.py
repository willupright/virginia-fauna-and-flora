"""Chart views that visualize complex database queries."""

from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface
from models.tables import Species, Habitat


class Species_By_Category(GroupByChartView):
    datamodel = SQLAInterface(Species)
    chart_title = "Species by Category"
    definitions = [
        {
            "group": "category",
            "series": [(aggregate_count, "common_name")]
        },
        # can add other groupings
    ]


class Species_By_Habitat(GroupByChartView):
    datamodel = SQLAInterface(Habitat)
    chart_title = "Species by Habitat"
    definitions = [
        {
            "group": "habitat",
            "series": [(aggregate_count, "species_id")]
        }
    ]
