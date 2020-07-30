run:
	FLASK_DEBUG=1 FLASK_APP=main:app venv/bin/flask run
install:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
