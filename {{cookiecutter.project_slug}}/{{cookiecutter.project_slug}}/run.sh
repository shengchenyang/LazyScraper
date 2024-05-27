#!/usr/bin/bash
SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
ROOT_DIR=$(dirname "$SCRIPT_DIR")
source "$ROOT_DIR/.venv/bin/activate"
cd "$ROOT_DIR/{{cookiecutter.project_slug}}" && nohup python ./run.py &
deactivate
