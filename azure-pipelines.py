#!/usr/bin/env python3

import json
import os

matrix = {name.split('-')[0]: dict(ContainerName=name) for name in os.listdir(os.getcwd()) if os.path.isdir(name) and name.endswith('-test-container')}

var_name = 'containers'
var_value = json.dumps(matrix, sort_keys=True)

# logging command
# see https://docs.microsoft.com/en-us/azure/devops/pipelines/scripts/logging-commands?view=azure-devops&tabs=bash
print(f'##vso[task.setVariable variable={var_name};isOutput=true]{var_value}')
