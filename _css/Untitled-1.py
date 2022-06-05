import json
carros_json='{"marca":"Honda","modelo":"HRV","cor":"prata"}'
carros=json.loads(carros_json)
print(carros['marca'])