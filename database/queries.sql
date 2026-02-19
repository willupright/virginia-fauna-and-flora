--------Will Upright----------
--getting the species, county, and notes of all approved observations
SELECT 
    observation.notes,
    species.common_name,
    county.name
FROM observation
    JOIN species ON observation.species_observed = species.species_id
    JOIN county ON observation.county_id = county.county_id
WHERE observation.status = 'Approved';

--getting all of the species in Rockingham County
SELECT 
    species.common_name,
    species.scientific_name,
    species.category,
    county.name
FROM species_exists
    JOIN species ON species_exists.species_id = species.species_id
    JOIN county ON species_exists.county_id = county.county_id
WHERE county.name = 'Rockingham County';

------------------------------



--------Michael Gerber----------
--Get all observations from a single user--
SELECT 
	Observation.observation_id,
	species.common_name,
	Observation.date,
	observation.status
	observation.notes 
FROM observation
JOIN species ON observation.species_observed = species.species_id
WHERE observation.observer_id = 1983

--Count of species in each county--
SELECT 
    county.name AS county,
    COUNT(DISTINCT species_exists.species_id) AS species_count
FROM county
LEFT JOIN species_exists ON county.county_id = species_exists.county_id
GROUP BY county.name
ORDER BY species_count DESC;

--------------------------------


--------Theo Mandelbaum----------
--Getting all of the observations species and their status from a specific user (user 12) from Loudon County
SELECT
    ob.species_observed,
    ob.status
FROM observation as ob
JOIN user ON user.user_id = ob.observer_id
JOIN county ON county.county_id = ob.county_id
WHERE user.user_id = 12
    AND county.name = 'Loudon County';

--Getting the common names of the 10 most recent species observed in a "forest" habitat
SELECT
    sp.common_name
FROM species as sp
JOIN observation AS ob ON sp.species_id = ob.species_observed
WHERE sp.habitat == 'forest'
ORDER BY ob.date DESC
LIMIT 10;
-------------------------------


--------Tenley Kennett----------
--Get all endangered species in Virginia--
SELECT
    species.common_name,
    species.scientific_name
FROM species
WHERE species.conservation_status = 'endangered'
ORDER BY species.common_name DESC;


--Get all admin who specialize in aquatic mammals--
SELECT
    user_id,
    name,
    email
FROM user
JOIN admin ON user.user_id = admin.user_id
WHERE admin.specialty = 'aquatic mammals';