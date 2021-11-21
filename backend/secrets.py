import subprocess
import yaml
import os

import getpass
import sys

class SecretGetter:
    def __init__(self, secret_path: str):
        self._secret_path = secret_path
        self._yaml = self._getSecrets()
        self._secrets = yaml.safe_load(self._yaml)

    def _configGPG(self):
        os.environ['GNUPGHOME'] = "/home/www-data/.gnupg"       

    def _getSecrets(self):
        self._configGPG()
        cmd = f"gpg -q -d {self._secret_path}"
        val = subprocess.run(cmd.split(' '), stdout=subprocess.PIPE).stdout
        return val

    def getSecret(self, key):
        return self._secrets[key]
