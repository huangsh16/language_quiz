import os

file = open('ques_mode(2).csv', 'r')

lis = []

for line in file :
	lis.append(line.split(',')[0])

#print(lis)

pictures = {}

for f in os.listdir('./static/resource/img') :
	pictures[f[:-4]] = 1

for name in lis :
	if name not in pictures :
		print(name)


