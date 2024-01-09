from moviepy.editor import *

def convert_to_mp3(mp4_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile('new_audio.mp3')
    audio.close()
    video.close()


if __name__ == "__main__":
    input_mp4 = input('The path to the file')
    convert_to_mp3(input_mp4)