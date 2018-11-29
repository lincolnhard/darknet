import os.path

### test set ###

totalnum = 0
out_file = open('/home/lincolnhard/Pictures/coco/coco/5k-person.txt', 'w')

for line in open('/home/lincolnhard/Pictures/coco/coco/5k.txt', 'r'):
	totalnum = totalnum + 1
	idx = line[-30:-5]
	has_person = 0
	txtfilename = '/home/lincolnhard/Pictures/coco/coco/labels/val2014/%s.txt'%(idx)
	if os.path.isfile(txtfilename) == False:
		continue

	for line2 in open(txtfilename, 'r'):
		if line2[0] == '0':
			has_person = 1
			break
	if has_person:
		out_file.write(line)

out_file.close()

print 'test set total sample: ' + str(totalnum)

### training set ###

totalnum = 0
out_trainfile = open('/home/lincolnhard/Pictures/coco/coco/trainvalno5k-person.txt', 'w')
for line in open('/home/lincolnhard/Pictures/coco/coco/trainvalno5k.txt', 'r'):
    totalnum = totalnum + 1
    idx = line[44:-5]
    has_person = 0
    txtfilename = '/home/lincolnhard/Pictures/coco/coco/labels/%s.txt'%(idx)
    if os.path.isfile(txtfilename) == False:
        continue
    for line2 in open(txtfilename, 'r'):
        if line2[0] == '0':
            has_person = 1
            break
    if has_person:
        out_trainfile.write(line)
out_trainfile.close()
print 'training set total sample: ' + str(totalnum)


### test set ###

for line in open('/home/lincolnhard/Pictures/coco/coco/5k-person.txt', 'r'):
    idx = line[-30:-5]
    txtfile = open('/home/lincolnhard/Pictures/coco/coco/labels/val2014/%s.txt'%(idx), 'r')
    lines = txtfile.readlines()
    txtfile.close()
    txtfile = open('/home/lincolnhard/Pictures/coco/coco/labels/val2014/%s.txt'%(idx), 'w')
    for line2 in lines:
        if line2[0] == '0':
            txtfile.write(line2)
    txtfile.close()

### training set ###

for line in open('/home/lincolnhard/Pictures/coco/coco/trainvalno5k-person.txt', 'r'):
    idx = line[44:-5]
    txtfile = open('/home/lincolnhard/Pictures/coco/coco/labels/%s.txt'%(idx), 'r')
    lines = txtfile.readlines()
    txtfile.close()
    txtfile = open('/home/lincolnhard/Pictures/coco/coco/labels/%s.txt'%(idx), 'w')
    for line2 in lines:
        if line2[0] == '0':
            txtfile.write(line2)
    txtfile.close()
