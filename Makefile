HUMILIS := .env/bin/humilis
PIP := .env/bin/pip
TOX := .env/bin/tox
PYTHON := .env/bin/python
TWINE := .env/bin/twine
STAGE := DEV
HUMILIS_ENV := tests/integration/streams

# create virtual environment
.env:
	virtualenv .env -p python3

# install dev dependencies, create layers directory
develop: .env
	$(PIP) install -r requirements-dev.txt

# run integration tests
test: develop
	$(PIP) install tox
	$(TOX)

# remove .tox and .env dirs
clean:
	rm -rf .env .tox

# deploy the test environment
create: develop
	$(HUMILIS) create --stage $(STAGE) $(HUMILIS_ENV).yaml

# update the test deployment
update: develop
	$(HUMILIS) update --stage $(STAGE) $(HUMILIS_ENV).yaml

# delete the test deployment
delete: develop
	$(HUMILIS) delete --stage $(STAGE) $(HUMILIS_ENV).yaml

# upload to Pypi
pypi: develop
	rm -rf dist
	$(PYTHON) setup.py sdist
	$(TWINE) upload dist/*
