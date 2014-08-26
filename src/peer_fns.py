# This code is distributed under the GNU General Public License (see
# THE_GENERAL_GNU_PUBLIC_LICENSE.txt for extending this information).
# Copyright (C) 2014, the P2PSP team.
# http://www.p2psp.org

# {{{ Imports

import threading
import sys
from peer_ims import Peer_IMS
from peer_dbs import Peer_DBS
from _print_ import _print_
from color import Color

# }}}

# FNS: Full-cone Nat Set of rules
class Peer_FNS(Peer_DBS):
    # {{{

    def __init__(self, peer):
        # {{{

        sys.stdout.write(Color.yellow)
        _print_("Peer FNS")
        sys.stdout.write(Color.none)

        threading.Thread.__init__(self)

        self.splitter_socket = peer.splitter_socket
        self.player_socket = peer.player_socket
        self.buffer_size = peer.buffer_size
        self.chunk_format_string = peer.chunk_format_string
        self.splitter = peer.splitter
        self.chunk_size = peer.chunk_size
        self.peer_list = peer.peer_list
        self.debt = peer.debt

        # }}}

    def say_hello(self, node):
        # {{{

        self.team_socket.sendto('H', node)

        # }}}

    def say_goodbye(self, node):
        # {{{

        self.team_socket.sendto('G', node)

        # }}}

    def disconnect_from_the_splitter(self):
        # {{{

        Peer_IMS.disconnect_from_the_splitter(self)
        self.say_hello(self.splitter)
        self.say_hello(self.splitter)
        self.say_hello(self.splitter)

        # }}}
        
    # }}}
