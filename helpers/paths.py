from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / 'config'
ENVS = CONFIG_DIR / 'envs.yaml'
EXPECTED_TEXT = CONFIG_DIR / 'expected_text'