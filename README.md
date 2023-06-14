# percentual
a nCurses progress tracker

<h3 align="center"><img src="https://github.com/gsobell/percentual/blob/home/v001.png" width=75% height=75%></h3>

## About
#### `percentual` is:
* a progress tracker

#### `percentual` is not:
- a TODO list (see [vit](https://github.com/vit-project/vit))
- a habit tracker (see [dijo](https://github.com/nerdypepper/dijo))

## Usage

### Installation

```sh
curl -LO  https://raw.githubusercontent.com/gsobell/percentual/home/percentual.py
chmod +x percentual.py
```

To add a new item to track:
```sh
percentual.py [name] [sections] [optional =  current]
```

For example, if you were reviewing chapters of a textbook for a test, and you studied until chapter 12:
```sh
percentual.py Intro-to-Algo 35 12
```

### Controls
Use vim or arrow keys to navigate the list of items.
Use the left or right (`h` or `l`) to increment by 1. Press `q` anytime to exit.


## Features

### Current
- Add item and steps to completion
- Sane defaults

### Future
- Checklist functionality
- Vim-style command palette
- Extended color palette 
- Delete from within UI
- Roman, 1a, or Semantic Version numbering
- Multiple separate panels
