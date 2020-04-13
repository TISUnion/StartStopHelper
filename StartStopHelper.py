# -*- coding: utf-8 -*-
import time


def wait(server, command, time_wait):
	while time_wait > 0:
		server.say('§cServer will {} in {}s§r'.format(command, time_wait))
		time.sleep(1)
		time_wait -= 1


def on_info(server, info):
	if info.is_user and server.get_permission_level(info) >= 3:  # admin
		args = info.content.split(' ')
		if len(args) not in [1, 2]:
			return
		if len(args) == 2 and not args[1].isdigit():
			return
		command = args[0]
		time_wait = int(args[1]) if len(args) == 2 else 10
		if command == '!!start':
			server.start()
		elif command == '!!stop':
			wait(server, 'stop', time_wait)
			server.stop()
		elif command == '!!stop_exit':
			wait(server, 'stop', time_wait)
			server.stop_exit()
		elif command == '!!restart':
			wait(server, 'restart', time_wait)
			server.restart()
