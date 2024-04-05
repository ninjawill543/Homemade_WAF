from flask import abort, redirect
import csv

def sql_check(input1, input2, path, method):
    if (method == "POST"):
        if (input1 == "" and input2 != ""):
            abort(400, 'Username cannot be empty')
        elif (input2 == "" and input1 != ""):
            abort(400, 'Password cannot be empty')
        elif (input1 == "" and input2 == ""):
            abort(400, 'Cannot send empty request')
        else:
            print(input1.lower(), input2.lower())
            chars = [chr(x) for x in range(33, 127) if not chr(x).isalnum()]
            # print (len(chars))
            import json
 
            f = open('checks/sql.json')

            data = json.load(f)
            

            for i in data['rules']:
                print(i)
            
            f.close()
    
        
    
    # with open("checks/sql.csv", "r") as f:
    #     print(list(csv.reader(f)))
    
    
