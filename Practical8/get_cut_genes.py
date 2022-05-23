import re
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
gene = ''
# create a file to store the sequences of genes that contain sequences can be cut by EcoRI
output = open('cut_genes.fa', 'w')
count = 0
names = []
for line in file:
    line = line.rstrip()  # strip the whitespace from the right-hand side of the string
    if line.startswith('>'):
        count += 1  # count the order of the gene names
        y = re.search(r'(gene):(\S+)', line)  # search the gene names
        name = y.group(2)
        names.append(name)  # store the gene names
        length = len(gene)
        if length != 0:
            if 'GAATTC' in gene:
                order = count - 2
                line1 = '>' + names[order] + '       ' + str(length) + '\n'
                line2 = gene + '\n'
                output.write(line1)
                output.write(line2)
                gene = ''
            else:
                gene = ''
                continue
    else:
        gene = gene + line

# to check whether the last gene can be cut by EcoRI
if 'GAATTC' in gene:
    order = count - 1
    length = len(gene)
    line1 = '>' + names[order] + '       ' + str(length) + '\n'
    line2 = gene + '\n'
    output.write(line1)
    output.write(line2)
    gene = ''

output.close()
