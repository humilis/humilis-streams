HUMILIS := .env/bin/humilis
PYTHON := .env/bin/python
STAGE := DEV
HUMILIS_ENV := streams

# create virtual environment
.env:
	virtualenv .env -p python3.4

# create symlinks
symlinks:
	mkdir -p layers
	rm -f layers/$(HUMILIS_ENV)
	ln -fs ../ layers/$(HUMILIS_ENV)

# install dev dependencies
develop: .env symlinks
	.env/bin/pip install -r requirements-dev.txt

# run test suite
test: develop
	.env/bin/tox

# remove virtualenv and layers dir
clean:
	rm -rf .env
	rm -f layers/$(HUMILIS_ENV)

create: develop
	$(HUMILIS) create --stage $(STAGE) $(HUMILIS_ENV).yaml

update: develop
	$(HUMILIS) update --stage $(STAGE) $(HUMILIS_ENV).yaml

delete: develop
	$(HUMILIS) delete --stage $(STAGE) $(HUMILIS_ENV).yaml
