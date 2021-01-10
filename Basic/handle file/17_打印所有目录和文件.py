import os


allfiles = []


def getAllFiles(path, level):
    childFiles = os.listdir(path)
    for file in childFiles:

        filePath = os.path.join(path, file)
        if os.path.isdir(filePath):
            getAllFiles(filePath, level+1)
            allfiles.append("\t"*level+filePath)


getAllFiles("movie", 0)

for f in reversed(allfiles):
    print(f)
