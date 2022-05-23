import re
file = open('cut_genes.fa', 'r')
fname = input('please write the new output file name:')
output = open(fname, 'w')
total = 0
name = ''
for line in file:
    if line.startswith('>'):
        y = re.search(r'\S+', line)
        name = y.group()

    else:
        cut = re.findall(r'GAATTC', line)
        for i in cut:
            total += 1

        line1 = name + '        ' + str(total) + '\n'
        line2 = line
        output.write(line1)
        output.write(line2)
        total = 0

output.close()