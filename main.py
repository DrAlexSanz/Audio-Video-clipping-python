from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
os.chdir(r"C:\Users\MY_DIR")
start_time = 2640 # Time in seconds
end_time = 3240
test_vid = ffmpeg_extract_subclip(r"Del44al54.avi", start_time, end_time, targetname=r"C:\Users\MY_FILE.mp4")
