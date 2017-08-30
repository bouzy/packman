<div align="center">
  <img src="logo.png"><br><br>
</div>

**PACKMAN** removes and installs selected packages in batch.

## System Requirements
- Ubuntu 16.04 LTS +
- Python 3.5

## Getting Started
Run the python file `packman.py` followed by an option.
```bash
$ sudo python packman.py h
```
```
PACKMAN 1.0

USAGE: sudo python packman.py [option]

OPTIONS:
  h - help menu
  rm - removes the selected packages
  in - installs the selected packages
  lrm - lists the selected packages to be removed
  lin - lists the selected packages to be installed
```
The lists of packages to be removed and installed are located in the variables `app_remove_list` and `app_add_list`.
```python
app_remove_list = (['libreoffice-core',
    'libreoffice-common',
    'account-plugin',
    'totem',
    'totem-common',
    'unity-scopes-runner',
    'unity-scope-video-remote',
    'unity-lens-files',
    'unity-lens-photos',
    'unity-lens-music',
    'unity-lens-video'])

app_add_list = (['gcc',
    'g++',
    'make',
    'vim',
    'git',
    'python-pip',
    'htop',
    'p7zip-full',
    'wget', 'curl',
    'traceroute',
    'nmap',
    'vlc'])
```
