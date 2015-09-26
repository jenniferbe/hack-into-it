import csv
import sqlite3

conn = sqlite3.connect('people.db')
f = open('filtereddata.csv')
csv_f = csv.reader(f)
c = conn.cursor()
# Create table
c.execute('''CREATE TABLE people
             (post_id text, subject text, details text, created_at text, platform text, question_tags text, state text, reply text, replied text, click_count integer, marriage_status text, employment_status text)''')

for row in csv_f:
  for s in row:
    text = row[2]
    marriage_status = ""
    employment_status = ""
    if "husband" in text or "wife" in text or "married" in text:
        marriage_status = "married"
    if "single mom" in text or "single dad" in text or "divorced" in text or "single parent" in text:
        marriage_status = "divorced"
    if "unemployed" in text:
        employment_status = "unemployed"
    else:
        employment_status = "employed"
    # Insert a row of data
    c.execute("INSERT INTO people VALUES (" + row[0] + ", " + row[1] + ", " + row[2] + ", " + row[3] + ", " + row[4] + ", " + row[5] + ", " + row[6] + ", " + row[7] + ", " + row[8] + ", 0, " + marriage_status + ", " + employment_status + ")")

# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()






