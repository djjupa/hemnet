#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011 Casey Link <unnamedrambler@gmail.com>
# Copyright (C) 2012 Hugo Lindström <hugolm84@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Contains information regarding caching behavior
"""

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
import shove
import os

from datetime import datetime, timedelta

try:
    OUTPUT_DIR = os.environ['OUTPUT_DIR']
except KeyError:
    OUTPUT_DIR = '/Users/hugo/cache/hemnet'

HTTP_CACHE_DIR = OUTPUT_DIR + '/http'
MAX_THREADS=5
TTL=3600


cache_opts = {
    'cache.type': 'file',
    'cache.data_dir': OUTPUT_DIR+'/cache/data',
    'cache.lock_dir': OUTPUT_DIR+'/cache/lock'
}

# Default expires next day at 1AM
def timedeltaUntilDays(days=1, hour=1) :
    today = datetime.utcnow()
    expires = datetime.replace(today + timedelta(days=days), hour=hour, minute=0, second=0)
    return dict({"expires" : expires-today, "date" : expires, 'seconds' :  (expires-today).total_seconds() })


def setCacheControl(header, expiresInSeconds):
    today = datetime.utcnow()
    expires = today + timedelta(seconds=expiresInSeconds)
    header.add("Expires", int((expires - datetime.utcfromtimestamp(0)).total_seconds()))
    header.add("Max-Age" , int(expiresInSeconds))
    header.add("Last-Modified" , today.strftime("%a, %d %b %Y %H:%M:%S +0000"))
    header.add("Date-Expires" , expires.strftime("%a, %d %b %Y %H:%M:%S +0000"))
    return header;


methodcache = CacheManager(**parse_cache_config_options(cache_opts))

storage = shove.Shove("file://"+OUTPUT_DIR+'/storage', optimize=False)
locations = shove.Shove("file://"+OUTPUT_DIR+'/locations', optimize=False)
