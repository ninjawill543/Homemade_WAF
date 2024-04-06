from flask import abort, redirect
import csv



def xss_check(input, path, method):
    if (method == "POST"):
        if (input == ""):
            abort(400, 'Input cannot be empty')



    
    
