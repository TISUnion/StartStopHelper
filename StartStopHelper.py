# -*- coding: utf-8 -*-

import time

def action(server, command, time_wait):
    for countdown in range(0, time_wait):
        server.say('§cServer will {} in {} second! Use !!abort to abort'.format(time_wait - countdown, command))
        for i in range(10):
            time.sleep(0.1)
            global abort
            if abort:
                server.say('§cAction aborted')
                return False
    else:
        return True


def on_user_info(server, info):
    if info.content.rstrip(' ') == '!!abort':
        global abort
        abort = True

    if info.content.startswith('!!') and info.is_user:
        args = info.content.split(' ')
        if len(args) not in [1, 2]:
            return

        command = args[0][2:]
        if command not in ['start', 'stop', 'stop_exit', 'restart', 'exit']:
            return

        if server.get_permission_level(info) >= 3:
            abort = False
            if len(args) == 2 and not args[1].isdigit():
                server.reply(info, '§c[time] argument need to be a number')
                return
            time_wait = int(args[1]) if len(args) == 2 else 0
            if command == 'start':
                server.start()
            elif command == 'stop':
                if action(server, 'stop', time_wait):
                    server.stop()
            elif command == 'stop_exit':
                if action(server, 'stop', time_wait):
                    server.stop_exit()
            elif command == 'restart':
                if action(server, 'restart', time_wait):
                    server.restart()
            elif command == 'exit':
                server.exit()
        else:
            server.reply(info, '§cPermission denied')
