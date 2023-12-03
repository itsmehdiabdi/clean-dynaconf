from dynaconf import Dynaconf
import os
from dotenv import load_dotenv
from utils import Settings

load_dotenv("./.env")
network = os.getenv("NETWORK")
env = os.getenv("ENV")
print(network, env)

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml"],
    environments=True,
    env=env,
    merge_enabled=True,
).as_dict()

network_settings = settings.pop('NETWORKS', None)
settings |= network_settings.get(network, {})
print(settings)

settings = Settings(**settings)
