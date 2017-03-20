all:

setup:
	pip install --upgrade pip setuptools wheel -r requirements.txt

install:
	pip install --upgrade .

develop:
	pip install --upgrade --editable .

uninstall:
	pip uninstall rpgtime

clean:
	rm -rf \*.egg-info
	rm -rf ENV
	rm -f `find . -name \*.pyc`
	rm -rf `find . -name __pycache__`
