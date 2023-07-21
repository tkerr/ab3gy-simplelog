###############################################################################
# globals.py
# Author: Tom Kerr AB3GY
#
# Global objects and data for the simplelog application.
#
# Designed for personal use by the author, but available to anyone under the
# license terms below.
###############################################################################

###############################################################################
# License
# Copyright (c) 2023 Tom Kerr AB3GY (ab3gy@arrl.net).
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,   
# this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,  
# this list of conditions and the following disclaimer in the documentation 
# and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without 
# specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.
###############################################################################

# System level packages.
import os

# Tkinter packages.
import tkinter as tk

# Local packages.
from ConfigFile import ConfigFile


##############################################################################
# Globals.
##############################################################################
APP_NAME = 'simplelog'
APP_VERSION = '0.1'
APP_COPYRIGHT = '2023'

NUM_USER_FIELDS = 4  # Number of user-defined fields

root = None          # The root window
config = None        # The config file object
qso_entry = None     # The QSO entry frame

# ADIF log file.
log_name = os.path.join('log', 'simplelog_log.adi')
log_file = None


##############################################################################
# Functions.
##############################################################################

# ------------------------------------------------------------------------
def init():
    """
    Initialize global settings.
    """
    global config

    # Read the configuration file.
    # TBD - Uncomment when config file is in service.
    #config = ConfigFile()
    #config.read()
   
# ------------------------------------------------------------------------
def close():
    """
    Gracefully persist all settings and shutdown all threads.
    """
    global config
    # TBD - Uncomment when config file is in service.
    #config.write()

# ------------------------------------------------------------------------
