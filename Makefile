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

test:
	$(ENV)/python setup.py test

run:
	$(ENV)/python 

freeze:
	$(ENV)/pip freeze
