###############################################################################
# WidgetButton.py
# Author: Tom Kerr AB3GY
#
# WidgetButton class for use with the simplelog application.
# Provides a framed button for GUI actions.
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

# Tkinter packages.
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

# Local packages.
import globals


##############################################################################
# Globals.
##############################################################################


##############################################################################
# Functions.
##############################################################################

    
##############################################################################
# WidgetButton class.
##############################################################################
class WidgetButton(object):
    """
    WidgetButton class for use with the simplelog application.
    Provides a framed button for GUI actions.
    """
    # ------------------------------------------------------------------------
    def __init__(self, parent, text, command,
        width=12, 
        readonly = True,
        title_padx = 3,
        title_pady = 3,
        title_size = 10,
        entry_padx = 3,
        entry_pady = 3,
        entry_size = 10,):
        """
        Class constructor.
        
        Parameters
        ----------
        parent : Tk object
            The parent object containing the widget
        text : str
            The button text to display
        command : str
            The command to execute when the button is clicked
        width : int
            The button width in characters

        Returns
        -------
        None.
        """
        self.parent = parent
        self.frame = tk.Frame(parent)
        #self.frame = tk.Frame(parent,
        #    highlightbackground="blue",
        #    highlightthickness=2)
        self._button = None          # The button widget
        self._text = text            # The button text to display
        self._command = command      # The button command to execute
        

        self.readonly = readonly
        self.title_padx = title_padx           # Title x padding
        self.title_pady = title_pady           # Title y padding
        self.title_font_size = title_size      # Title font size
        self.widget_padx = entry_padx          # Combo box x padding
        self.widget_pady = entry_pady          # Combo box y padding
        self.widget_font_size = entry_size     # Combo box font size
        self.widget_width = width              # Combo box text width
        
        self.init()
    
    

    # ------------------------------------------------------------------------
    def set_focus(self):
        """
        Set focus to the button.
        """
        self._button.focus_set()

    # ------------------------------------------------------------------------
    def bind(self, event, bind_fn):
        """
        Bind a function or method to a text entry event.
        
        Parameters
        ----------
        event : str
            The event to bind, e.g., '<Return>', '<FocusOut>', etc.
        bind_fn : function
            The function to execute when the event occurs
            The function has the signature bind_fn(*args)

        Returns
        -------
        None.
        """
        self._button.bind(event, bind_fn)

    # ------------------------------------------------------------------------
    def init(self):
        """
        Method to create and initialize the button widget.
        """
        # Create a blank label for proper GUI spacing.
        dummy_label = tk.Label(self.frame,
            text = '  ',
            font=tkFont.Font(size=self.title_font_size))
        dummy_label.grid(
            row=0,
            column=0,
            padx=self.title_padx,
            pady=(self.title_pady,0))
            
        # Create the button widget.
        self._button = tk.Button(self.frame,
            text = self._text,
            width = self.widget_width,
            font=tkFont.Font(size=self.widget_font_size),
            command=self._command)
        self._button.grid(
            row=1,
            column=0,
            padx=self.widget_padx,
            pady=(0, self.widget_pady))


##############################################################################
# Main program.
############################################################################## 
if __name__ == "__main__":
    print('WidgetButton main program not implemented.')
   