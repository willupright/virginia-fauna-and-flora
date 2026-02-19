-- Migration script to add liked_observation table to existing database
-- Run this script if you want to add the table without rebuilding the entire database
-- Usage: psql -h localhost -p 5432 -U team27 team27 < migrate_liked_observation.sql

CREATE TABLE IF NOT EXISTS "liked_observation" (
  "user_id" INT,
  "observation_date_time" timestamp,
  "observation_species_observed" INT,
  "observation_observer_id" INT,
  "liked_at" timestamp,
  PRIMARY KEY ("user_id", "observation_date_time", "observation_species_observed", "observation_observer_id")
);

-- Add foreign key constraint if it doesn't exist
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint 
        WHERE conname = 'liked_observation_observation_fkey'
    ) THEN
        ALTER TABLE "liked_observation" 
        ADD CONSTRAINT "liked_observation_observation_fkey"
        FOREIGN KEY ("observation_date_time", "observation_species_observed", "observation_observer_id") 
        REFERENCES "observation" ("date_time", "species_observed", "observer_id");
    END IF;
END $$;

