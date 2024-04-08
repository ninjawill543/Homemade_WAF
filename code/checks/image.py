from flask import abort, redirect
import csv


def image_check(file, method):
    if (method == "POST"):
        if (file.filename == ""):
            abort(400, 'Please chose file to upload')
        print(file.filename, file.mimetype)




    
    