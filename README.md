# haveibeenpawned

This repo provides a safe way to check if your password has been breached before.
it is powered by https://haveibeenpwned.com/

It is not recommended to provide the full hash of your password to check if it has been leaked. Probably you might do it now.
Hence this script uses  [search by range](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange) and then compares the match locally in memory.

## Requirements
it requires python3 to be installed.

## Usage
clone the repo and run the following command:

`python3 pawned.py <your-password>`

## Example
```
python3 .\pawned.py Password1
checking.......
password has been cracked : 139705 times. So CHANGE IT !! 
```
## Additional info
it also outputs the following
```
target url : https://api.pwnedpasswords.com/range/70CCD
SHA-1 hash to be looked for: 9007338D6D81DD3B6271621B9CF9A97EA00
```
so that you can check it manually as well to double check.


