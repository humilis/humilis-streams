Kinesis Streams
==================

A [humilis][humilis] plug-in layer that deploys one ore more
[Kinesis streams][kinesis]. See [humilis][humilis] documentation for more
information.

[firehose]: http://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html
[kinesis]: https://aws.amazon.com/documentation/kinesis/
[humilis]: https://github.com/InnovativeTravel/humilis


## Installation

```
pip install git+https://github.com/InnovativeTravel/humilis-streams
```


## Development

Assuming you have [virtualenv][venv] installed:

[venv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```

Configure humilis:

```
.env/bin/humilis configure --local
```


## Testing

This layer has no embedded logic so there are no unit tests. To run the
integration test suite you will first need to make a test deployment to AWS:

```
make create
```

Then you can run the tests using:

```
make test
```

Don't forget to delete the deployment when you are done:

```
make delete
```


## More information

See [humilis][humilis] documentation.


## Who do I ask?

Ask [German](mailto:german@innovativetravel.eu)
