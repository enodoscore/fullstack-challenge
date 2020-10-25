export FLASK_APP=api/properties
export FLASK_ENV=development
export APP_ROOT=~/git/enodo-fullstack-challenge

npm run --prefix ./properties-app/ serve &
flask run
