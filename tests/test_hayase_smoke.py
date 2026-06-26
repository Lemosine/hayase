from hayase.main import load_config


def test_load_config_returns_dict():
    assert isinstance(load_config(), dict)
