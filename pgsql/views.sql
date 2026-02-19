--
-- Workshops by department/college of faculty leader
--
CREATE VIEW rockingham_county AS
  SELECT 
    ROW_NUMBER() OVER () AS id,
    species.common_name,
    species.scientific_name,
    species.category,
    county.name
  FROM species_exists
  JOIN species ON species_exists.species_id = species.species_id
  JOIN county ON species_exists.county_id = county.county_id
  WHERE county.county_id = 15;

--
-- Workshops with assigned room information
--
CREATE VIEW number_species_in_each_county AS
  SELECT 
    ROW_NUMBER() OVER () AS id,
    county.name AS county,
    COUNT(DISTINCT species_exists.species_id) AS species_count
  FROM county
  LEFT JOIN species_exists ON county.county_id = species_exists.county_id
  GROUP BY county.name
  ORDER BY species_count DESC;


--
-- Species found in forest habitats
--
CREATE VIEW forest_species AS
  SELECT 
    ROW_NUMBER() OVER () AS id,
    sp.common_name,
    sp.scientific_name,
    sp.category
  FROM species as sp
  JOIN habitat AS h ON sp.species_id = h.species_id
  WHERE h.habitat = 'Forest'
  ORDER BY sp.common_name;

--
-- Invasive species (conservation_status = 'I')
--
CREATE VIEW invasive_species AS
  SELECT 
    ROW_NUMBER() OVER () AS id,
    species.common_name,
    species.scientific_name,
    species.category
  FROM species
  WHERE species.conservation_status = 'I'
  ORDER BY species.common_name DESC
