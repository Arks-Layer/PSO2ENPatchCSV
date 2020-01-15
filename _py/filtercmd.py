#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from sys import stdin, exit

def ci_switchs(cmd):  # decode /ci[1-9] {[1-5]} {t[1-5]} {nw} {s[0-99]}
    count = 0
    cmdl = cmd.split(" ", 5)
    lcmd = len(cmdl)
    if lcmd == count + 1:
        return count
    if not (cmdl[count + 1]):
        return count
    if cmdl[count + 1].isdigit():
        count += 1
    if lcmd == count + 1:
        return count
    if cmdl[count + 1] == "t":
        count += 1
    if lcmd == count + 1:
        return count
    if cmdl[count + 1] == "nw":
        count += 1
    if lcmd == count + 1:
        return count
    if cmdl[count + 1] == "s":
        count += 1
    return count


PSO2_Commands = [
    # Text Bubble Emotes
    ("toge", 0),
    ("moya", 0),
    ("mn", 0),  # (mn#)
    # Switch Main Palette (mpal#)
    ("mainpalette", 0),
    ("mpal", 0),
    ("subpalette", 0),
    ("spal", 0),
    # Switch Consume %1
    ("costume", 1),
    ("cs", 1),
    # Switch Camos %1
    ("camouflage", 1),
    ("cmf", 1),
    # Lobby action %1
    ("la", 1),
    ("mla", 1),
    ("fla", 1),
    ("cla", 1),
    # Symbol Art (symbol#)
    ("symbol", 0),
    # Voice Clip (vo#)
    ("vo", 0),
    # All chat
    ("a", 0),
    # Party chat
    ("p", 0),
    # Team Chat
    ("t", 0),
    # Timer
    ("start", 0),
    # Rideroid effect
    ("rt_eff", 0),
    # Rideroid timer
    ("rt_time", 0),
    # emotion?
    ("face", 0),
    # breaking 4th Wall
    ("ce", 0),
    # EOL
]


def need_switchs(msg):  # return the max number of swtichs for the command
    for s, n in PSO2_Commands:
        if msg.startswith(s):
            return n
    if msg.startswith("ci"):
        return ci_switchs(msg)  # Cut-ins need special handling
    return -1  # Unknown


def split_cmd_msg(message):
    cmd = ""
    msg = message
    if not message.strip() or message.strip() == "null":
        return (cmd, "")
    cmd, split, msg = message.rpartition("/")  # Let process that last command
    if split:
        args = need_switchs(msg)  # how many switchs does the last command need?
        if args == -1:  # not a vaild command, let look again
            cmdr, msgr = split_cmd_msg(cmd)
            return (cmdr, msgr + split + msg)
        else:  # so it is a vaild command, let add back togther
            msg += u" "
            msgl = msg.split(u" ", args + 1)   # let break apart msg strings into a list
            msg = msgl[-1]  # the string at the end of the list is the text
            cmdl = []  # Start a new list, with cmd
            cmdl.extend(msgl[0:args + 1])  # Add the command and all the switchs
            cmd = split + u" ".join(cmdl)  # join the list into a string
            if cmd and msg.rstrip():
                cmd += u" "
    return (cmd, msg.rstrip())

for line in stdin:
    output = ""
    cmd = ""
    cmd, output = split_cmd_msg(line)
    try:
        print(output, end="\n")
    except BrokenPipeError as e:
        exit(os.EX_IOERR);
