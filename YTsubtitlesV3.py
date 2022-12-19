from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import json
import pandas as pd
  
# first get a transcript from video using id
transcript = YouTubeTranscriptApi.get_transcript("veEQQ-N9xWU")

# format transcript to json
formatter = JSONFormatter()
json_formatted = formatter.format_transcript(transcript)

# write transcript to a file
with open('your_filename.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)

# use pandas to try format json to plain txt file
df = pd.read_json (r'C:\Users\sheld\Documents\Projects\Coding\Python\YT Ted\your_filename.json')
df.to_csv (r'C:\Users\sheld\Documents\Projects\Coding\Python\YT Ted\transcript.txt', index = False)