# create virtual environment
.env:
	virtualenv .env -p python2.7

# install dev dependencies, create layers directory
develop: .env
	.env/bin/pip install -r requirements-dev.txt
	mkdir -p layers
	rm -f layers/firehose-rsc
	ln -fs ../ layers/firehose-rsc

# run test suite
test:
	.env/bin/tox

# remove virtualenv and layers dir
clean:
	rm -rf .env
	rm layers/firehose-rsc

create:
	humilis --profile test create --stage TEST humilisenv.yaml


update:
	humilis --profile test update --stage TEST humilisenv.yaml


delete:
	humilis --profile test delete --stage TEST humilisenv.yaml
