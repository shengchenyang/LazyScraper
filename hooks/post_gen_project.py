import os
import shutil

REMOVE_PATHS = []

source_control = "{{ cookiecutter.source_control }}"
if source_control == "github":
    REMOVE_PATHS.extend((".gitlab", ".gitlab-ci.yml"))
elif source_control == "gitlab":
    REMOVE_PATHS.append(".github")

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
