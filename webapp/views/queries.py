"""Views for database view models (read-only)."""

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from models.queries import (
    ForestSpecies,
    InvasiveSpecies,
    NumberSpeciesInEachCounty,
    RockinghamCounty,
)



class RockinghamCountyView(ModelView):
    datamodel = SQLAInterface(RockinghamCounty)
    route_base = '/rockinghamcounty'
    list_title = 'Rockingham County Species'
    list_columns = ['common_name', 'scientific_name', 'category', 'name']
    base_permissions = ['can_list']
    base_filters = []
    can_add = False
    can_edit = False
    can_delete = False
    can_show = False  # Disable detail view since views don't support single row lookups well


class NumberSpeciesInEachCountyView(ModelView):
    datamodel = SQLAInterface(NumberSpeciesInEachCounty)
    route_base = '/numberspeciesineachcounty'
    list_title = 'Species Count by County'
    list_columns = ['county', 'species_count']
    base_permissions = ['can_list']
    base_filters = []
    can_add = False
    can_edit = False
    can_delete = False
    can_show = False


class ForestSpeciesView(ModelView):
    datamodel = SQLAInterface(ForestSpecies)
    route_base = '/forestspecies'
    list_title = 'Forest Species'
    list_columns = ['common_name', 'scientific_name', 'category']
    base_permissions = ['can_list']
    base_filters = []
    can_add = False
    can_edit = False
    can_delete = False
    can_show = False


class InvasiveSpeciesView(ModelView):
    datamodel = SQLAInterface(InvasiveSpecies)
    route_base = '/invasivespecies'
    list_title = 'Invasive Species'
    list_columns = ['common_name', 'scientific_name', 'category']
    base_permissions = ['can_list']
    base_filters = []
    can_add = False
    can_edit = False
    can_delete = False
    can_show = False

