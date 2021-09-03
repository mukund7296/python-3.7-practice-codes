import re
d='India represents “Unity in Diversity” . Our country is a mixture of cultures, regions, traditions, diversity in food, languages, etc. Our people of India are so polite, understanding and helping in nature. The national bird of India is Peacock and is very beautiful. India is so incredible and is full of colors and has the tiger as its national animal, hockey as its national game, etc. the national language or mother tongue of our country is Hindi. Indians are also so talented and have shown very high growth. The I.T. sector of our country shows accelerating growth due to intelligent software engineers.'

c=re.search(r"[A-Z]+",d)
print(c)