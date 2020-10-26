export FLASK_APP=api/properties
export FLASK_ENV=development
export APP_ROOT=~/git/enodo-fullstack-challenge

# create the db
python api/properties/db/db_init.py --force
npm run --prefix ./properties-app/ serve &
flask run
