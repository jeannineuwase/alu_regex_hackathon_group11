import re
pattern = r'\[Verse \d+\] .+'

lyrics = "[Verse 2] This is the third verse of the song"
match = re.match(pattern, lyrics)

if match:
    print("Lyrics found!")
else:
    print("Lyrics not found.")
