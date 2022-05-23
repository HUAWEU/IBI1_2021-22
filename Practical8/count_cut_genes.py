<<<<<<< HEAD
import re
file = open('cut_genes.fa', 'r')
output = open('count_cut_genes.fa', 'w')
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

=======
import re
file = open('cut_genes.fa', 'r')
output = open('count_cut_genes.fa', 'w')
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

>>>>>>> e22e09b592cc8a054107ad38ad83d7f407d9cd31
output.close()