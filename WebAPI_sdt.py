import dropbox

class Db:
    def __init__(self, token):
        self.tok = token
    def uploadFile(self, file_from, file_to):
        f = open(file_from, 'rb')
        f = f.read()
        dbx = dropbox.Dropbox(self.tok)
        if file_from != '' and file_to != '':
            dbx.files_upload(f, file_to)
            print("File has been uploaded")
            
    def deleteFile(self, path):
        dbx = dropbox.Dropbox(self.tok)
        dbx.files_delete_v2(path)
        print("File has been deleted")

    def getMetaData(self, path):
        dbx = dropbox.Dropbox(self.tok)
        res = dbx.files_get_metadata(path)
        print(res)

if __name__ == '__main__':
    t = input("Token:")
    user = Db(t)
    folder = input("Folder:")
    file = input("File:")
    folder = '/' + folder + '/' + file
    user.uploadFile(file, folder)
    user.getMetaData(folder)
    user.deleteFile(folder)
