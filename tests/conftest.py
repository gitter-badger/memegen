import json
import logging

import pytest

from memegen.app import create_app
from memegen.settings import get_config


def load(response, as_json=True):
    """Convert a response's binary data (JSON) to a dictionary."""
    text = response.data.decode('utf-8')
    if not as_json:
        return text
    if text:
        data = json.loads(text)
    else:
        data = None
    logging.debug("response: %r", data)
    return data


@pytest.fixture
def app():
    return create_app(get_config('test'))


@pytest.fixture
def client(app):
    return app.test_client()
