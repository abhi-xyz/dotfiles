import os
import subprocess
# from libqtile.command import lazy
from libqtile import hook

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

