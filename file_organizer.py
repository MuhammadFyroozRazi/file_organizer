
import os
import shutil

def file_migrate(dir_name,file,cur_dir):
    if os.path.exists(cur_dir+'/'+dir_name):
        #if path exist
        shutil.move(cur_dir+'/'+file,cur_dir+'/'+dir_name+'/'+file)
    else:
        os.makedirs(cur_dir+'/'+dir_name)
        shutil.move(cur_dir+'/'+file,cur_dir+'/'+dir_name+'/'+file)

def access_files(dir_path,video=0,image=0,doc=0,audio=0,compress=0):
    print(dir_path,video,image,doc,audio,compress)
    os.chdir(dir_path)
    files=os.listdir()
    cur_dir=os.getcwd()
    for file in files:
        if doc==1 and f".{file.split('.')[-1].lower()}" in text_extensions:
            file_migrate(doc_dir,file,cur_dir)
        elif image==1 and f".{file.split('.')[-1].lower()}" in image_extensions:
            file_migrate(image_dir,file,cur_dir)
        elif audio==1 and f".{file.split('.')[-1].lower()}" in audio_extensions:
            file_migrate(audio_dir,file,cur_dir)
        elif video==1 and f".{file.split('.')[-1].lower()}" in video_extension:
            file_migrate(video_dir,file,cur_dir)
        elif compress==1 and f".{file.split('.')[-1].lower()}" in compressed_extension:
            file_migrate(compre_dir,file,cur_dir)
        # elif f".{file.split('.')[-1].lower()}" in executable_file:
        #     file_migrate(exe_dir,file,cur_dir)


image_extensions=['.jpeg','.png','.jpg','.tiff','.svg','.ico','.jfif','.webp','.gif']
audio_extensions=['.mp3','.mav','.aac','.wma','.m4a','.wav']
video_extension=['.flv','.mp4','.mov','.avi','.wmv','.mkv','.webm']
compressed_extension=['.rar','.zip','.iso']
text_extensions=['.pdf','.docx','.doc','.html','.xls','.xlsx','.txt']
# executable_file=['.exe']

image_dir='Images'
video_dir='Videos'
audio_dir='Audio'
doc_dir='Document'
compre_dir='Compressed'
exe_dir='Software'

if __name__=='__main__':
    path=r'url'
    access_files(path)