import configparser
import requests

class TextToVideo:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.example.com/text-to-video"

    def generate_video(self, text, duration=30):
        payload = {
            'text': text,
            'duration': duration,
            'api_key': self.api_key
        }
        response = requests.post(self.api_url, json=payload)

        if response.status_code == 200:
            return response.json()['video_url']
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['API']['key']

    t2v = TextToVideo(api_key)
    video_url = t2v.generate_video("Your text to convert into video", duration=30)
    print(f'Generated video URL: {video_url}')