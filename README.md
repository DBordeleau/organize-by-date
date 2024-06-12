# organize-by-date
Simple python script that will organize all the files in a specified directory (and subdirectories) by creation date.

You must specify the full system path of the directory you want to sort as a command line argument when you run the script.

Example: python organize_by_date.py C:\Users\User\Photos\2024Vacation

In the future I would add:
* option to default sort the directory you run the script from
* let users specify different criteria to sort by (filetype, prefix in filename, modification date, etc)
* sort by multiple criteria at once (sort all files by date and into subdirectories by type without having to run the script multiple times)
* better error handling for invalid arguments and empty directories/subdirectories
