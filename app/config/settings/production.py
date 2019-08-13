from .base import *

secrets = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))
