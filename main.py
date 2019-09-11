# pip install pyFirmata
import matlab.engine
from pyfirmata import Arduino, util
import time

print("set up the board and pins")
board = Arduino('/dev/tty.usbmodem14101')
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
digital_8_input = board.get_pin('d:8:i')

print("define handy functions")
def turn_on():
	print("Power on")
	board.digital[13].write(1)

def turn_off():
	print("Power off")
	board.digital[13].write(0)



def digital_8_is_high():
	return(digital_8_input.read())

turn_off()

def start_matlab_in_working_dir(dirname):
    eng = matlab.engine.start_matlab()
    eng.cd(r'%s' % dirname, nargout=0)
    return(eng)

print("start the matlab service")
matlab_working_directory =   "~/Documents/GitHub/bc/mphand/"
eng = start_matlab_in_working_dir(matlab_working_directory)
#wait until button press to invoke matlab
print("Awaiting High on digital 8")
while (digital_8_is_high()==False):
 	pass
done = eng.create_gui_button(5)
print("DONE")
turn_on()
time.sleep(8)
turn_off()
