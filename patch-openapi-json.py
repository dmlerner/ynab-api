import json
import sys
from collections import defaultdict

api = json.loads(sys.stdin.read())

schemas = api['components']['schemas']
for k, v in schemas.items():
  required = set(defaultdict(list, v)['required'])
  if 'properties' not in v:
    continue
  not_required = set(v['properties'].keys()) - required
  for pk in not_required:
    v['properties'][pk]['nullable'] = True

sys.stdout.write(json.dumps(api, indent=2))
