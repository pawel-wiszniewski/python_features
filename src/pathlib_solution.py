# tasks:
# 1 - refactor read_config function to use pathlib function and Path object


import json
import os
from pathlib import Path
from typing import Any


def main():
    config = read_config("config.json")
    print(config)


def read_config(file_name: str) -> dict[str, Any]:
    root_folder = Path(__file__).parent
    with open(root_folder / "config" / file_name, "rt") as config_file:
        config = json.load(config_file)
    return config


if __name__ == "__main__":
    main()
