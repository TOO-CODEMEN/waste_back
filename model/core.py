# здесь будет моделька
import os
from roboflow import Roboflow
from settings import MlSettings
from handler.video_convert import VideoConvert
import time


class RoboflowRequest():
    @staticmethod
    def get_info(image: str):
        api = MlSettings().api_key.get_secret_value()
        rf = Roboflow(api_key=api)
        project = rf.workspace().project("waste-detect-rb23i")
        model = project.version(3).model
        if image.endswith('.mp4'):
            VideoConvert.start(image)
            time.sleep(2)
            job_id, signed_url, expire_time = model.predict_video(
                os.path.abspath('model/saves/new_' + image),
                #f'model/saves/new_{image}',
                fps=2,
                prediction_type="batch-video",
            )

            info = model.poll_until_video_results(job_id)
            print(info)
        else:
            print(os.path.abspath('model/' + image))
            print(f'model/{image}')

            model.predict(f'model/uploads/{image}', confidence=40, overlap=30).save(f'model/saves/new_{image}')
            info = model.predict(f'model/uploads/{image}', confidence=40, overlap=30).json()
            print(info)
            os.remove(f'model/uploads/{image}')
        return info


if __name__ == '__main__':
    RoboflowRequest()
    # RoboflowRequest().get_info("new_3334137.mp4")
