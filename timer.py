import threading; import sys
from os import system

def timer(stawt, stahp, step, time_step):
	from time import sleep
	global run_timer

	stawt = int(stawt)
	stahp = int(stahp)

	if stahp < 1:
		stahp = 1
	elif stahp > 1000:
		stahp = 1000
	
	stahp = stahp * 100 + 1
	titerator = iter(range(stawt, stahp, step))

	def print_time():
		while run_timer is True:
			try:
				current_step = str(next(titerator))
				if int(current_step) < 99:
					final_time = '0' + current_step[:0] + '.' + current_step[0:] + 's'
					print('\r' + final_time, end='')
				elif int(current_step) < 999:
					final_time = current_step[:1] + '.' + current_step[1:] + 's'
					print('\r' + final_time, end='')
				elif int(current_step) < 9999:
					final_time = current_step[:2] + '.' + current_step[2:] + 's'
					print('\r' + final_time, end='')
				else:
					final_time = current_step[:3] + '.' + current_step[3:] + 's'
					print('\r' + final_time, end='')

				sleep(time_step)
			except:
				print(); break
	
		seconds = int((int(current_step) / 100) % 60)
		minutes = int((int(current_step) / 100) // 60)

		if minutes < 1:
			return ''
		else:
			final_time_human = str(minutes) + 'm ' + str(round(seconds)) + 's'
			print(final_time_human + '\n')

	print_time()

def _init_timer():
	global run_timer; run_timer = True

	print('Enter max number of seconds to count: ', end='')
	count_to = float(input()); print()

	timer_thread = threading.Thread(target=timer, args=(0, count_to, 1, 0.01))
	timer_thread.start()

	print('\rPress enter to stop the timer:')
	usr_input = input(); run_timer = False

system('clear')
_init_timer()
print('\nGoodbye!')
