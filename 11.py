fname = input("Enter file name: ")
file = open(fname,"r")
keyword = "Free"
count = 0
for line in file:
    if keyword in line:
        count+=1
a=count
print('No of free items  %d' % (a))
file = open(fname,"r")
keyword = "Discount"
count = 0
for line in file:
    if keyword in line:
        count+=1
b=count
non_blank_count = 0
with open(fname,'r') as infp:
    for line in infp:
       if line.strip():
          non_blank_count += 1
print('No of items purchasd %d' % (non_blank_count-a-b))
mylines = []                              # Declare an empty list
with open (fname, 'r') as myfile:  # Open lorem.txt for reading text.
    for line in myfile:                   # For each line of text,
        mylines.append(line)              # add that line to the list.
    for element in mylines:               # For each element in the list,
        print(element)          
