#!/usr/bin/bash
SCRIPT_DIR=$(cd $(dirname "${BASH_SOURCE[0]}") && pwd)
source "$SCRIPT_DIR/.venv/bin/activate"
cd "$SCRIPT_DIR/{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}" && nohup python ./run.py &
deactivate
