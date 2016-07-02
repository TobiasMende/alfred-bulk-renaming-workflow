This workflow lets you rename multiple files at once using the realy realy great [Alfred App](https://www.alfredapp.com) on OS X.
For this purpose, it provides a file action. After choosing files you are guided through three phases:

# Step by Step

1. You are ask to enter or choose a regular expression which should match parts of the input file. File endings are not renamed so your regex must not match a file name with its extension but only the name itself. 
2. You are ask to enter or choose a rename pattern (also a regular expression). Here you have the following options:
    * `$0` matches the full input, i.e. if your file is named 'foo.jpg' `$0` gives you 'foo'.
    * `$1` to `$n` contain the regex matching groups, you have defined previously.
    * `{n}` contains a serial number which starts at 1.
    * `{d}` contains the current date in the format 'YYYY-MM-DD'.
3. After pressing enter again, Alfred shows you a list wich gives you a preview of how the renaming will look.
4. Pressing enter again will rename all files according to your expressions.
