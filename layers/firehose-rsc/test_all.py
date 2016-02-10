# -*- coding: utf-8 -*-

import uuid
from mock import Mock

import pytest
from lambda_function import lambda_function


@pytest.fixture(scope='session')
def create_event():
    """A sample CF create event."""
    return {
        "StackId": "arn:aws:cloudformation:us-west-2:XX/stack-name/guid",
        "ResponseURL": "http://pre-signed-S3-url-for-response",
        "ResourceProperties": {
            "StackName": "stack-name",
            "List": [
                "1",
                "2",
                "3"
                ]
            },
        "RequestType": "Create",
        "ResourceType": "Custom::TestResource",
        "RequestId": "unique id for this create request",
        "LogicalResourceId": "MyTestResource"
    }


@pytest.fixture(scope="session")
def context():
    """A dummy CF context object."""

    class DummyContext:
        def __init__(self):
            self.function_name = lambda_function.__name__
            self.function_version = 1
            self.invoked_function_arn = 'arn'
            self.memory_limit_in_mb = 128
            self.aws_request_id = str(uuid.uuid4())
            self.log_group_name = 'dummy_group'
            self.log_stream_name = 'dummy_stream'
            self.identity = Mock(return_value=None)
            self.client_context = Mock(return_value=None)

        def get_remaining_Time_in_millis():
            return 100

    return DummyContext()


def test_create(create_event, context, monkeypatch):
    """Tests resource creation."""
    monkeypatch.setattr("urllib2.build_opener",
                        Mock(return_value=Mock()))
    # Don't sleep!
    monkeypatch.setattr("time.sleep", lambda t: None)
    lambda_function.lambda_handler(create_event, context)
