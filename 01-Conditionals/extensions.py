# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs
# that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

suffixes = {".gif": "image/gif",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".pdf": "application/pdf",
            ".txt": "text/plain",
            ".zip": "application/zip"
            }

file = str(input("File name: ")).lower().strip().strip(".")

bingo = str()
for suffix in suffixes:
    if suffix in file:
        bingo = suffixes.get(suffix)
        break

if bingo:
    print(bingo)
else:
    print("application/octet-stream")
