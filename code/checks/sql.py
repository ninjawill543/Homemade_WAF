from flask import abort, redirect
import csv
import json

log_value = 3
drop_value = 4

def score(data, in1, in2):
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0,13):
        for j in range (len((data["rules"][i]["rule"]))):
            if (data["rules"][i]["rule"][j]) in in1:
                counter[i] = (data["rules"][i]["points"])
    print(counter)
    print(sum(counter))

def sql_check(input1, input2, path, method):
    if (method == "POST"):
        if (input1 == "" and input2 != ""):
            abort(400, 'Username cannot be empty')
        elif (input2 == "" and input1 != ""):
            abort(400, 'Password cannot be empty')
        elif (input1 == "" and input2 == ""):
            abort(400, 'Cannot send empty request')
        else:
            chars = [chr(x) for x in range(33, 127) if not chr(x).isalnum()]
            # print (len(chars))
            
            file_path = 'checks/sql.json' 
            with open(file_path, 'r') as file:
                data = file.read()
            parsed_data = json.loads(data)

            score(parsed_data, input1.lower(), input2.lower())


    
        
    
    # with open("checks/sql.csv", "r") as f:
    #     print(list(csv.reader(f)))
    
    
