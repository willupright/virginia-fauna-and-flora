CREATE TABLE "county" (
  "county_id" INT PRIMARY KEY,
  "state" TEXT,
  "name" TEXT,
  "region" TEXT
);

CREATE TABLE "observation" (
  "date_time" timestamp,
  "species_observed" INT,
  "observer_id" INT,
  "county_id" INT,
  "observation_type" TEXT,
  "notes" TEXT,
  "status" TEXT,
  PRIMARY KEY ("date_time", "species_observed", "observer_id")
);

CREATE TABLE "user" (
  "user_id" INT PRIMARY KEY,
  "name" TEXT,
  "permission_level" INT,
  "email" TEXT
);

CREATE TABLE "specialized_in" (
  "specialty_id" INT,
  "user_id" INT
);

CREATE TABLE "specialty" (
  "specialty_id" INT PRIMARY KEY,
  "admin_specialty" TEXT
);

CREATE TABLE "species_exists" (
  "species_id" INT,
  "county_id" INT
);

CREATE TABLE "species" (
  "species_id" SERIAL PRIMARY KEY,
  "common_name" TEXT,
  "scientific_name" TEXT,
  "category" TEXT,
  "conservation_status" TEXT,
  "description" TEXT
);

CREATE TABLE "habitat" (
  "species_id" INT,
  "habitat" TEXT,
  PRIMARY KEY ("species_id", "habitat")
);

CREATE TABLE "media" (
  "media_id" INT PRIMARY KEY,
  "media_date_time" timestamp,
  "media_species_observed" INT,
  "media_observer_id" INT,
  "media_type" TEXT,
  "media_URL" TEXT,
  "description" TEXT
);

CREATE TABLE "comment" (
  "comment_id" INT PRIMARY KEY,
  "user_id" INT,
  "observation_date_time" timestamp,
  "observation_species_observed" INT,
  "observation_observer_id" INT,
  "comment_text" TEXT,
  "time_stamp" timestamp
);

CREATE TABLE "liked_observation" (
  "user_id" INT,
  "observation_date_time" timestamp,
  "observation_species_observed" INT,
  "observation_observer_id" INT,
  "liked_at" timestamp,
  PRIMARY KEY ("user_id", "observation_date_time", "observation_species_observed", "observation_observer_id")
);



