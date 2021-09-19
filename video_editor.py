from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

ready = 0


def editing():
    print("i'm fucking working")

    clips = []
    clips_dir = r"C:\Users\LENOVO\PycharmProjects\tiktok-scraper\clips"
    x = 0

    for clip in os.listdir(clips_dir):
        clips.append(VideoFileClip(rf"C:\Users\LENOVO\PycharmProjects\tiktok-scraper\clips\{clip}").resize((864, 1080)))
        x = x + 1

    transition = VideoFileClip("transition.mp4")
    try:
        final_clip = concatenate_videoclips(clips, transition=transition, method='compose')

        if os.path.exists("final_clip.mp4"):
            os.remove("final_clip.mp4")

        final_clip.write_videofile("final_clip.mp4")
        if os.path.exists("final_clip.mp4"):
            try:
                for clip in os.listdir(clips_dir):
                    os.remove(rf"C:\Users\LENOVO\PycharmProjects\tiktok-scraper\clips\{clip}")
            except Exception as e:
                print(e)
                pass

    except Exception as e:
        for clip in os.listdir(clips_dir):
            os.remove(rf"C:\Users\LENOVO\PycharmProjects\tiktok-scraper\clips\{clip}")
        print(e)
        input("editing didn't work")
