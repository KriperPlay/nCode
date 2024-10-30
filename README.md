# nCode

![](https://github.com/user-attachments/assets/e9f957cb-ba5b-43cf-a5b0-3403b15db7dc)

# About
nCode - simple qrcode by me

# How it work
every line - symbol coded into binary code as pixels

## Example

* ![output](https://github.com/user-attachments/assets/d6996353-a9a4-457e-8fec-3766a7f56be5)

# Need to install
* python3 and pip
* PIL

# How to use
## Download nCode
```bash
git clone https://github.com/KriperPlay/nCode/
```
## Run
* ```python3 main.py [mode] [text/.png]```
## Modes
* create
* * ```python3 main.py create [text]```
* read
* * ```python3 main.py read [.png]```
## Config
* in config u may edit colors for 0/1
* all colors must be HEX, without '#'
* ```json
  {
    "000000": "0",
    "008000": "1",
    "0": "000000",
    "1": "008000"
  }
* here 0 - black, 1 - green

# END
thx for downloand and using nCode <3

    
