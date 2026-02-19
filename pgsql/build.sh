# This script rebuilds the entire database.
#
# Create a pgpass file in your home directory for storing the password.
# See https://www.postgresql.org/docs/16/libpq-pgpass.html for details.

export CMD='psql -q -h localhost -p 5432 -U team27 team27'

echo Dropping tables...
$CMD < drop.sql

echo Creating tables...
$CMD < create.sql

echo Adding comments...
$CMD < comment.sql

echo Loading data...
$CMD < load.sql

echo Generating data...
python generate.py

echo Adding constraints...
$CMD < alter.sql

# echo "Syncing sequences..."
# $CMD -c "SELECT setval('comment_comment_id_seq', COALESCE((SELECT MAX(comment_id) FROM comment), 0));"
# $CMD -c "SELECT setval('species_species_id_seq', COALESCE((SELECT MAX(species_id) FROM species), 0));"


echo Creating views...
$CMD < views.sql
