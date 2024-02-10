#!/usr/bin/python3
"""Fabric script to clean outdated archives"""

from fabric.api import env, run, local
from datetime import datetime
import os

# Set the environment variables
env.hosts = ['ubuntu@100.25.135.254', 'ubuntu@54.160.74.210']
env.key_filename = '~/path/to/your/private/key'

def do_clean(number=0):
    """Deletes out-of-date archives."""
    try:
        number = int(number)
    except ValueError:
        return

    if number < 0:
        return

    # Local cleanup
    local("ls -1t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number + 1))

    # Remote cleanup
    run("ls -1t /data/web_static/releases | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number + 1))
