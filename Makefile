ENV=./env/bin

dev: 
	$(ENV)/pip install -r requirements/dev.txt --upgrade

prod:
	$(ENV)/pip install -r requirements/prod.txt --upgrade

env:
	virtualenv -p `which python3` env

clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.egg-info
	rm -rf __pycache__

test:
	$(ENV)/pip install -r requirements/test.txt --upgrade
	$(ENV)/flake8 mailpimp.py
	$(ENV)/coverage report --fail-under=20
	$(ENV)/nosetests


run:
	$(ENV)/python 

freeze:
	$(ENV)/pip freeze
