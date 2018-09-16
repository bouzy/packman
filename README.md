<div align="center">
  <img src="packman-logo.png"><br><br>
</div>

**PACKMAN** removes and installs a list of packages in batch.

## Supported OS
- Ubuntu

## Requirements
- Python 3.6

## Getting Started
Run the python file `packman.py` followed by an `option`. The following command uses the option `h`.
```bash
$ sudo ./packman.py h
```
Output
```
PACKMAN 1.1

USAGE: sudo ./packman.py [option]

OPTIONS:
  h - help
  rm - removes the selected packages
  in - installs the selected packages
  lrm - lists the selected packages to be removed
  lin - lists the selected packages to be installed
```
The lists of packages to be removed and installed are located in the variables `app_remove_list` and `app_add_list`.
