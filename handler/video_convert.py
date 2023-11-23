from moviepy.video.io import VideoFileClip

def convert_video(a):
    video = VideoFileClip('uploads/' + a)
    video = video.cutout(90, 150)
    # Сохранение
    video.write_videofile("new_video/new_" + a, fps=30)