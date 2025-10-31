import importlib


def test_package_imports():
    mod = importlib.import_module("stochastic_reserving_framework")
    assert hasattr(mod, "__version__")
