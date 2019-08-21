from helpers.paths import EXPECTED_TEXT
from os import path
from typing import Union, Any
from ruamel.yaml import YAML

def read_yaml_file(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as yaml_file:
        yaml = YAML(typ='safe')
        return yaml.load(yaml_file)

def get_expected_text(file_name: str, text: str) -> str:
    expected_text = read_yaml_file(path.join(EXPECTED_TEXT, file_name))
    return expected_text[text]