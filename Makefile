# create virtual environment
.env:
	virtualenv .env -p python3.4

# install dev dependencies, create layers directory
develop: .env
	.env/bin/pip install -r requirements-dev.txt
	mkdir -p layers
	rm -f layers/io-streams
	ln -fs ../ layers/io-streams

# run test suite
test:
	.env/bin/tox

# remove virtualenv and layers dir
clean:
	rm -rf .env
	rm layers/io-streams

create:
	humilis create --stage TEST io-streams.yaml


update:
	humilis update --stage TEST io-streams.yaml


delete:
	humilis delete --stage TEST io-streams.yaml
