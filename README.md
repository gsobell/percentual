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

To install in the current working directory on any *nix system:
```sh
curl -LO  https://raw.githubusercontent.com/gsobell/percentual/home/percentual.py
mkdir ~/.local/share/percentual && touch ~/.local/share/percentual/data
mv percentual.py percentual && chmod +x percentual
```

To install on Arch and derivative systems, use the [PKGBUILD](https://github.com/gsobell/percentual/blob/home/PKGBUILD):
```shell
curl -O https://raw.githubusercontent.com/gsobell/percentual/home/PKGBUILD
makepkg -i
```

To add a new item to track:
```sh
percentual [name] [total sections] [optional = current section]
```

For example, if you were reviewing a textbook, and you read until chapter 14:
```sh
percentual Intro-to-Algo 35 14
```

### Controls
Add new item as argument to 
Use vim or arrow keys to navigate the list of items.
Use the left or right (`h` or `l`) to increment by 1. Press `q` anytime to exit.


## Features

### Current
- Add item and steps to completion
- Sane defaults

### Future
- Checklist functionality
- Term-resize resilience
- Vim-style command palette
- User defined color palette 
- Delete from within UI
- Roman, 1a, or SemVer numbering
- Multiple separate panels

***

Like [progress](https://github.com/Xfennec/progress), but for humans.
