from flask import abort

def sql_check(input1, input2, path):
    if (input1 == "" and input2 != ""):
        abort(400, 'Username cannot be empty')
    elif (input2 == "" and input1 != ""):
        abort(400, 'Password cannot be empty')
