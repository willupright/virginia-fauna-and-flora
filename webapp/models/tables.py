"""SQLAlchemy model classes for database tables."""

import datetime
from typing import Optional

from flask_appbuilder import Model
from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, Table, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class County(Model):
    __tablename__ = 'county'
    __table_args__ = (
        PrimaryKeyConstraint('county_id', name='county_pkey'),
    )

    county_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    state: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(Text)
    region: Mapped[Optional[str]] = mapped_column(Text)

    species: Mapped[list['Species']] = relationship('Species', secondary='species_exists', back_populates='counties')
    observations: Mapped[list['Observation']] = relationship('Observation', back_populates='county')

    def __str__(self):
        return f"{self.name}, {self.state or 'Unknown State'} ({self.region or 'Unknown Region'})"
    
    def __repr__(self):
        return self.name or ""


class Specialty(Model):
    __tablename__ = 'specialty'
    __table_args__ = (
        PrimaryKeyConstraint('specialty_id', name='specialty_pkey'),
    )

    specialty_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    admin_specialty: Mapped[Optional[str]] = mapped_column(Text)

    users: Mapped[list['Userr']] = relationship('Userr', secondary='specialized_in', back_populates='specialties')

    def __str__(self):
        return f"Specialty is {self.admin_specialty}"


class Species(Model):
    __tablename__ = 'species'
    __table_args__ = (
        PrimaryKeyConstraint('species_id', name='species_pkey'),
    )

    species_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    common_name: Mapped[Optional[str]] = mapped_column(Text)
    scientific_name: Mapped[Optional[str]] = mapped_column(Text)
    category: Mapped[Optional[str]] = mapped_column(Text)
    conservation_status: Mapped[Optional[str]] = mapped_column(Text)
    description: Mapped[Optional[str]] = mapped_column(Text)

    counties: Mapped[list['County']] = relationship('County', secondary='species_exists', back_populates='species')
    habitat: Mapped[list['Habitat']] = relationship('Habitat', back_populates='species')

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name})"
    
    def __repr__(self):
        return self.common_name or ""


class Userr(Model):
    __tablename__ = 'user'
    __table_args__ = (
        PrimaryKeyConstraint('user_id', name='user_pkey'),
    )

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(Text)
    permission_level: Mapped[Optional[int]] = mapped_column(Integer)
    email: Mapped[Optional[str]] = mapped_column(Text)

    specialties: Mapped[list['Specialty']] = relationship('Specialty', secondary='specialized_in', back_populates='users')
    observations: Mapped[list['Observation']] = relationship('Observation', back_populates='observer')

    def __str__(self):
        return f"{self.name}"


class Habitat(Model):
    __tablename__ = 'habitat'
    __table_args__ = (
        ForeignKeyConstraint(['species_id'], ['species.species_id'], name='habitat_species_id_fkey'),
        PrimaryKeyConstraint('species_id', 'habitat', name='habitat_pkey')
    )

    species_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    habitat: Mapped[str] = mapped_column(Text, primary_key=True)

    species: Mapped['Species'] = relationship('Species', back_populates='habitat')

    def __str__(self):
        return f"Habitat is {self.habitat}"
    
    def __repr__(self):
        return self.habitat or ""


class Observation(Model):
    __tablename__ = 'observation'
    __table_args__ = (
        ForeignKeyConstraint(['county_id'], ['county.county_id'], name='observation_county_id_fkey'),
        ForeignKeyConstraint(['observer_id'], ['user.user_id'], name='observation_observer_id_fkey'),
        PrimaryKeyConstraint('date_time', 'species_observed', 'observer_id', name='observation_pkey')
    )

    date_time: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    species_observed: Mapped[int] = mapped_column(Integer, ForeignKey('species.species_id'), primary_key=True)
    observer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    county_id: Mapped[Optional[int]] = mapped_column(Integer)
    observation_type: Mapped[Optional[str]] = mapped_column(Text)
    notes: Mapped[Optional[str]] = mapped_column(Text)
    status: Mapped[Optional[str]] = mapped_column(Text)

    county: Mapped[Optional['County']] = relationship('County', back_populates='observations')
    observer: Mapped['Userr'] = relationship('Userr', back_populates='observations')
    species: Mapped[Optional['Species']] = relationship('Species')
    comment: Mapped[list['Comment']] = relationship('Comment', back_populates='observation')
    media: Mapped[list['Media']] = relationship('Media', back_populates='observation')

    def __str__(self):
        date_str = self.date_time.strftime("%Y-%m-%d %H:%M") if self.date_time else "Unknown date"
        observer_name = self.observer.name if self.observer else f"User {self.observer_id}"
        species_name = self.species.common_name if self.species else f"Species {self.species_observed}"
        county_name = self.county.name if self.county else f"County {self.county_id}"
        county_state = self.county.state if self.county else "Unknown"
        return (
            f"{observer_name} observed {species_name} "
            f"in {county_name}, {county_state} on {date_str} "
            f"as a {self.observation_type or 'Unknown'} observation "
            f"(Status: {self.status or 'Unknown'})"
        )
    
    def __repr__(self):
        observer_name = self.observer.name
        species_name = self.species.common_name
        date_str = self.date_time.strftime("%Y-%m-%d %H:%M")
        notes = self.notes or ""

        summary = f"{observer_name} observed {species_name} on {date_str}"
        if notes:
            summary += f" — Notes: {notes}"

        return summary


t_specialized_in = Table(
    'specialized_in', Model.metadata,
    Column('specialty_id', Integer),
    Column('user_id', Integer),
    ForeignKeyConstraint(['specialty_id'], ['specialty.specialty_id'], name='specialized_in_specialty_id_fkey'),
    ForeignKeyConstraint(['user_id'], ['user.user_id'], name='specialized_in_user_id_fkey')
)


t_species_exists = Table(
    'species_exists', Model.metadata,
    Column('species_id', Integer),
    Column('county_id', Integer),
    ForeignKeyConstraint(['county_id'], ['county.county_id'], name='species_exists_county_id_fkey'),
    ForeignKeyConstraint(['species_id'], ['species.species_id'], name='species_exists_species_id_fkey')
)


class Comment(Model):
    __tablename__ = 'comment'
    __table_args__ = (
        ForeignKeyConstraint(['observation_date_time', 'observation_species_observed', 'observation_observer_id'], ['observation.date_time', 'observation.species_observed', 'observation.observer_id'], name='comment_observation_date_time_observation_species_observed_fkey'),
        PrimaryKeyConstraint('comment_id', name='comment_pkey')
    )

    comment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(Integer)
    observation_date_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    observation_species_observed: Mapped[Optional[int]] = mapped_column(Integer)
    observation_observer_id: Mapped[Optional[int]] = mapped_column(Integer)
    comment_text: Mapped[Optional[str]] = mapped_column(Text)
    time_stamp: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)

    observation: Mapped[Optional['Observation']] = relationship('Observation', back_populates='comment')

    def __str__(self):
        if self.observation:
            return f"Comment on Observation of #{self.observation.species_observed}"
        return f"Comment #{self.comment_id}"
    
    def __repr__(self):
        return self.comment_text or ""


class Media(Model):
    __tablename__ = 'media'
    __table_args__ = (
        ForeignKeyConstraint(['media_date_time', 'media_species_observed', 'media_observer_id'], ['observation.date_time', 'observation.species_observed', 'observation.observer_id'], name='media_media_date_time_media_species_observed_media_observe_fkey'),
        #PrimaryKeyConstraint('media_id', name='media_pkey')
    )

    media_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    media_date_time: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    media_species_observed: Mapped[Optional[int]] = mapped_column(Integer)
    media_observer_id: Mapped[Optional[int]] = mapped_column(Integer)
    media_type: Mapped[Optional[str]] = mapped_column(Text)
    media_URL: Mapped[Optional[str]] = mapped_column(Text)
    description: Mapped[Optional[str]] = mapped_column(Text)

    observation: Mapped[Optional['Observation']] = relationship('Observation', back_populates='media')

    def __str__(self):
        if self.observation:
            return f"Media on Species {self.observation.species_observed}"
        return f"Media #{self.media_id}"


class LikedObservation(Model):
    """Table to store which observations users have liked."""
    __tablename__ = 'liked_observation'
    __table_args__ = (
        ForeignKeyConstraint(
            ['observation_date_time', 'observation_species_observed', 'observation_observer_id'],
            ['observation.date_time', 'observation.species_observed', 'observation.observer_id'],
            name='liked_observation_observation_fkey'
        ),
        PrimaryKeyConstraint('user_id', 'observation_date_time', 'observation_species_observed', 'observation_observer_id', name='liked_observation_pkey')
    )

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Flask-AppBuilder user ID
    observation_date_time: Mapped[datetime.datetime] = mapped_column(DateTime, primary_key=True)
    observation_species_observed: Mapped[int] = mapped_column(Integer, primary_key=True)
    observation_observer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    liked_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, default=lambda: datetime.datetime.now())

    observation: Mapped[Optional['Observation']] = relationship('Observation')

    def __str__(self):
        return f"User {self.user_id} liked observation at {self.observation_date_time}"
    
    def __repr__(self):
        return f"<LikedObservation user_id={self.user_id}, obs_date={self.observation_date_time}>"