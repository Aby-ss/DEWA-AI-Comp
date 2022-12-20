import moviepy
import moviepy.editor as moviepy

from rich.traceback import install
install(show_locals=True)

clip = moviepy.VideoFileClip("output.avi")
clip.write_videofile("Vid.mp4")