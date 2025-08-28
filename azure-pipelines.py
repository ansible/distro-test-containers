#!/usr/bin/env python3

from __future__ import annotations

import json
import pathlib
import re

matrix: dict[str, dict[str, str]] = {}

for container in (pathlib.Path(__file__).parent / 'containers').iterdir():
    for version in container.iterdir():
        name = re.sub(r'\W', '_', f'{container.name}-{version.name}', flags=re.ASCII)

        matrix[name] = dict(
            ContainerName=f'{container.name}-test-container',
            ContainerVersion=version.name,
            ContainerContext=str(version),
        )

var_name = 'containers'
var_value = json.dumps(matrix, sort_keys=True)

# logging command
# see https://docs.microsoft.com/en-us/azure/devops/pipelines/scripts/logging-commands?view=azure-devops&tabs=bash
print(f'##vso[task.setVariable variable={var_name};isOutput=true]{var_value}')
