create virtual env:

	virtualenv -p python3 venv/py36web

install requirements libs

	pip3 install -r requirements.txt

run the app

	export FLASK_APP=main
	export FLASK_ENV=development
	flask run
