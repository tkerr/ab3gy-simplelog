###############################################################################
# WidgetComboBox.py
# Author: Tom Kerr AB3GY
#
# WidgetComboBox class for use with the simplelog application.
# Provides a labeled drop-down box for GUI selection of log field values.
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
# WidgetComboBox class.
##############################################################################
class WidgetComboBox(object):
    """
    WidgetComboBox class for use with the simplelog application.
    Provides a labeled drop-down box for GUI selection of log field values.
    """
    # ------------------------------------------------------------------------
    def __init__(self, parent, title, field, values,
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
        title : str
            The widget title to be displayed in the GUI
        field : str
            The ADIF field name of the log entry
        values : list
            List of strings to appear as the combo box choices
        width : int
            The combo box width in characters
        readonly : bool
            Set the combo box choices to read-only if True

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
        self._combo_widget = None              # Combo box widget used to select log info
        self._value = tk.StringVar(self.frame) # Combo box value
        self._values = values                  # Combo box list of choices

        self.readonly = readonly
        self.title_padx = title_padx           # Title x padding
        self.title_pady = title_pady           # Title y padding
        self.title_font_size = title_size      # Title font size
        self.widget_padx = entry_padx          # Combo box x padding
        self.widget_pady = entry_pady          # Combo box y padding
        self.widget_font_size = entry_size     # Combo box font size
        self.widget_width = width              # Combo box text width
        
        self.LABEL_BG = 'SlateGray1'
        
        self.set_title(title)
        self.init()
    
    # ------------------------------------------------------------------------
    def clear(self):
        """
        Clear the text entry widget.
        """
        self.set_value('')

    # ------------------------------------------------------------------------
    def set_focus(self):
        """
        Set focus to the combo box.
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
        
        # Create the combo box widget.
        self._entry_widget = ttk.Combobox(self.frame,
            width = self.widget_width,
            textvariable=self._value,
            font=tkFont.Font(size=self.widget_font_size))
        self._entry_widget['values'] = self._values
        if self.readonly:
            self._entry_widget['state'] = 'readonly'
        self._entry_widget.grid(
            row=1,
            column=0,
            padx=self.widget_padx,
            pady=(0, self.widget_pady))


##############################################################################
# Main program.
############################################################################## 
if __name__ == "__main__":
    print('WidgetComboBox main program not implemented.')
   