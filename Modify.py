import os
import inspect
import sys
import new
def main():
    sandbox()

    def game_over():
        print("Unable to modify the code execution flow")
        print (LOSE_LOGO)
        os._exit(1)
        print('The code execution altered properly')
        

    def win():
        print (WIN_LOGO)
        
    game_over()
    win()

def sandbox():
	TRACE_INTO = ['game_over']
	def trace_lines(frame, event, arg):
		if event != 'line':
			return
		co = frame.f_code
		func_name = co.co_name
		line_no = frame.f_lineno
		frame.f_lineno = line_no + 3
		filename = co.co_filename
	
	def debugs1(frame, event, arg):
		if event != 'call':
			return
		co = frame.f_code
		func_name = co.co_name
		if func_name == 'game_over':
			if func_name in TRACE_INTO:
				return trace_lines
		return
	sys.settrace(debugs1)	
	pass


WIN_LOGO = """
  ####                 ####       ############           ####       ####
   ####               ####            ####             ########    ####
	####    ####    ####             ####            ####  ####  ####
 	 ########  ########              ####           ####    ########
 	  ####        ####           ############      ####       #####
     """

LOSE_LOGO = """
####			############	  ############       ############
####			####    ####	  #####				 ####
####			####    ####	  ############       #######
####			####    ####			 #####       ####
############    ############      ############       ############
    """

if __name__ == '__main__':
    main()
    
