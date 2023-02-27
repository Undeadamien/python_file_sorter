from os import listdir, replace
path_to_check = ["C:\\Users\\Damien\\Downloads",
                 "C:\\Users\\Damien\\Desktop"]

path_music = "C:\\Users\\Damien\\Music"
path_image = "C:\\Users\\Damien\\Desktop\\DRAWING_\\Photo_ref"
path_video = "C:\\Users\\Damien\\Downloads\\Film"
path_video_process = "C:\\Users\\Damien\\Desktop\\DRAWING_\\Documentation"
filters = ["art", "paint", "draw"]

for path in path_to_check:
    for file_ in listdir(path):

        try:

            if file_.lower().endswith((".mp3", ".flac")):
                replace(f"{path}\\{file_}",
                        f"{path_music}\\{file_}")

            elif file_.lower().endswith((".jpg", ".gif")):
                replace(f"{path}\\{file_}",
                        f"{path_image}\\{file_}")

            elif file_.lower().endswith((".mp4", ".mkv")):

                if any([True for x in filters[0] if x in file_.lower()]):
                    replace(f"{path}\\{file_}",
                            f"{path_video_process}\\{file_}")
                else:
                    replace(f"{path}\\{file_}",
                            f"{path_video}\\{file_}")

        except PermissionError:
            continue
