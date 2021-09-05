from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pydub import AudioSegment

remove_intro_1 = ffmpeg_extract_subclip(r"C:\Users\asanz\Desktop\Podcasts\C0NSULT0RIO 1.mp3", 55, 5460, targetname=r"C:\Users\asanz\Desktop\Podcasts\parte 1.mp3")

remove_intro_2 = ffmpeg_extract_subclip(r"C:\Users\asanz\Desktop\Podcasts\CONSULTORIO 2.mp3", 44, 5638, targetname=r"C:\Users\asanz\Desktop\Podcasts\parte 2.mp3")

combine_1 = AudioSegment.from_file(r"C:\Users\asanz\Desktop\Podcasts\parte 1.mp3", format="mp3")
combine_2 = AudioSegment.from_file(r"C:\Users\asanz\Desktop\Podcasts\parte 2.mp3", format="mp3")

consultorio_05_sep = combine_1 + combine_2

# Now this will take a bit if it's long. About 1 min for 2x90 min podcasts
consultorio_05_sep.export(r"C:\Users\asanz\Desktop\Podcasts\consultorio_05_sep.mp3", format = "mp3")


