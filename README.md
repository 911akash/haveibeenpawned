# haveibeenpawned

This repo provides a safe way to check if your password has been breached before.
it is powered by https://haveibeenpwned.com/

It is not recommended to provide the full hash of your password to check if it has been leaked, As you might facilitate it while checking for the same !.
To counter this, i used [search by range](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange) method and then match complete hash locally in memory.

## Requirements
it requires python3 to be installed.

## Usage
clone the repo and run the following command:

`python3 tools/pawned.py <your-password>`

## Example
```
python3 tools\pawned.py Password1
checking.......
password has been cracked : 139705 times. So CHANGE IT !! 
```
## Additional info
it also outputs the following
```
target url : https://api.pwnedpasswords.com/range/70CCD
SHA-1 hash to be looked for: 9007338D6D81DD3B6271621B9CF9A97EA00
```
so that you can check it manually as well, just to double check.

## Unit test
on root folder run 
```
pytest
```
