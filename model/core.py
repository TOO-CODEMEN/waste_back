# здесь будет моделька
import os
from roboflow import Roboflow
from settings import MlSettings
class RoboflowRequest():
    @staticmethod
    def get_info(image: str):
        api = MlSettings().api_key.get_secret_value()
        rf = Roboflow(api_key=api)
        project = rf.workspace().project("waste-detect-rb23i")
        model = project.version(3).model
        if image.endswith('.mp4'):
            job_id, signed_url, expire_time = model.predict_video(
                    f'model/{image}',
                    fps=2,
                    prediction_type="batch-video",
            )
            info = model.poll_until_video_results(job_id)
            print(info)
        else:
            model.predict(f'model/{image}', confidence=40, overlap=30).save(f'model/result_{image}')
            info = model.predict(f'model/{image}', confidence=40, overlap=30).json()
            print(info)
            os.remove(f'model/{image}')
        return info

if __name__ == '__main__':
    RoboflowRequest()