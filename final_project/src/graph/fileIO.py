import os


def writeToFile(string, filename):
    with open(filename, "w") as myfile:
        myfile.write(string)

def createDirectory(filename):
    os.makedirs(format(os.path.dirname(filename)), exist_ok=True)
