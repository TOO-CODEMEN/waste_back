from moviepy.editor import *


class VideoConvert():
    @staticmethod
    def start(path):
        video = VideoFileClip('model/uploads/' + path)
        # video = video.cutout(0, 115)

        video = video.cutout(0, 90)
        video = video.cutout(150, 240)
        # video = video.cutout(135, 240)

        # Сохранение
        video.write_videofile("C:\\Users\\Администратор\\PycharmProjects\\waste_back\\model\\saves\\new_" + path, fps=5)


if __name__ == "__main__":
    VideoConvert()
