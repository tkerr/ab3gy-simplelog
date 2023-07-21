###############################################################################
# WidgetTextEntry.py
# Author: Tom Kerr AB3GY
#
# WidgetTextEntry class for use with the simplelog application.
# Provides a labeled text entry box for GUI entry of log field values.
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
from src.validators import text_validator


##############################################################################
# Globals.
##############################################################################


##############################################################################
# Functions.
##############################################################################

    
##############################################################################
# WidgetTextEntry class.
##############################################################################
class WidgetTextEntry(object):
    """
    WidgetTextEntry class for use with the simplelog application.
    Provides a labeled text entry box for GUI entry of log field values.
    """
    # ------------------------------------------------------------------------
    def __init__(self, parent, title, field, 
        width=12, 
        to_upper = False,
        validator=None,
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
        title : str
            The widget title to be displayed in the GUI
        field : str
            The ADIF field name of the log entry
        width : int
            The text entry box width in characters
        to_upper : bool
            Converts characters to uppercase if True
        validator : function name
            The name of a validator callback function for the text entry.

        Returns
        -------
        None.
        """
        self.parent = parent
        self.frame = tk.Frame(parent)
        #self.frame = tk.Frame(parent,
        #    highlightbackground="blue",
        #    highlightthickness=2)
        
        self._title = tk.StringVar(self.frame) # Widget title to be displayed in GUI
        self._title_label = None               # Label object to display the title
        self._adif_field = field.upper()       # ADIF field name corresponding to this log entry
        self._entry_widget = None              # Text entry widget used to enter log info
        self._value = tk.StringVar(self.frame) # Text entry value
        self._validator_cb = None              # Registered validator callback function

        self.title_padx = title_padx           # Title x padding
        self.title_pady = title_pady           # Title y padding
        self.title_font_size = title_size      # Title font size
        self.widget_padx = entry_padx          # Entry object x padding
        self.widget_pady = entry_pady          # Entry object y padding
        self.widget_font_size = entry_size     # Entry object font size
        self.widget_width = width              # Entry text width
        self.to_upper = to_upper               # Convert text entries to uppercase if true
        
        self.LABEL_BG = 'SlateGray1'
        
        self.set_title(title)
        if validator is not None:
            self._validator_cb = self.frame.register(validator)
        else:
            self._validator_cb = self.frame.register(text_validator)
        self.init()
    
    # ------------------------------------------------------------------------
    def _to_upper(self, *args):
        """
        Convert the text entry to upper case.
        """
        self._value.set(self._value.get().upper())
    
    # ------------------------------------------------------------------------
    def clear(self):
        """
        Clear the text entry widget.
        """
        self.set_value('')
    
    # ------------------------------------------------------------------------
    def set_focus(self):
        """
        Set focus to the text entry box.
        """
        self._entry_widget.focus_set()
    
    # ------------------------------------------------------------------------
    def get_title(self):
        """
        Return the widget title string.
        """
        return self._title.get()
    
    # ------------------------------------------------------------------------
    def set_title(self, value):
        """
        Set the widget title.
        """
        self._title.set(str(value))
    
    # ------------------------------------------------------------------------
    def get_value(self):
        """
        Return the text entry value.
        """
        return self._value.get()
    
    # ------------------------------------------------------------------------
    def set_value(self, value):
        """
        Set the text entry value.
        Note that this value is not validated.
        """
        self._value.set(str(value))
    
    # ------------------------------------------------------------------------
    def get_field(self):
        """
        Return the ADIF field name string.
        """
        return self._adif_field.upper()
    
    # ------------------------------------------------------------------------
    def set_field(self, value):
        """
        Set the ADIF field name.
        """
        self._adif_field = (str(value).upper())

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
        self._entry_widget.bind(event, bind_fn)

    # ------------------------------------------------------------------------
    def init(self):
        """
        Method to create and initialize the UI widget.
        """
        self.clear()
        
        # Create the widget title label.
        self._title_label = tk.Label(self.frame,
            textvariable = self._title,
            font=tkFont.Font(size=self.title_font_size))
        self._title_label.grid(
            row=0,
            column=0,
            sticky='W',
            padx=self.title_padx,
            pady=(self.title_pady,0))
        
        # Create the text entry widget.
        self._entry_widget = tk.Entry(self.frame,
            width = self.widget_width,
            textvariable=self._value,
            font=tkFont.Font(size=self.widget_font_size),
            validate='key',
            validatecommand=(self._validator_cb, '%d', '%i', '%S', '%P'))
        self._entry_widget.grid(
            row=1,
            column=0,
            padx=self.widget_padx,
            pady=(0, self.widget_pady))
        if self.to_upper:
            self._value.trace_add('write', self._to_upper) # Convert all letters to uppercase


##############################################################################
# Main program.
############################################################################## 
if __name__ == "__main__":
    print('WidgetTextEntry main program not implemented.')
   