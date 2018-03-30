import tweepy
import musahid.config as config
import tweepy.models

class TimeLineStreamListener(tweepy.StreamListener):
    def on_status(self, status: tweepy.models.Status):
        print(status.text)

    def on_event(self, status: tweepy.models.Status):
        if status.event in [
            'favorite',
            'unfavorite',
        ]:
            print(status.created_at, status.event, status.source['id'], status.target_object['id'])

        print(status.created_at, status.event, status.source['id'], status.target['id'])

    def on_error(self, status_code: int):
        if status_code == 420:
            return False

if __name__ == '__main__':
    timeline_listener = TimeLineStreamListener()
    timeline = tweepy.Stream(auth=config.AUTH, listener=timeline_listener)

    timeline.userstream(async=True, stall_warnings=True)