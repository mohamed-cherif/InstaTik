from TikTokApi import TikTokApi
import random

"""
how to get the verifyFp value: browser > tiktok.com > lock icon beside the url > 
                                    cookies > www.tiktok.com > s_v_web_id > copy value
"""
verifyFp = input("enter the verify cookie:    ")
keyword = input("enter desired keyword:    ")
api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

count = 2000
videos = []
chosen_videos = []

title = "BEST MEMES COMPILATION"
description = "Enjoy ! and don't forget to follow." \
              "#fuuny #meme #lol #funnyvideo"
tiktoks = api.by_hashtag(keyword, count=count)

for tiktok in tiktoks:
    duration = tiktok['video']['duration']
    author = tiktok['author']['uniqueId']
    id = tiktok['id']
    desc = tiktok['desc']
    video_share_link = f"https://www.tiktok.com/@{author}/video/{id}"
    print(video_share_link)
    print(duration)
    print(author)
    print(desc)
    print(tiktok)
    if duration <= 15:
        if "india" not in desc:
            videos.append(video_share_link)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

for i in range(6):
    chosen = random.choice(videos)
    chosen_videos.append(chosen)

print(chosen_videos)
# python -m playwright install (try uninstall if not needed anymore)
