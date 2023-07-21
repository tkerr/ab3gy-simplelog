###############################################################################
# WidgetQsoEntry.py
# Author: Tom Kerr AB3GY
#
# WidgetQsoEntry class for use with the simplelog application.
# Implements a QSO entry UI frame for entering amateur radio contacts.
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
from datetime import datetime, timezone

# Tkinter packages.
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

# Local packages.
import globals
from adif import adif, freq2band
from TextFile import TextFile
from src.simplelogUtils import format_adif
from src.WidgetButton import WidgetButton
from src.WidgetComboBox import WidgetComboBox
from src.WidgetTextEntry import WidgetTextEntry
from src.validators import callsign_validator, date_validator, \
    frequency_validator, rst_validator, text_validator, time_validator

##############################################################################
# Globals.
##############################################################################


##############################################################################
# Functions.
##############################################################################

    
##############################################################################
# WidgetQsoEntry class.
##############################################################################
class WidgetQsoEntry(object):
    """
    WidgetQsoEntry class for use with the simplelog application.
    Implements a QSO entry UI frame for entering amateur radio contacts.
    """
    # ------------------------------------------------------------------------
    def __init__(self, root):
        """
        Class constructor.
        
        Parameters
        ----------
        root : Tk object
            The root object containing the QSO entry frame.

        Returns
        -------
        None.
        """
        # The QSO entry frame.
        self.frame = ttk.Frame(root)
        
        # Dictionary of UI widgets containing log data.
        self.widgets = {
            'BAND'     : None,
            'CALL'     : None,
            'COMMENT'  : None,
            'FREQ'     : None,
            'MODE'     : None,
            'QSO_DATE' : None,
            'RST_RCVD' : None,
            'RST_SENT' : None,
            'TIME_ON'  : None,
        }

        self.init()

    # ------------------------------------------------------------------------        
    def _grid_add(self, widget, row, col, colspan=1):
        """
        Add the GUI widget to the main grid at the specified row and column.
        """
        widget.frame.grid(
            row=row,
            column=col,
            columnspan=colspan,
            padx=3,
            pady=3,
            sticky='EW')
    # ------------------------------------------------------------------------
    def _set_band(self, *args):
        """
        Set BAND field based on the currently entered frequency.
        """
        #print(args)
        freq_khz = self.widgets['FREQ'].get_value()
        if (len(freq_khz) > 0):
            freq_mhz = float(freq_khz) / 1000.
            band = freq2band(freq_mhz)
            if (band == 'NONE'):
                self.widgets['BAND'].clear()  # Invalid frequency
            elif (len(band) > 0):
                self.widgets['BAND'].set_value(band)
        
    # ------------------------------------------------------------------------
    def _set_now(self):
        self._set_date()
        self._set_time()

    # ------------------------------------------------------------------------
    def _set_date(self):
        utc = datetime.now(timezone.utc)
        self.widgets['QSO_DATE'].set_value((f'{utc.year}-{utc.month:02}-{utc.day:02}'))

    # ------------------------------------------------------------------------
    def _set_time(self):
        utc = datetime.now(timezone.utc)
        self.widgets['TIME_ON'].set_value((f'{utc.hour:02}:{utc.minute:02}'))
    
    # ------------------------------------------------------------------------        
    def clear_qso(self):
        """
        Clear all QSO entry fields.
        """
        for widget in self.widgets:
            self.widgets[widget].clear()
    
    # ------------------------------------------------------------------------        
    def log_qso(self):
        """
        Log the QSO to the ADIF file.
        """
        my_adif = adif()
        for widget_name in self.widgets:
            widget = self.widgets[widget_name]
            field = widget.get_field()
            value = widget.get_value()
            
            # Format values in their expected ADIF formatting.
            value = format_adif(field, value)

            if (len(field) > 0) and (len(value) > 0):
                my_adif.set_field(field, value)
                
        #print(my_adif.get_adif())
        globals.log_file.append(my_adif.get_adif())
        
    # ------------------------------------------------------------------------
    def init(self):
        """
        Create and initialize the QSO entry frame.
        """
        row = 0
        column = 0

        # CALLSIGN text entry.
        self.widgets['CALL'] = WidgetTextEntry(self.frame, 
            title='Callsign', 
            field='CALL',
            validator=callsign_validator,
            to_upper=True)
        self._grid_add(self.widgets['CALL'], row, column)
        column += 1

        # RST SENT text entry.
        self.widgets['RST_SENT'] = WidgetTextEntry(self.frame, 
            title='RST Sent', 
            field='RST_SENT',
            validator=rst_validator)
        self._grid_add(self.widgets['RST_SENT'], row, column)
        column += 1
    
        # RST RCVD text entry.
        self.widgets['RST_RCVD'] = WidgetTextEntry(self.frame, 
            title='RST Rcvd', 
            field='RST_RCVD',
            validator=rst_validator)
        self._grid_add(self.widgets['RST_RCVD'], row, column)
        column += 1
        
        # LOG QSO button.
        btn_log_qso = WidgetButton(self.frame, 
            text='Log QSO', 
            command=self.log_qso)
        self._grid_add(btn_log_qso, row, column)
        column += 1
        
        # Clear QSO button.
        btn_clr_qso = WidgetButton(self.frame, 
            text='Clear QSO', 
            command=self.clear_qso)
        self._grid_add(btn_clr_qso, row, column)
        column += 1
        
        row += 1
        column = 0
        
        # QSO DATE text entry.
        self.widgets['QSO_DATE'] = WidgetTextEntry(self.frame, 
            title='Date', 
            field='QSO_DATE',
            validator=date_validator)
        self._grid_add(self.widgets['QSO_DATE'], row, column)
        column += 1
    
        # TIME ON text entry.
        self.widgets['TIME_ON'] = WidgetTextEntry(self.frame, 
            title='Time', 
            field='TIME_ON',
            validator=time_validator,)
        self._grid_add(self.widgets['TIME_ON'], row, column)
        column += 1
        
        # FREQUENCY text entry.
        self.widgets['FREQ'] = WidgetTextEntry(self.frame, 
            title='Frequency (KHz)', 
            field='FREQ',
            width=14,
            validator=frequency_validator)
        self._grid_add(self.widgets['FREQ'], row, column)
        self.widgets['FREQ'].bind('<FocusOut>', self._set_band)
        column += 1

        # BAND combo box.
        self.widgets['BAND'] = WidgetComboBox(self.frame, 
            title='Band', 
            field='BAND',
            width=10,
            values=TextFile('bands.txt').readlines())
        self._grid_add(self.widgets['BAND'], row, column)
        column += 1
    
        # MODE combo box.
        self.widgets['MODE'] = WidgetComboBox(self.frame, 
            title='Mode', 
            field='MODE',
            width=10,
            values=TextFile('modes.txt').readlines())
        self._grid_add(self.widgets['MODE'], row, column)
        column += 1
        
        row += 1
        column = 0
        
        # NOW button.
        btn_now = tk.Button(self.frame,
            text = 'Now',
            width = 8,
            font=tkFont.Font(size=10),
            command=self._set_now)
        btn_now.grid(
            row=row,
            column=column,
            padx=3,
            pady=3)
            
        row += 1
        column = 0
        
        # COMMENT text entry.
        self.widgets['COMMENT'] = WidgetTextEntry(self.frame, 
            title='Comment', 
            field='COMMENT',
            width=74,
            validator=text_validator)
        self._grid_add(self.widgets['COMMENT'], row, column, colspan=5)
        column += 1

        # Set focus to the callsign entry field.
        self.widgets['CALL'].set_focus()


##############################################################################
# Main program.
############################################################################## 
if __name__ == "__main__":
    print('WidgetQsoEntry main program not implemented.')
   