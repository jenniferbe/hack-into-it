import csv
import json
import sqlite3
import numpy as np

f = open('output.csv')
post_data = list(csv.reader(f))
f.close()

# POST_DATA
# 0 Post ID
# 1 Subject
# 2 Details
# 3 Created At
# 4 Edition
# 5 Platform
# 6 Question Tags
# 7 State
# 8 Reply
# 9 Replied At
N = len(post_data)
print(N)
print(post_data[0])
print(post_data[1])

post_date_useful = np.empty(N)
for i in range(N):
	post = post_data[i]
	post_data_useful[i] = [post[1].lower(), post[2].lower(), post[8].lower()]

# tags_lists = [post_data[i][6].split(',') for i in range(1, len(post_data))]
# flattened_tags = [item.strip() for sublist in tags_lists for item in sublist]
# tags = set(flattened_tags)
# print(len(tags))
# print(tags)

# with open('tags.txt', 'w') as f:
# 	for t in tags:
# 		f.write(t + "\n")

keywords = []
with open('keywords.txt') as f:
	keywords = f.readlines()
keywords = [kw.strip().lower() for kw in keywords]
K = len(keywords)
print(K)
print(keywords)

N = 100000
post_data_filtered = []
post_data_kw = np.empty((N, K+1))
weights = np.array([10, 5, 3])
for i in range(N):
	if i % 10000 == 0:
		print(i)
	post = post_data_useful[i]
	for j in range(K):
		kw = keywords[j]
		counts = np.array([post[k].count(kw) for k in range(len(post))])
		kw_score = np.dot(weights, counts)
		post.append(kw_score)
		post_data_kw[i, j] = kw_score
		post_data_kw[i, K] += kw_score
	if post_data_kw[i, K] > 0:
		post_data_filtered.append(post)

print(np.mean(post_data_kw, 0))
print(np.std(post_data_kw, 0))

print(len(post_data_filtered))

# Create database of filtered posts (posts that contain at least one of the keywords)
conn = sqlite3.connect('post_data.db')
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


# j_file = json.load(open('tt_blog.json.txt'))






