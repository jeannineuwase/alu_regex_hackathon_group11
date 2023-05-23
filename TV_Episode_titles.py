import re

pattern = r".+ S\d{2}E\d{2}"
title = "Ginny and Georgia S01E01"
 if re.match(pattern, title):
            return True
        else:
            return False
  
  
