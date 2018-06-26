<div align="center">
  <img src="logo.png"><br><br>
</div>

**PACKMAN** removes and installs selected packages in batch.

## Requirements
- Ubuntu or Debian
- Python 3.6

## Getting Started
Run the python file `packman.py` followed by an `option`. The following command uses the option `h`.
```bash
$ sudo python3 packman.py h
```
Output
```
PACKMAN 1.0.1

USAGE: sudo python packman.py [option]

OPTIONS:
  h - help
  rm - removes the selected packages
  in - installs the selected packages
  lrm - lists the selected packages to be removed
  lin - lists the selected packages to be installed
```
The lists of packages to be removed and installed are located in the variables `app_remove_list` and `app_add_list`.
```python
app_remove_list = ([''])

app_add_list = ([''])
```
