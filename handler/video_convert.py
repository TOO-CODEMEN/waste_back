import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

from moviepy.editor import VideoFileClip
class VideoConvert():
    @staticmethod
    def start(path):
        #'model/uploads/' + path
        video = VideoFileClip(os.path.abspath('model/uploads/') + '\\' + path)
        # video = video.cutout(0, 115)

        video = video.cutout(0, 90)
        video = video.cutout(150, 240)
        # video = video.cutout(135, 240)
#C:\\Users\\Администратор\\PycharmProjects\\waste_back
        # Сохранение
        video.write_videofile(os.path.abspath("model/saves/new_") + path, fps=5)


if __name__ == "__main__":
    VideoConvert()