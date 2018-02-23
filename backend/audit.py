#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re


class AuditLogHander(object):
    '''分析audit log日志'''

    def __init__(self, log_file):
        self.log_file_obj = self._get_file(log_file)

    def _get_file(self, log_file):
        return open(log_file)

    def parse(self):
        cmd_list = []
        cmd_str = ''
        catch_write5_flag = False  # for tab complication
        catch_vim_flag = False
        for line in self.log_file_obj:
            line = line.split()
            try:
                time_clock, io_call, char = line[0:3]
                if io_call.startswith('read(4'):
                    if char == '"\\10",':  # backspace
                        char = "backspace"
                    elif char == '"\\33[A",':
                        if not catch_vim_flag:
                            char = '[↑ 1]'
                        else:
                            catch_write5_flag = True
                    elif char == '"\\33[B",':
                        if not catch_vim_flag:
                            char = '[↓ 1]'
                        else:
                            catch_write5_flag = True
                    elif char == '"\\33[D",':
                        if not catch_vim_flag:
                            char = '[← 1]'
                        else:
                            catch_write5_flag = True
                    elif char == '"\\33[C",':
                        if not catch_vim_flag:
                            char = '[→ 1]'
                        else:
                            catch_write5_flag = True
                    elif char == '"\\33[2;2R",':
                        char = '[----enter vim mode-----]'
                        catch_vim_flag = True

                    elif char == '"\\t",':
                        print('tab')
                        catch_write5_flag = True
                        continue

                    cmd_str += char.strip('"",')
                    if char == '"\\r",':
                        if len(cmd_str):
                            cmd_str.strip(r'\r')
                            cmd_list.append([time_clock, cmd_str])
                        if cmd_str.__contains__(':q') or cmd_str.__contains__(':wq'):
                            catch_vim_flag = False
                        cmd_str = ''
                    if char == '"':
                        cmd_str += ' '

                if catch_write5_flag:
                    if io_call.startswith('write(5'):
                        if char == r'"\7",':
                            pass
                        else:
                            cmd_str += char.strip('"",')
                        catch_write5_flag = False
            except ValueError as e:
                print("\033[031;1mSession log record err,please contact your IT admin,\033[0m", e)
        return cmd_list


if __name__ == '__main__':
    parser = AuditLogHander('strace.log')
    parser.parse()
