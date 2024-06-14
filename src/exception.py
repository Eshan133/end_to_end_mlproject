import sys  #manipulate various parts of Python runtime environment
from src.logger import logging

# Common throughout the code, used in all the try-catch block 

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info() # on which file, line no. the exception has occured (exc_tb)

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


'''
When `CustomException` class is called, following things will happen:
1. Inheriting the parent class 'Exception'
2. `error_message` and `error_detail` are passed to `error_message_detail`
3. `error_message_detail` will give a "custom exception-message" that we defined in above function
4. We will inherit another function `__self__`, which returns the error_message
'''
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys): #overiding the init method
        super().__init__(error_message)  
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self) -> str: # prints when we execute the CustomException class
        return self.error_message



# Creates the log with the cmd "python src/exception.py"
'''
if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero error") 
        raise CustomException(e, sys)
'''
