"""
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

© Omar Junaid
"""

import os


def ls_in_directory(path):
    """List all scripts (.py files) in a directory.

    This returns a List object (you guessed it).
    Just pass the path."""
    for file in os.listdir(path):
        if file.endswith(".py"):
            print(file)
