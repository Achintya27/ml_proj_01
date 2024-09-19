import sys
import logging
'''Any Exception is getting control the sys will contain that information '''

# def error_message_detail(error, error_detail:sys):
def error_message_detail(*args):
    error, error_detail = args
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename # search for Python exception handling
    error_message = f"Error occured in python script name {filename} line number {exc_tb.tb_lineno} error message {str(error)}"
    return error_message
    
class CustomException(Exception):
    
    # def __init__(self, error, error_detail: sys) -> None:
    #     super().__init__(str(error))  # Ensure the error message is passed to the Exception base class
    #     self.error_message = error_message_detail(error, error_detail)
    
    def __init__(self, *args) -> None:
        super().__init__(str(args[0]))  # The first arg is the error message
        self.error_message = error_message_detail(*args)

    def __str__(self):
        return self.error_message
