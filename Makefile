HUMILIS := .env/bin/humilis
PIP := .env/bin/pip
TOX := .env/bin/tox
PYTHON := .env/bin/python
STAGE := DEV
HUMILIS_ENV := tests/integration/streams

# create virtual environment
.env:
	virtualenv .env -p python3

# install dev dependencies, create layers directory
develop: .env
	.env/bin/pip install -r requirements-dev.txt

# run integration tests
test: .env
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
	$(PYTHON) setup.py sdist upload
