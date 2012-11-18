#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pySFML2 - Cython SFML Wrapper for Python
# Copyright 2012, Jonathan De Wachter <dewachter.jonathan@gmail.com>
#
# This software is released under the GPLv3 license.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sfml as sf
import client, server

try:
    # python 2 compatability
    input = raw_input
except NameError:
    pass
# choose a random port for opening sockets (ports < 1024 are reserved)
PORT = 2435

# client or server ?
print("Do you want to be a server (s) or a client (c) ?")
who = input()

if who == 's':
	server.do_server(PORT)
else:
	client.do_client(PORT)

input("Press any key to exit...")
