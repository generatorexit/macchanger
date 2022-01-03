# MACCHANGER

## Install

```
git clone https://github.com/generatorexit/macchanger
cd macchanger
```

### Usage:

```
macchanger [option]

optional arguments:
  -h, --help         show this help message and exit
  -m , --mac         MAC Address to change [Manual Mode]
  -s, --show         Show available interface and exit
  -R, --Random       Automaticaly assign Random MAC
  -r, --reset        Reset to Original MAC

Required Arguments:
  -i , --interface   Interface you want to change MAC

Example: python3 macchanger.py -i [interface] -m [XX:XX:XX:XX:XX:XX]

```

```
[Manual] python3 macchanger.py -i [interface] -m XX:XX:XX:XX:XX:XX
```

```
[Auto] python3 macchanger.py -i [interface] -R
```
