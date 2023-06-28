#!/usr/bin/env python3
from sys import argv, exit
from os import path, makedirs
import json
import curses
from curses import wrapper

DEFAULT_COLOR = 2
DATA = path.expanduser("~/.local/share/percentual/data.json")
# OUT = path.expanduser("~/.local/share/percentual/out") # debug
# CONFIG = "$HOME/.config/percentual/percentualrc"

"""percentual
name of tasks should right aling  with end of longest task name
for task over n, use ticker tape
command mode is contextual; will apply to visually selected line if possible
"""

"""
TODO:
gracefully handler term resize
delete from tui
vim style input box
json data store
"""

VERSION = "0.0.2"


def show_usage():
    print("usage: percentual [name] [sections] [optional =  current] ")
    print("Use  ←↓↑→  or  hjkl  to navigate. ")
    print("Options:")
    print(" -h,  --help     display this help message")
    print(" -l,             show licence")
    print(" -v,             show version")
    print("press 'q' anytime to quit")
    print(" -a,  --add      add new item")


def save(bars, path):
    """saves changes on exit, without fail"""
    with open(path, "w") as data:
        json.dump(bars, data)

#
# def add(name, end, current=0):
#     if not path.exists(DATA):
#         makedirs(DATA)
#     if int(current) <= int(end):
#         with open(DATA, 'a') as f:
#             f.write(f"{name} {end} {current}\n")
#     else:
#         flag_error()


def add(name, end, current=0):
    if not path.exists(DATA):
        makedirs(path.dirname(DATA), exist_ok=True)
        with open(DATA, 'w') as file:
            json.dump([], file)  # Initialize an empty JSON list
    # if int(current) <= int(end):
    with open(DATA, 'r+') as file:
        data = json.load(file)  # Load the existing JSON data
        # Append a new list to the JSON data
        data.append([name, int(end), int(current), DEFAULT_COLOR])
        file.seek(0)
        file.truncate()
        json.dump(data, file)


def load(path):
    """load from file, assumes correct input"""
    with open(path, "r") as extant:
        loaded = json.load(extant)
        return loaded


def flag_error():
    print("One or more arguments are invalid.")
    show_usage()
    exit()


# Check if flags present
i = 1
while i < len(argv):
    arg = argv[i]
    if arg == "-h" or arg == "--help":
        print("percentual")
        print("a nCurses progress tracker")
        show_usage()
        exit()
    if arg == "-a" or arg == "--add":
        print(len(argv))
        if (len(argv)) == 5:
            if (int(argv[3]) >= int(argv[4])):
                add(str(argv[2]), int(argv[3]), int(argv[4]))
        elif len(argv) == 4:
            add(str(argv[2]), int(argv[3]))
        else:
            flag_error()
        break
    elif arg == "-v":
        print(f"version {VERSION}")
        exit()
    elif arg == "-l":
        print("Under GPL3 licence.\n \
Full license distribuited \
with copy of software")
        exit()
    i += 1


def curses_setup(stdscr):
    """Init curses and color pairs, program title"""
    stdscr.clear()   # Clear the screen
    curses.noecho()  # Turn off echoing of keys
    curses.cbreak()  # Turn off normal tty line buffering
    stdscr.keypad(True)   # Enable keypad mode
    curses.mousemask(True)
    curses.curs_set(0)    # Hide cursor
    curses.start_color()  # Enable colors if supported
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # text
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_BLUE)   # status bar
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_WHITE)

    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.addstr(0, int((curses.COLS - len(f"percentual v{VERSION}")) / 2),
                  f"percentual v{VERSION}", curses.color_pair(1))

    stdscr.refresh()


def color_legend(stdscr):
    stdscr.move(curses.LINES - 1, 0)
    stdscr.addstr("Press key for:", curses.color_pair(1) | curses.A_UNDERLINE)
    stdscr.addstr(" 1: Blue ", curses.color_pair(2) | curses.A_REVERSE)
    stdscr.addstr("2: Cyan ", curses.color_pair(3) | curses.A_REVERSE)
    stdscr.addstr("3: Red ", curses.color_pair(4) | curses.A_REVERSE)
    stdscr.addstr("4: Green ", curses.color_pair(5) | curses.A_REVERSE)
    stdscr.addstr("5: Magenta ", curses.color_pair(6) | curses.A_REVERSE)
    stdscr.addstr("6: Yellow ", curses.color_pair(7) | curses.A_REVERSE)
    stdscr.addstr("7: White", curses.color_pair(8) | curses.A_REVERSE)
    stdscr.addstr(" 'q' to exit", curses.color_pair(1))


def draw_bar(stdscr, y, x, bar, padding):
    """draws a bar in line y"""
    part = bar[2] / bar[1]
    bar_size = int((curses.COLS - padding) * part)
    percent = f" {round(part * 100, 1)}%"
    count = f" ({bar[2]}/{bar[1]})"
    stdscr.addstr(y, x, bar[0], curses.color_pair(1))
    stdscr.addstr(y, padding, " " * bar_size, curses.color_pair(bar[3]))
    if bar_size + padding + len(percent + count) <= curses.COLS:
        stdscr.addstr(y, padding + bar_size,
                      percent + count, curses.color_pair(1))
    else:
        stdscr.addstr(y, padding + bar_size - len(percent) - len(count),
                      percent + count, curses.color_pair(bar[3]))


def draw_bars(stdscr, bars):
    padding = max([len(b[0]) for b in bars]) + 1
    y, x = 1, 0
    for bar in bars:
        draw_bar(stdscr, y, x, bar, padding)
        y += 2
    stdscr.refresh()
    return padding


def get_move(c, bars, counter, padding, stdscr):
    if c == curses.KEY_LEFT or c == ord('h'):
        if (bars[counter][2] != 0):
            bars[counter][2] -= 1
            stdscr.move(counter*2 + 1, 0)
            stdscr.clrtoeol()
            draw_bar(stdscr, counter*2 + 1, 0, bars[counter], padding)
            save(bars, DATA)
    elif c == curses.KEY_RIGHT or c == ord('l'):
        if (bars[counter][1] > bars[counter][2]):
            bars[counter][2] += 1
            stdscr.move(counter*2 + 1, 0)
            stdscr.clrtoeol()
            draw_bar(stdscr, counter*2 + 1, 0, bars[counter], padding)
            save(bars, DATA)
    # elif c == ord('a') or c == ord('A'):
        # add(name, end, current)
    elif ord('0') <= c <= ord('9') - 2:      # invisible bar
        bars[counter][3] = c - ord('0') + 1  # can't be pair 1'
        draw_bar(stdscr, counter*2 + 1, 0, bars[counter], padding)
        save(bars, DATA)
    elif c == curses.KEY_UP or c == ord('k'):
        counter -= 1
        if counter < 0:
            counter = len(bars) - 1
    elif c == curses.KEY_DOWN or c == ord('j'):
        counter += 1
        if counter >= len(bars):
            counter = 0
    elif c == ord('q'):
        exit()
    else:
        # stdscr.addstr(0, 0, "Not a valid input key")
        pass
    return counter


def percentual(stdscr):
    curses_setup(stdscr)
    if path.exists(DATA):
        bars = load(DATA)
        padding = draw_bars(stdscr, bars)
        counter = 0
    else:
        stdscr.addstr(1, 0, "You have no items loaded.")
        stdscr.addstr(2, 0, "Run 'percentual --help' for usage")
    color_legend(stdscr)
    while True:
        c = stdscr.getch()
        old_counter = counter
        counter = get_move(c, bars, counter, padding, stdscr)
        stdscr.chgat(old_counter * 2 + 1, 0,
                     len(bars[old_counter][0]), curses.A_NORMAL)
        stdscr.chgat(counter * 2 + 1, 0,
                     len(bars[counter][0]), curses.A_BLINK | curses.A_STANDOUT)
        stdscr.refresh()


if __name__ == "__main__":
    try:
        wrapper(percentual)
    except KeyboardInterrupt:
        print("Bye.")
    # except ValueError:
    #     print("No items added yet.")
    #     show_usage()
    finally:
        pass
