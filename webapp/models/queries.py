"""SQLAlchemy model classes for database views (read-only)."""

from typing import Optional

from flask_appbuilder import Model
from sqlalchemy import Integer, PrimaryKeyConstraint, Text
from sqlalchemy.orm import Mapped, mapped_column


# View models for database views
# Note: Views don't have real primary keys, so we use composite keys for uniqueness
class RockinghamCounty(Model):
    __tablename__ = 'rockingham_county'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    common_name: Mapped[str] = mapped_column(Text)
    scientific_name: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(Text)
    name: Mapped[str] = mapped_column(Text)

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name}) in {self.name}"


class NumberSpeciesInEachCounty(Model):
    __tablename__ = 'number_species_in_each_county'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    county: Mapped[str] = mapped_column(Text)
    species_count: Mapped[int] = mapped_column(Integer)

    def __str__(self):
        return f"{self.county}: {self.species_count} species"


class ForestSpecies(Model):
    __tablename__ = 'forest_species'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    common_name: Mapped[str] = mapped_column(Text)
    scientific_name: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(Text)

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name})"


class InvasiveSpecies(Model):
    __tablename__ = 'invasive_species'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    common_name: Mapped[str] = mapped_column(Text)
    scientific_name: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(Text)

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name})"
