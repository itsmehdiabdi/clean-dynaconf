from dynaconf import Dynaconf
import os
from dotenv import load_dotenv
from utils import Settings

load_dotenv("./.env")
network = os.getenv("NETWORK")
env = os.getenv("ENV")
print(network, env)

environment_settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.environment.toml"],
    environments=True,
    env=env,
    merge_enabled=True,
).as_dict()

network_settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.network.toml"],
    environments=True,
    env=network,
    merge_enabled=True,
).as_dict()

settings = environment_settings | network_settings

print(settings)

settings = Settings(**settings)
