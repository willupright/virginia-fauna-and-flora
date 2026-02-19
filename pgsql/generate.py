"""Generate fake data for the database."""
__authors__ = "Tenley, Michael, Will, Theo"
import csv
import faker
import random
import os
import sys

from faker import Faker
from pprint import pprint

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from flask_appbuilder import Model

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from webapp.models.tables import (
    County,
    Specialty,
    Species,
    Userr,
    Habitat,
    Observation,
    Comment,
    Media,
    t_specialized_in,
    t_species_exists,
)

# DB_URL = "postgresql+psycopg://kennetta:114296106@localhost/team27"

BASE_DIR = os.path.dirname(__file__)  # /path/to/database/pgsql
SPECIES_CSV_PATH = os.path.join(BASE_DIR, "..", "database", "data", "species.csv")
PLANTS_CSV_PATH = os.path.join(BASE_DIR, "..", "database", "data", "plants-list.csv")

# Conservation statuses and abbreviations
CONSERVATION_STATUSES = [
    ("N", "Native"),
    ("I", "Invasive")
]

PLANT_TYPES = [
    "Flower",
    "Shrub",
    "Tree",
    "Aquatic Plant",
    "Grass / Sedge",
    "Herb / Vegetable",
    "Other"
]

# Number of rows to generate per table
NUM_COUNTY = 10
NUM_SPECIALTY = 8
NUM_SPECIES = 20 #? 
NUM_USER = 10
NUM_HABITAT = 20
NUM_OBSERVATION = 25
NUM_COMMENT = 40
NUM_MEDIA = 20
NUM_COUNTIES_PER_SPECIES = 60  # minimum number of counties per species
MAX_COUNTIES_PER_SPECIES = 120  # maximum number of counties per species

# Containers for generated data
counties: list[County] = []
specialties: list[Specialty] = []
plant_list: list[Species] = []
all_species: list[Species] = []
users: list[Userr] = []
habitats: list[Habitat] = []
observations: list[Observation] = []
comments: list[Comment] = []
media_list: list[Media] = []

DB_URL = "postgresql+psycopg://team27:5pz7eyHHUSpu+jcZ@localhost/team27"

# con = psycopg.connect(host="localhost", port="5432", user="kennetta", dbname="team27")

# Initialize generators
random.seed(0)
fake = faker.Faker()

def make_counties():
    return [
        # Northern Virginia
        County(state="Virginia", name="Arlington County", region="Northern"),
        County(state="Virginia", name="Fairfax County", region="Northern"),
        County(state="Virginia", name="Loudoun County", region="Northern"),
        County(state="Virginia", name="Prince William County", region="Northern"),
        County(state="Virginia", name="Fauquier County", region="Northern"),
        County(state="Virginia", name="Stafford County", region="Northern"),
        County(state="Virginia", name="Clarke County", region="Northern"),
        County(state="Virginia", name="Spotsylvania County", region="Northern"),
        County(state="Virginia", name="King George County", region="Northern"),
        County(state="Virginia", name="Rappahannock County", region="Northern"),

        # Northwestern/Shenandoah Valley
        County(state="Virginia", name="Frederick County", region="Northwestern"),
        County(state="Virginia", name="Shenandoah County", region="Northwestern"),
        County(state="Virginia", name="Warren County", region="Northwestern"),
        County(state="Virginia", name="Page County", region="Northwestern"),
        County(state="Virginia", name="Rockingham County", region="Northwestern"),
        County(state="Virginia", name="Augusta County", region="Northwestern"),
        County(state="Virginia", name="Rockbridge County", region="Northwestern"),
        County(state="Virginia", name="Bath County", region="Northwestern"),
        County(state="Virginia", name="Highland County", region="Northwestern"),
        County(state="Virginia", name="Alleghany County", region="Northwestern"),
        County(state="Virginia", name="Botetourt County", region="Northwestern"),
        County(state="Virginia", name="Craig County", region="Northwestern"),
        County(state="Virginia", name="Roanoke County", region="Northwestern"),
        County(state="Virginia", name="Floyd County", region="Northwestern"),
        County(state="Virginia", name="Montgomery County", region="Northwestern"),
        County(state="Virginia", name="Pulaski County", region="Northwestern"),
        County(state="Virginia", name="Giles County", region="Northwestern"),

        # Central Virginia
        County(state="Virginia", name="Albemarle County", region="Central"),
        County(state="Virginia", name="Buckingham County", region="Central"),
        County(state="Virginia", name="Fluvanna County", region="Central"),
        County(state="Virginia", name="Greene County", region="Central"),
        County(state="Virginia", name="Louisa County", region="Central"),
        County(state="Virginia", name="Nelson County", region="Central"),
        County(state="Virginia", name="Orange County", region="Central"),
        County(state="Virginia", name="Madison County", region="Central"),
        County(state="Virginia", name="Amherst County", region="Central"),
        County(state="Virginia", name="Appomattox County", region="Central"),
        County(state="Virginia", name="Bedford County", region="Central"),
        County(state="Virginia", name="Campbell County", region="Central"),
        County(state="Virginia", name="Pittsylvania County", region="Central"),
        County(state="Virginia", name="Halifax County", region="Central"),
        County(state="Virginia", name="Charlotte County", region="Central"),
        County(state="Virginia", name="Prince Edward County", region="Central"),
        County(state="Virginia", name="Cumberland County", region="Central"),

        # Eastern Virginia/Tidewater
        County(state="Virginia", name="Accomack County", region="Eastern"),
        County(state="Virginia", name="Northampton County", region="Eastern"),
        County(state="Virginia", name="Essex County", region="Eastern"),
        County(state="Virginia", name="Lancaster County", region="Eastern"),
        County(state="Virginia", name="Northumberland County", region="Eastern"),
        County(state="Virginia", name="Richmond County", region="Eastern"),
        County(state="Virginia", name="Westmoreland County", region="Eastern"),
        County(state="Virginia", name="King and Queen County", region="Eastern"),
        County(state="Virginia", name="King William County", region="Eastern"),
        County(state="Virginia", name="Gloucester County", region="Eastern"),
        County(state="Virginia", name="Mathews County", region="Eastern"),
        County(state="Virginia", name="Middlesex County", region="Eastern"),
        County(state="Virginia", name="York County", region="Eastern"),
        County(state="Virginia", name="James City County", region="Eastern"),
        County(state="Virginia", name="Surry County", region="Eastern"),
        County(state="Virginia", name="Isle of Wight County", region="Eastern"),
        County(state="Virginia", name="Southampton County", region="Eastern"),
        County(state="Virginia", name="Sussex County", region="Eastern"),
        County(state="Virginia", name="Prince George County", region="Eastern"),
        County(state="Virginia", name="Chesapeake City", region="Eastern"),
        County(state="Virginia", name="Norfolk City", region="Eastern"),
        County(state="Virginia", name="Virginia Beach City", region="Eastern"),
        County(state="Virginia", name="Portsmouth City", region="Eastern"),
        County(state="Virginia", name="Hampton City", region="Eastern"),
        County(state="Virginia", name="Newport News City", region="Eastern"),
        County(state="Virginia", name="Franklin City", region="Eastern"),
        County(state="Virginia", name="Williamsburg City", region="Eastern"),

        # Southwestern Virginia
        County(state="Virginia", name="Lee County", region="Southwestern"),
        County(state="Virginia", name="Scott County", region="Southwestern"),
        County(state="Virginia", name="Wise County", region="Southwestern"),
        County(state="Virginia", name="Dickenson County", region="Southwestern"),
        County(state="Virginia", name="Buchanan County", region="Southwestern"),
        County(state="Virginia", name="Russell County", region="Southwestern"),
        County(state="Virginia", name="Tazewell County", region="Southwestern"),
        County(state="Virginia", name="Smyth County", region="Southwestern"),
        County(state="Virginia", name="Washington County", region="Southwestern"),
        County(state="Virginia", name="Grayson County", region="Southwestern"),
        County(state="Virginia", name="Carroll County", region="Southwestern"),
        County(state="Virginia", name="Patrick County", region="Southwestern"),
        County(state="Virginia", name="Wythe County", region="Southwestern"),
        County(state="Virginia", name="Henry County", region="Southwestern"),
        County(state="Virginia", name="Bristol City", region="Southwestern")
    ]

# Global for later
ALL_COUNTIES = make_counties()

def make_habitats_with_species(species: list[Species]) -> list[Habitat]:
    habitat_options = [
        "Forest", "Grassland", "Wetland", "Coastal", "Urban",
        "Agricultural", "Desert", "Mountains", "Freshwater", "Riparian"
    ]
    habitats: list[Habitat] = []
    for sp in species:
        num_habitats = random.randint(1, 3)
        rand_habitats = random.sample(habitat_options, k=num_habitats)
        for hab in rand_habitats:
            habitats.append(Habitat(habitat=hab, species=sp))
    return habitats


def make_observations():
    obs = []
    for _ in range(NUM_OBSERVATION):
        date_time = fake.date_time_this_year()
        species_observed = random.randint(1, NUM_SPECIES)
        observer_id = random.randint(1, NUM_USER)
        county_id = random.randint(1, NUM_COUNTY)
        observation_type = random.choice(["Private", "Public", "Research"])
        notes = fake.text(max_nb_chars=200)
        status = random.choice(["Confirmed", "Unconfirmed", "Pending"])

        observation = Observation(
            date_time=date_time,
            species_observed=species_observed,
            observer_id=observer_id,
            county_id=county_id,
            observation_type=observation_type,
            notes=notes,
            status=status
        )
        obs.append(observation)
    return obs

def make_users():
    users = []
    for i in range(NUM_USER):
        user = Userr(
            user_id=i + 1,
            name=fake.name(),
            permission_level=random.randint(1, 4),
            email=fake.email()
        )
        users.append(user)
    return users

# AI used to help with opening and reading a csv file using DictReader
def make_species_from_csv(path: str) -> list[Species]:
    species_list = []
    
    with open(path, newline='', encoding='utf-8') as csvfile:
        # DictReader reads the csv as a dictionary 
        # where the keys are the column names from the header row
        reader = csv.DictReader(csvfile)
        for row in reader:            
            if random.random() < 0.15:  # 15% chance of an invasive
                status_code, status_label = ("I", "Invasive")
            else:
                status_code, status_label = ("N", "Native")
            
            s = Species(
                common_name=row["common_name"].strip(),
                scientific_name=row["scientific_name"].strip(),
                category=row["category"].strip(),
                conservation_status=status_code,
                description=fake.paragraph(nb_sentences=3)
            )
            species_list.append(s)
    all_species.extend(species_list)
    return species_list

def make_plants_from_csv(path: str) -> list[Species]:
    plants_list = []
    
    with open(path, newline='', encoding='utf-8-sig') as csvfile:
        # DictReader reads the csv as a dictionary 
        # where the keys are the column names from the header row
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row.keys())
            cat = random.choice(PLANT_TYPES)
            p = Species(
                common_name=row["common_name"].strip(),
                scientific_name=row["scientific_name"].strip(),
                category=cat,
                conservation_status=row["conservation_status"].strip(),
                description=fake.paragraph(nb_sentences=3)
            )
            plants_list.append(p)
    all_species.extend(plants_list)
    return plants_list


def link_species_and_counties(counties: list[County], all_species: list[Species]):
    species_exists_entries = []

    for sp in all_species:
        num_counties = random.randint(NUM_COUNTIES_PER_SPECIES, min(MAX_COUNTIES_PER_SPECIES, len(counties)))
        rand_counties = random.sample(counties, k=num_counties)
        for county in rand_counties:
            species_exists_entries.append({
                'species_id': sp.species_id,
                'county_id': county.county_id
            })
    
    return species_exists_entries

def make_comments(observations: list[Observation]):
    """Create comments that reference existing observations."""
    comments = []
    for i in range(NUM_COMMENT):
        # Pick a random observation to comment on
        observation = random.choice(observations)
        comment = Comment(
            comment_id=i + 1,
            observation_date_time=observation.date_time,
            observation_species_observed=observation.species_observed,
            observation_observer_id=observation.observer_id,
            user_id=random.randint(1, NUM_USER),
            comment_text=fake.text(max_nb_chars=200),
            time_stamp=fake.date_time_this_year()
        )
        comments.append(comment)
    return comments

def make_media(observations: list[Observation]):
    """Create media that references existing observations."""
    media_items = []
    media_types = ["Image", "Video", "Audio"]
    for i in range(NUM_MEDIA):
        # Pick a random observation to attach media to
        observation = random.choice(observations)
        media = Media(
            media_id=i + 1,
            media_date_time=observation.date_time,
            media_species_observed=observation.species_observed,
            media_observer_id=observation.observer_id,
            media_type=random.choice(media_types),
            media_URL=fake.url(),
            description=fake.text(max_nb_chars=200)
        )
        media_items.append(media)
    return media_items

def make_specialties():
    specialties = []
    specialty_names = [
        "Botany",
        "Zoology",
        "Ecology",
        "Conservation",
        "Entomology",
        "Ornithology",
        "Herpetology",
        "Marine Biology"
    ]
    for i, name in enumerate(specialty_names):
        specialty = Specialty(
            specialty_id=i + 1,
            admin_specialty=name
        )
        specialties.append(specialty)
    return specialties


def main():
    engine = create_engine(DB_URL)
    
    # Drop all views first (CASCADE will handle dependencies)
    with engine.begin() as conn:
        # Query for all views in the public schema and drop them
        result = conn.execute(text("""
            SELECT table_name 
            FROM information_schema.views 
            WHERE table_schema = 'public'
        """))
        views = [row[0] for row in result.fetchall()]
        
        # Drop each view with CASCADE
        for view_name in views:
            conn.execute(text(f'DROP VIEW IF EXISTS "{view_name}" CASCADE;'))
            # Also try lowercase version in case PostgreSQL stored it differently
            conn.execute(text(f'DROP VIEW IF EXISTS {view_name.lower()} CASCADE;'))

    # Now drop all tables
    Model.metadata.drop_all(engine)
    Model.metadata.create_all(engine)
    
    with Session(engine) as session:
        cts = make_counties()
        specs = make_species_from_csv(SPECIES_CSV_PATH)
        plants = make_plants_from_csv(PLANTS_CSV_PATH)
        users = make_users()
        obs = make_observations()
        # Create comments and media that reference existing observations
        comments = make_comments(obs)
        media = make_media(obs)
        specialties = make_specialties()
        # session.add_all(specs)
        habs = make_habitats_with_species(specs)
        session.add_all(ALL_COUNTIES)
        session.flush()
        
        session.add_all(specs + plants + habs + users + obs + comments + media + specialties)
        session.flush()

        species_and_counties = link_species_and_counties(ALL_COUNTIES, all_species)
        session.execute(t_species_exists.insert(), species_and_counties)
        session.commit()


    print("Inserted 10 Virginia counties successfully!")

    # con.commit()
    print("Fake data successfully generated and inserted!")

    with engine.begin() as conn:
        conn.execute(text("""
            SELECT setval('comment_comment_id_seq', COALESCE((SELECT MAX(comment_id) FROM comment), 1), true);
        """))
        conn.execute(text("""
            SELECT setval(pg_get_serial_sequence('media','media_id'), 21, false);
        """))
        print("comment id value synced to current max id")



if __name__ == "__main__":
    main()
