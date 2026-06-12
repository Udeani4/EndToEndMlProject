## create custom exception

import sys ## browse more on this 

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename ## you can search for custom exception handl
    error_message='Error occured in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name
    )