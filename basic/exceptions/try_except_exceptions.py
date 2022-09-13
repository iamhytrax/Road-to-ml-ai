import sys
def linux_interaction():
    assert ('Linux' in sys.platform), "Function can only run on Linux systems."
    print("doing something")


try:
    linux_interaction()
except AssertionError as error:
    print(error)
    #print("The linux_interaction() function was not executed")
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as nerror:
        print(nerror)
finally: #finally is used to cleanup exceptions
    print("cleaning up irrespective of any exception")
    