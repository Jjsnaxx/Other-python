f = open('top100.txt','rt')
print(f)

print(f.readlines())

f.seek(0)

print(f.readlines())

f.seek(0)
for line in f:
	print(line.strip())

f.close()

f = open('test.txt','w')
f.write('test line!')
f.close()

with open('rockyou.txt',encoding = 'latin-1') as f:
	for line in f:
		pass
