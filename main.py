import os
import shutil

def createFolder(path,fileExtension):
    folderPath = os.path.join(path,fileExtension) # Get the folder path.
    os.makedirs(folderPath,exist_ok=True) # Create a folder for the file type.

def moveFile(filePath, destinationFolderPath):
    shutil.move(filePath, destinationFolderPath) # Move the file to the folder.

def sortFiles(folderPath):
    if not os.path.isdir(folderPath): # Check whether the path exists or not.
        return "The folder does not exist."
    
    for item in os.listdir(folderPath): # A loop to check every file in the folder.
        itemPath = os.path.join(folderPath,item)

        if os.path.isfile(itemPath): # Check whether the item is a file or not.
            fileExtension = item.split(".")[-1].lower() # Get the file extension and make it all lower case for uniformity purpose.
            newFolderPath = os.path.join(folderPath,fileExtension) # Get the new folder path.
            if not os.path.exists(newFolderPath): # Check whether the folder for the file type exists or not.
                createFolder(newFolderPath,fileExtension)
            moveFile(itemPath,newFolderPath) # If folder exists, move the file into the folder.

if __name__ == "__main__":
    folderPath = input("Enter the folder path:")
    sortFiles(folderPath)