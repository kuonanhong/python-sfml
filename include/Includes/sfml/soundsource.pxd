# PySFML - Python bindings for SFML
# Copyright (c) 2012-2016, Jonathan De Wachter <dewachter.jonathan@gmail.com>
#                          Edwin Marshall <emarshall85@gmail.com>
#
# This file is part of PySFML project and is available under the zlib
# license.

cdef extern from "SFML/Audio.hpp" namespace "sf::SoundSource":
    cdef enum Status:
        Stopped
        Paused
        Playing
