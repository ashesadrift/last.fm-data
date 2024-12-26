import datetime
import csv

def format_date(string):
    try:
        # remove the extra quotation marks
        string = string.strip('"')
        # left 10 chars + '.' + right 3 chars
        decimaled = f"{string[:10]}.{string[-3:]}"
        # convert to GMT days since 1/1/1970
        gmt = (((float(decimaled)/60) / 60) / 24)
        
        # stack overflow: adding days to a date
        og_date = datetime.datetime.strptime("01/01/70", "%m/%d/%y")
        # adding days, subtracting 5 hours to get EST
        end_date = og_date + datetime.timedelta(days=gmt) - datetime.timedelta(hours=5)
        
        return end_date
    except ValueError: # raised for 1st row of col titles
        return "Time played"

def open_data(filepath, newfile):
    try:
        # open file to read
        # not sure about the encoding part, got it from stack overflow
        file = open(filepath, 'r')
        
        # read file
        content = file.readlines()
        
        new_file = open(newfile, 'w', encoding='utf-8-sig', newline='') # create new file with requested name
        writer = csv.writer(new_file, delimiter=',')
        
        for row in content:
        # Artist;Album;Track;Date#{username}
            info = row.strip().split(';') # must turn into actual list with 4 elts

            # access UNIX date string
            date = format_date(info[3])
            
            track = info[2].replace('"', '')
            album = info[1].replace('"', '')
            artist = info[0].replace('"', '')
            
            # write input as a list
            # [date, track, album, artist]
            new_row = [date, track, album, artist]

            writer.writerow(new_row)
            
        new_file.close()
        file.close()
    except FileNotFoundError:
        print("Error! File not found.")

def main():
    
    data_file = "" # paste filepath to your last.fm stats (ex. 'lastfmstats-user.txt')
    csv_name = "" # name your csv file (ex. 'test_test.csv')
    open_data(data_file, csv_name)

main()