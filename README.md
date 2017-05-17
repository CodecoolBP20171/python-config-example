# python-config-example
It is a simple example to show how to separate your private settings not to version control it.

Check how [dbConnectionTest.py](dbConnectionTest.py) imports [config.py](config.py), [public_config.py](public_config.py), [private_config.py](private_config.py) in this order to create default settings and to overwrite/extend it with the private ones.

Private config file (private_config.py) is not uploaded (see [.gitignore](.gitignore)) into git but instead [private_config_template.py](private_config_template.py) is. This later one shows a skeleton to define your local private_config.py file
