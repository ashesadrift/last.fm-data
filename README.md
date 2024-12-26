# last.fm-data
Get data from lastfmstats.com and format as a .csv with separated columns.

# Retrieving data
[This website](https://www.lastfmstats.com) can take any last.fm username and retrieve all scrobble history. I downloaded a .csv file of every scrobble in the form of Artist;”Album”;”Track”;”Date”. The date is a 13-digit number, given as a UNIX timestamp.

# Converting .csv to .txt
Solely as a result of the way I wrote the code, I had to open my lastfm-crystalz63.csv as a .txt file. This was because I realized I had tracks like “"30/90 (from "tick, tick... BOOM!" Soundtrack from the Netflix Film)” that had commas in them… and just because I’m a little lazy and am not sure how to be fixing up the CSV file by combining some columns that got separated, this way is easier. So when you open the .csv file you get from Last.fm Stats, save the file as a .txt.

# Python code
Download the Python file provided, open it, and scroll to the bottom (to main()). Insert the name of your file with the last.fm data (for instance, 'lastfm-crystalz63.txt') and create a name for the .csv file the program will create.
