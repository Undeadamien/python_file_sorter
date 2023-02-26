from os import listdir, replace
path_to_check =      ["C:\\Users\\Damien\\Downloads", 
                      "C:\\Users\\Damien\\Desktop"]

path_music =         "C:\\Users\\Damien\\Music"
path_image =         "C:\\Users\\Damien\\Desktop\\DRAWING_\\Photo_ref"
path_video =         "C:\\Users\\Damien\\Downloads\\Film"
path_video_process = "C:\\Users\\Damien\\Desktop\\DRAWING_\\Documentation"

for path in path_to_check:

    for file_ in listdir(path):

        try:
            #music file
            if file_.lower().endswith((".mp3",".flac")):
                replace(f"{path}\\{file_}",
                        f"{path_music}\\{file_}")
                
            #video file
            elif file_.lower().endswith((".mp4",".mkv")):
                #art process video 
                if any([True for x in ["art", "paint", "draw"] 
                        if x in file_.lower()]):
                    replace(f"{path}\\{file_}",
                            f"{path_video_process}\\{file_}")
                #other video file
                else:
                    replace(f"{path}\\{file_}",
                            f"{path_video}\\{file_}")

            #image file
            elif file_.lower().endswith((".jpg",".gif")):
                replace(f"{path}\\{file_}",
                        f"{path_image}\\{file_}")

        #if the file is open, ignore the file
        except PermissionError:
            continue
