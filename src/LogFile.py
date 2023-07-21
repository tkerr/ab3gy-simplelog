###############################################################################
# LogFile.py
# Author: Tom Kerr AB3GY
#
# LogFile class.
# Implements a class for creating and writing ADIF log files.
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
import sys

# Local packages.


##############################################################################
# Globals.
##############################################################################


##############################################################################
# Functions.
##############################################################################


##############################################################################
# LogFile class.
##############################################################################
class LogFile(object):
    """
    LogFile class.
    Implements a class for creating and writing ADIF log files.
    """
    
    # ------------------------------------------------------------------------
    def __init__(self, filename='', create=True):
        """
        Class constructor.
    
        Parameters
        ----------
        filename : str
            The optional log file name.  Must be specified in the append() method
            if not specified here.
        create : bool
            If True and filename is specified, then log file is created if it does not exist.
        
        Returns
        -------
        None.
        """
        self.filename = filename
        self._my_class = self.__class__.__name__
        
        if (len(self.filename) > 0) and create:
            if not os.path.isfile(self.filename):
                self._create()

    # ------------------------------------------------------------------------
    def _print_msg(self, msg):
        """
        Print an error message.
        
        Parameters
        ----------
        msg : str
            The error message to print.
        
        Returns
        -------
        None
        """
        print('{}: {}'.format(self._my_class, msg))

    # ------------------------------------------------------------------------
    def _create(self):
        """
        Create an ADIF log file.
        
        Parameters
        ----------
        None.
        
        Returns
        -------
        ok : bool
            True if file created successfully, False otherwise.
        """
        ok = False
        
        # Make sure we have a file name.
        if (len(self.filename) == 0):
            self._print_msg('No filename specified')
            return ok

        # Create the file and add an ADIF header.
        try:
            hdr = 'ADIF log file created by {}\n<EOH>\n'.format(os.path.basename(sys.argv[0]))
            with open(self.filename, 'w') as fd:
                fd.write(hdr)
            ok = True
        except Exception as err:
            self._print_msg('Error creating {}: {}'.format(self.filename, str(err)))
        return ok
        
    # ------------------------------------------------------------------------
    def append(self, record, filename=''):
        """
        Append an ADIF record to the log file.
        
        Parameters
        ----------
        record : str
            The complete ADIF record to append.
        filename : str
            The optional log file name.  Must have been specified in the constructor
            if not specified here.
        
        Returns
        -------
        ok : bool
            True if file append is successful, False otherwise.
        """
        ok = False
        
        # Make sure we have a file name.
        if (len(filename) > 0):
            self.filename = filename
        if (len(self.filename) == 0):
            self._print_msg('No filename specified')
            return ok
        
        # Create the log file if needed.
        if not os.path.isfile(self.filename):
            if not self._create():
                return ok
        
        # Append to the log file.
        try:
            with open(self.filename, 'a') as fd:
                fd.write('{}\n'.format(record))
            ok = True
        except Exception as err:
            self._print_msg('Error writing {}: {}'.format(self.filename, str(err)))
        return ok

 
##############################################################################
# Main program.
############################################################################## 
if __name__ == "__main__":
    
    my_filename = 'testfile.adi'
    my_file = LogFile(my_filename)
    my_file.append('<CALL:5>AB3GY <EOR>') 
    my_file.append('<CALL:5>K3MJW <EOR>') 
    my_file.append('<CALL:4>W3GH <EOR>') 
