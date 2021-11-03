from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class Googdrive():
    def __init__(self, obj):
        self.obj = obj
        gauth = GoogleAuth()           
        drive = GoogleDrive(gauth)

    def upload(self, obj):
        upload_file_list = ['1.jpg', '2.jpg']
        #for upload_file in upload_file_list:
        gfile = drive.CreateFile({'parents': [{'id': '1pzschX3uMbxU0lB5WZ6IlEEeAUE8MZ-t'}]})
        # Read file and set it as the content of this instance.
        gfile.SetContentFile(upload_file)
        gfile.Upload() # Upload the file.


    def listfiles():
        file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1cIMiqUDUNldxO6Nl-KVuS9SV-cWi9WLi')}).GetList()
        for file in file_list:
                print('title: %s, id: %s' % (file['title'], file['id']))

    def download():
        for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
        print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
        file.GetContentFile(file['title'])
