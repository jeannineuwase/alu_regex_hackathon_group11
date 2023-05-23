import re

title = input('Insert the tv episode title')
pattern = r".+ S\d{2}E\d{2}"

def match_episode_title(title):
 if re.match(pattern, title):
            return True
        else:
            return False
  
