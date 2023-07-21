###############################################################################
# validators.py
# Author: Tom Kerr AB3GY
#
# Text entry validator functions for the simplelog application.
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
import re

# Local packages.


##############################################################################
# Globals.
##############################################################################


##############################################################################
# Functions.
##############################################################################

# ------------------------------------------------------------------------        
def callsign_validator(why, where, what, all):
    """
    Validate allowable characters in callsigns.
    Does not attempt to validate actual callsigns or callsign formats.
    
    Parameters
    ----------
    why : int
        Action code: 0 for an attempted deletion, 1 for an attempted 
        insertion, or -1 for everything else.
    where : int
        Index of the beginning of the insertion or deletion.
    what : str
        The text being inserted or deleted.
    all : str
        The value that the text will have if the change is allowed. 
    Returns
    -------
    status : bool
        True if the character string is allowable, False otherwise.
    """
    #print(str(why), str(what))
    pat = re.compile('[a-zA-Z0-9\/]+') 
    if (why != '1'): return True # 1 = insertion
    if (pat.fullmatch(what)): return True
    return False

# ------------------------------------------------------------------------        
def date_validator(why, where, what, all):
    """
    Validate a date in one of these formats:
        YYYY-MM-DD
        MM/DD/YY
        MM/DD/YYYY
    Does not validate months, day, or years (i.e., 99/99/9999 is allowed).

    See callsign_validator() for a description of the parameters and return value.
    """
    #print(str(why), str(where), str(what), str(all))
        
    # YYYY-MM-DD patterns.
    pat1 = re.compile('\d{1,4}\-?')
    pat2 = re.compile('\d{4}\-\d{1,2}')
    pat3 = re.compile('\d{4}\-\d{2}\-?')
    pat4 = re.compile('\d{4}\-\d{2}\-\d{1,2}')
        
    # MM/DD/YY and MM/DD/YYYY patterns.
    pat5 = re.compile('\d{1,2}\/?')
    pat6 = re.compile('\d{1,2}\/\d{1,2}\/?')
    pat7 = re.compile('\d{1,2}\/\d{1,2}\/\d{1,4}')
        
    if (why != '1'): return True # 1 = insertion
    if pat1.fullmatch(all): return True
    if pat2.fullmatch(all): return True
    if pat3.fullmatch(all): return True
    if pat4.fullmatch(all): return True
    if pat5.fullmatch(all): return True
    if pat6.fullmatch(all): return True
    if pat7.fullmatch(all): return True
    return False
    
# ------------------------------------------------------------------------        
def frequency_validator(why, where, what, all):
    """
    Validate a 10-digit frequency with one decimal point.
    Does not try to validate a valid amateur frequency (999.999999 is allowed)
    
    See callsign_validator() for a description of the parameters and return value.
    """
    #print(str(why), str(where), str(what), str(all))
    pat = re.compile('\d*\.\d*')
    if (why != '1'): return True          # 1 = insertion
    if (len(all) > 10): return False      # Max 10 characters
    if what.isnumeric(): return True      # Numerics OK
    if (all.count('.') > 1): return False # Only one decimal allowed
    if pat.fullmatch(what): return True   # Frequency pattern match
    return False
    
# ------------------------------------------------------------------------        
def power_validator(why, where, what, all):
    """
    Validate a TX power field.
    Allows up to 4 digits.

    See callsign_validator() for a description of the parameters and return value.
    """
    #print(str(why), str(where), str(what), str(all))
    if (why != '1'): return True      # 1 = insertion
    if (len(all) > 4): return False   # Max 4 digits
    if what.isnumeric(): return True
    return False
  
# ------------------------------------------------------------------------        
def rst_validator(why, where, what, all):
    """
    Validate RST values and FT8 SNR reports.
    
    See callsign_validator() for a description of the parameters and return value.
    """
    # Validates RST values and FT8 SNR reports.
    #print(str(why), str(where), str(what), str(all))
    idx = int(where)
    rst1 = re.compile('[1-5]')
    rst2 = re.compile('[1-5][1-9]')
    rst3 = re.compile('[1-5][1-9][1-9]')
    snr = re.compile('[\+\-]\d{0,2}')
    if (why != '1'): return True # 1 = insertion
    if rst1.fullmatch(all): return True
    if rst2.fullmatch(all): return True
    if rst3.fullmatch(all): return True
    if snr.fullmatch(all):  return True # FT8 SNR
    return False

# ------------------------------------------------------------------------        
def sig_info_validator(why, where, what, all):
    """
    Validate the SIG_INFO field.
    Validates any combination of letter, numbers and a dash. The order of
    the characters is not validated.

    See callsign_validator() for a description of the parameters and return value.
    """
    #print(str(why), str(where), str(what), str(all))
    pat = re.compile('[a-zA-Z0-9\-]+')
    if (why != '1'): return True      # 1 = insertion
    if pat.fullmatch(what): return True
    return False

# ------------------------------------------------------------------------        
def state_validator(why, where, what, all):
    """
    Validate a state field.
    The ADIF STATE field contains the Primary Administrative Subdivision
    of a particular DXCC, which are enumerations containing 1-3 letters 
    or numbers.
 
    See callsign_validator() for a description of the parameters and return value.
    """
    #print(str(why), str(where), str(what), str(all))
    pat = re.compile('[a-zA-Z0-9]{1,3}')
    if (why != '1'): return True      # 1 = insertion
    if pat.fullmatch(all): return True
    return False

# ------------------------------------------------------------------------        
def text_validator(why, where, what, all):
    """
    Validates a general text field.
    Eliminates problem characters from commens and general text:
        double quote ("), backslash (\)
    
    See callsign_validator() for a description of the parameters and return value.
    """
    #print(str(why), str(where), str(what), str(all))
    if (why != '1'): return True   # 1 = insertion
    if '"' in what: return False   # No double quotes
    if '\\' in what: return False  # No backslash
    return True

# ------------------------------------------------------------------------
def time_validator(why, where, what, all):
    """
    Validate a time in HH:MM format.
    See callsign_validator() for a description of the parameters and return value.
    """
    #print(str(why), str(where), str(what), str(all))
    
    # HH:MM patterns.
    pat1 = re.compile('\d{1,2}')
    pat2 = re.compile('\d{1,2}\:\d{0,2}')
    if (why != '1'): return True  # 1 = insertion
    if pat1.fullmatch(all): return True
    if pat2.fullmatch(all): return True
    return False

