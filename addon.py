#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright 2016 PrimeAsiaTV.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from xbmcswift import Plugin, xbmc, xbmcgui

 


PLUGIN_NAME = 'PrimeAsiaTV'
PLUGIN_ID = 'plugin.video.primeasiatv'


plugin = Plugin(PLUGIN_NAME, PLUGIN_ID, __file__)
 


 
  

@plugin.route('/', default=True)
def show_homepage():
    items = [
        # Live
        {'label': 'Watch Live TV',
         'url': plugin.url_for('live_tv')},      
    ]
    return plugin.add_items(items)


@plugin.route('/live/')
def live_tv():
    rtmpurl = 'rtsp://158.69.124.9:1935/primeasia/primeasia'
    li = xbmcgui.ListItem('PrimeAsiaTV Live')
    xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(rtmpurl, li)
    # Return an empty list so we can test with plugin.crawl() and
    # plugin.interactive()
    return []

 
if __name__ == '__main__':
    plugin.run()
