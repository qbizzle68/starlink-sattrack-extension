import tomllib
from copy import deepcopy
from importlib.resources import files

# Global configuration dictionary.
starlinkConfig = {}


def importDefaultConfig() -> dict:
    """Import the default starlink configuration as a resource distributed as package data."""

    configPath = files('starlink.config').joinpath('starlink-config.toml')
    with open(configPath, 'rb') as toml:
        config = tomllib.load(toml)

    return config


def updateConfig(path: str):
    """Update the global starlinkConfig variable to the config file at path. The config file must be
    a strictly formatted toml file. TODO: add format link.
    Any missing required default values will be added to the configuration."""

    global starlinkConfig
    defaults: dict = deepcopy(starlinkConfig['defaults'])
    starlinkConfig.clear()

    with open(path, 'rb') as toml:
        _importedConfig = tomllib.load(toml)

    starlinkConfig.update(_importedConfig)

    if not starlinkConfig.get('defaults'):
        starlinkConfig['defaults'] = {}
        starlinkConfig['defaults'].update(defaults)


def getConfig() -> dict:
    """If needed, this method returns the internal starlinkConfig dictionary."""

    global starlinkConfig
    return starlinkConfig
