import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def uploadFile(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.accessToken)
        for root,dirs,files in os.walk(fileFrom): 
            for fileName in files: 
                localPath=os.path.join(root,fileName)
                relativePath=os.path.relpath(localPath,fileFrom)
                dropboxPath=os.path.join(fileTo,relativePath)
                with open(localPath,'rb') as f:
                    dbx.files_upload(f.read(),dropboxPath,mode=WriteMode('overwrite'))
def main():
    accessToken='sl.AwUMCaTQBxyhaPhNK8voxxJO1Fn6qpyyfD2gbK0WYD9pqTl4PXJaU_1gcRoOK-HU9Gfxy95mOMc1UAWIvx5QwZyXmHdrEedRzJkG2Q83_xj7EEH1EBRNTzHEr83Kx8j2nboQox8'
    transferData=TransferData(accessToken)
    fileFrom=input("Enter the Source File Path: ")
    fileTo=input("Enter the Destination File Path: ")
    transferData.uploadFile(fileFrom,fileTo)
    print("File has been Moved.")
main()