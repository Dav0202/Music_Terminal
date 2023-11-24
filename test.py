from pytify.core.search import search_artist
from pytify.core.request import read_config
from pytify.auth.auth import authenticate
from pprint import pprint as pp

config = read_config()

auth = authenticate(config)
results = search_artist('Rihanna', auth)
pp(results)