import os
import yaml
import sys
import logging

from spotipy import Spotify
from spotipy import util


def check_config(config, dir_path):
    for key in ['username', 'client_secret', 'client_id']:
        if key not in config or config.get(key) is None:
            logging.warning(
                """Config is invalid. {} key is empty or does not exist.
                   Config file can be found at: {}/config.yaml
                """.format(key, dir_path)
            )
            sys.exit(-1)


def akttym():
    SCOPE = 'user-library-modify,user-read-playback-state'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config = yaml.safe_load(open(dir_path + '/config.yaml'))
    check_config(config, dir_path)

    token = util.prompt_for_user_token(
        config['username'],
        SCOPE,
        client_id=config['client_id'],
        client_secret=config['client_secret'],
        redirect_uri='http://localhost:1911/',
        cache_path=dir_path + '/cache'
    )

    if token:
        sp = Spotify(auth=token)
        track = sp.current_playback()
        if track is not None:
            sp.current_user_saved_tracks_add([track['item']['id']])
            logging.warning("added %s to %s's library", track['item']['name'], config['username'])
        else:
            logging.warning("nothing is playing currently, aborting")
    else:
        logging.warning("Can't get token for %s", config['username'])
