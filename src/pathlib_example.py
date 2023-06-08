# tasks:
# 1 - refactor read_config function to use pathlib function and Path object


import json
import os
from typing import Any


def main():
    config = read_config("config.json")
    print(config)


def read_config(file_name: str) -> dict[str, Any]:
    root_folder = os.path.dirname(os.path.abspath(__file__))
    config_folder = os.path.join(root_folder, "config")
    with open(f"{config_folder}/{file_name}", "rt") as config_file:
        config = json.load(config_file)
    return config


if __name__ == "__main__":
    main()
