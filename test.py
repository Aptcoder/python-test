import requests, re, random, os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

page = open('python_class_question.html', 'r')
html = page.read()
# html = page.text

l = set(['YELLOW', 'CREAM', 'WHITE', 'BLUE', 'GREEN', 'PINK', 'ORANGE', 'BROWN', 'RED', 'ARSH', 'BLACK'])
# dict of color to number of appearance.
m = dict()
max_count = 0
total_count = 0

# for each color, get the number of times it appears appears
for color in l:
    color_count = len(re.findall(color, html))
    m[color] = color_count
    total_count = total_count + color_count

    if color_count > max_count:
        max_count = color_count
        most_worn = color


# print(html)
print(m)

#1. Mean of colors
mean = round(total_count / len(l))
for k, v in m.items():
    if v == mean:
        print(k ,'is the mean color', mean)
        continue

#2. Mostly worn during the week
print('Most worn color is', most_worn)

sort_counts = sorted(m.values())
median_position = len(sort_counts) // 2

#3. Median of colors
median = sort_counts[median_position]
for k, v in m.items():
    if v == median:
        print(k, 'is the median color')
        continue

probability_color_is_red = m['RED'] / total_count
#5. Probability of red
print('Probability of red ', round(probability_color_is_red, 4))


four_bits = ''.join(random.choices(['0','1'], k=4))
base_10_value = int(four_bits, 2)
#8. Probability of red
print('Random 4 bits and decimal value ',four_bits, base_10_value)



current, next = 1, 1
sum = 0
for _ in range(50):
    sum += current
    current, next = next, current + next

#9. Sum of first 50 numbers
print('Sum of first 50 numbers in fibonacci sequence', sum)




#6. Save number and their frequencies in postgres database
conn = psycopg2.connect(database=os.environ['DB_NAME'],
                        host=os.environ['DB_HOST'],
                        user=os.environ['DB_USER'],
                        password=os.environ['DB_PASSWORD'],
                        port=os.environ['DB_PORT'])

conn.autocommit = True

cursor = conn.cursor()

sql = '''INSERT INTO colors (color, count) VALUES '''
values = []
for k,v in m.items():
     values.append("('{}', {} )".format(k, v))

sql = sql + ','.join(values)
print(sql)

cursor.execute(sql)

cursor.close()