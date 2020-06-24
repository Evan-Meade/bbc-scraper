import os
import csv
import bbc

OUTPUT_FILE = 'headlines.csv'

if not os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, 'w') as outfile:
        csv_writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['utc_timestamp', 'source', 'headline', 'url'])
        outfile.close()


with open(OUTPUT_FILE, 'a') as outfile:
    csv_writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

    timestamp, headline = bbc.grab_bbc()
    csv_writer.writerow([timestamp, 'BBC News', headline, bbc.BBC_URL])

    outfile.close()
