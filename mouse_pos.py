from os import system

system('clear')
print('')

def get_mouse_xy():
	import tkinter

	try:
		p = Tkinter.Tk()
	except:
		p = tkinter.Tk()

	mouse_position = p.winfo_pointerxy()
	return mouse_position

def disp_cur_pos():
	from os import get_terminal_size

	cursor_pos = get_mouse_xy()
	cur_x = cursor_pos[0]
	cur_y = cursor_pos[1]

	COLS = get_terminal_size().columns
	print('\033[Kx is {} and y is {}'.center(COLS).format(cur_x, cur_y), end='\r')
	
while True:
	disp_cur_pos()
	system('sleep 0.01')