from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
from os import getenv, path, environ
import botocore
from config import BASE_DIR

from dotenv import load_dotenv


class SecretManager:

    def __init__(self):
        try:
            load_dotenv(dotenv_path=path.join(BASE_DIR, ".env"))
        except Exception as ex:
            print(f"{ex}")

        if getenv("ENV_TYPE").lower == "dev":
            self.printenv()
        self.get_client()
        self.get_cache()

    def printenv(self):
        for key in environ:
            print(f"{key}: {getenv(key)}")

    def get_client(self):
        self.client = botocore.session.get_session().create_client(
            service_name='secretsmanager',
            aws_access_key_id=getenv("AWS_ACCESS_KEY_ID", ""),
            aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY", ""),
            region_name=getenv("AWS_REGION_NAME", ""),

        )

    def get_cache(self):
        cache_config = SecretCacheConfig()
        self.cache = SecretCache(config=cache_config, client=self.client)

    def getenv(self, key: str = "") -> str:
        if not key or key == "":
            print(f"Imporper key: {key}")
            return ""
        try:
            secret = self.cache.get_secret_string(key)
            return secret
        except Exception as ex:
            print(f"KEY: {key}; {ex}")
            return ""

    def exportenv(self, key:str="")->None:
        if not key or key == "":
            print(f"Imporper key: {key}")
            return ""
        
        value: str = self.getenv(key)
        if value == "":
            print(f"VALUEERROR; ENVVAR not found. Placing blank.")

        environ[key.split("/")[-1]] = value


def main():
    secret_manager = SecretManager()
    key = "stg/crm-auto/es-url"
    # secret = secret_manager.getenv(key=key)
    secret_manager.exportenv(key)
    secret_manager.printenv()

if __name__ == "__main__":
    main()
