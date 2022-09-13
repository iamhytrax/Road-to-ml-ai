x = 123
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))



    #output throws an exception


    """Traceback (most recent call last):
  File "f:\PYTHON\python project vs code\ basic\exceptions\ raising_exception.py", line 3, in <module>
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
Exception: x should not exceed 5. The value of x was: 123"""