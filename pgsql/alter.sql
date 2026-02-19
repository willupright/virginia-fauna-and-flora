ALTER TABLE "species_exists" ADD FOREIGN KEY ("county_id") REFERENCES "county" ("county_id");

ALTER TABLE "species_exists" ADD FOREIGN KEY ("species_id") REFERENCES "species" ("species_id");

--ALTER TABLE "observation_species" ADD FOREIGN KEY ("observation_species_observed") REFERENCES "observation" ("species_observed");

--ALTER TABLE "observation_species" ADD FOREIGN KEY ("species_species_id") REFERENCES "species" ("species_id");

ALTER TABLE "observation" ADD FOREIGN KEY ("county_id") REFERENCES "county" ("county_id");

--ALTER TABLE "user" ADD FOREIGN KEY ("user_id") REFERENCES "observation" ("observer_id");

ALTER TABLE "observation" ADD FOREIGN KEY ("observer_id") REFERENCES "user" ("user_id");

ALTER TABLE "media" ADD FOREIGN KEY ("media_date_time", "media_species_observed", "media_observer_id") REFERENCES "observation" ("date_time", "species_observed", "observer_id");

ALTER TABLE "specialized_in" ADD FOREIGN KEY ("specialty_id") REFERENCES "specialty" ("specialty_id");

ALTER TABLE "specialized_in" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("user_id");

ALTER TABLE "comment" ADD FOREIGN KEY ("observation_date_time", "observation_species_observed", "observation_observer_id") REFERENCES "observation" ("date_time", "species_observed", "observer_id");

ALTER TABLE "habitat" ADD FOREIGN KEY ("species_id") REFERENCES "species" ("species_id");

ALTER TABLE "liked_observation" ADD FOREIGN KEY ("observation_date_time", "observation_species_observed", "observation_observer_id") REFERENCES "observation" ("date_time", "species_observed", "observer_id");