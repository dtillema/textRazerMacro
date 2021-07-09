from FileHandler import FileHandler
import sys

if len(sys.argv) > 1:
    myFileHandler = FileHandler(sys.argv[1], sys.argv[2])
else:
    myFileHandler = FileHandler()

myFileHandler.file_header()
myFileHandler.input_file()
myFileHandler.file_footer()