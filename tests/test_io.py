# -*- coding: utf-8 -*-
"""
Tests the input and output Kinesis streams
"""

import base64
import pytest
import json
import uuid

import boto3
from humilis.environment import Environment


STAGE = "TEST"
ENVIRONMENT_PATH = "io-streams.yaml"
LAYER_NAME = "io-streams"


@pytest.fixture(scope="session", params=[1, 10, 100])
def events(request):
    """A batch of events to be ingested by Kinesis."""
    return [{
        "event_id": str(uuid.uuid4()).replace('-', ''),
        "timestamp": '2016-01-22T01:45:44.235+01:00',
        "client_id": "1628457772.1449082074",
        "url": "http://staging.findhotel.net/?lang=nl-NL",
        "referrer": "http://staging.findhotel.net/"
        } for _ in range(request.param)]


@pytest.fixture(scope="session")
def payloads(events):
    """A base 64 encoded data record."""
    payloads = []
    for kr in events:
        record = json.dumps(kr)
        payload = base64.encodestring(record.encode('utf-8')).decode()
        payloads.append(payload)
    return payloads


@pytest.fixture(scope="session")
def environment():
    """The io-streams-test humilis environment."""
    env = Environment(ENVIRONMENT_PATH, stage=STAGE)
    env.create()
    return env


@pytest.fixture(scope="session", params=['InputStream', 'OutputStream'])
def io_stream_name(environment, request):
    """The name of the input and output streams in the rawpipe layer."""
    layer = [l for l in environment.layers if l.name == LAYER_NAME][0]
    return layer.outputs.get(request.param)


@pytest.fixture(scope="session")
def kinesis():
    """Boto3 kinesis client."""
    return boto3.client('kinesis')


def test_io_streams_put_get_record(kinesis, io_stream_name, payloads):
    """Put and read a record from the input stream."""
    response = kinesis.put_records(
        StreamName=io_stream_name,
        Records=[
            {
                "Data": payload,
                "PartitionKey": str(uuid.uuid4())
            } for payload in payloads])

    assert response['ResponseMetadata']['HTTPStatusCode'] == 200
    seqnb = response['Records'][0]['SequenceNumber']
    shardid = response['Records'][0]['ShardId']
    # Try to read the data back from kinesis
    response = kinesis.get_shard_iterator(
        StreamName=io_stream_name,
        ShardId=shardid,
        ShardIteratorType='AT_SEQUENCE_NUMBER',
        StartingSequenceNumber=seqnb)
    record = kinesis.get_records(
        ShardIterator=response['ShardIterator'],
        Limit=1)['Records'][0]
    assert record['Data'].decode() == payloads[0]
